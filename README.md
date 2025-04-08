#　 fastapi（python）のテスト用

sqlacodegenがsqlalchemyのバージョン2に対応していないためsqlalchemyバージョン1を使用
1まではOK

以下は、FastAPI で GraphQL API を通す際のフローの目次です。これを基に、実装のステップを整理していきます。

---

## 目次

1. [`sqlacodegen` を使って、既存のデータベースから SQLAlchemy モデルを自動生成](#1-sqlacodegen-を使って既存のデータベースから-sqlalchemy-モデルを自動生成)
    - 1.1. `sqlacodegen` のインストール
    - 1.2. データベーススキーマからモデルの生成

2. sqlacodegenを使ってPydantic モデルを自動生成（
<!-- 2. [`sqlalchemy2-pydantic` を使って、SQLAlchemy モデルから Pydantic モデルを自動生成](#2-sqlalchemy2-pydantic-を使って-sqlalchemy-モデルから-pydantic-モデルを自動生成)
    - 2.1. `sqlalchemy2-pydantic` のインストール
    - 2.2. Pydantic モデルの生成 -->

3. [SQLAlchemy と Pydantic を連携させる](#3-sqlalchemy-と-pydantic-を連携させる)
    - 3.1. FastAPI と GraphQL の統合
    - 3.2. GraphQL Query の実装
    - 3.3. SQLAlchemy セッションとデータベース操作

4. [GraphQL クエリの実行](#4-graphql-クエリの実行)

5. [ミューテーションの実装](#5-ミューテーションの実装)

---

### 1. `sqlacodegen` を使って、既存のデータベースから SQLAlchemy モデルを自動生成

#### 1.1. `sqlacodegen` のインストール

```bash
pip install sqlacodegen
```

#### 1.2. データベーススキーマからモデルの生成

```bash
sqlacodegen postgresql+psycopg2://user:password@localhost/mydatabase --outfile models.py
```

---

### 2. `sqlalchemy2-pydantic` を使って、SQLAlchemy モデルから Pydantic モデルを自動生成

#### 2.1. `sqlalchemy2-pydantic` のインストール

```bash
pip install sqlalchemy2-pydantic
```

#### 2.2. Pydantic モデルの生成

```python
from sqlalchemy2_pydantic import sqlalchemy_to_pydantic
from models import Actor  # sqlacodegenで生成されたActorモデル

ActorPydantic = sqlalchemy_to_pydantic(Actor)
```

---

### 3. SQLAlchemy と Pydantic を連携させる

#### 3.1. FastAPI と GraphQL の統合

```bash
pip install fastapi uvicorn strawberry-graphql[fastapi]
```

#### 3.2. GraphQL Query の実装

```python
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session
from models import Actor  # sqlacodegenで生成されたActorモデル
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy2_pydantic import sqlalchemy_to_pydantic

# SQLAlchemyの設定
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://user:password@localhost/mydatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Pydanticモデル生成
ActorPydantic = sqlalchemy_to_pydantic(Actor)

# GraphQL Query定義
@strawberry.type
class Query:
    @strawberry.field
    def get_actors(self) -> list[ActorPydantic]:
        db: Session = SessionLocal()
        actors = db.query(Actor).all()
        return [ActorPydantic.from_orm(actor) for actor in actors]

# FastAPI + GraphQL 統合
schema = strawberry.Schema(query=Query)

app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
```

#### 3.3. SQLAlchemy セッションとデータベース操作

- `SessionLocal` を使って SQLAlchemy セッションを管理
- `ActorPydantic.from_orm(actor)` を使用して、SQLAlchemy モデルのインスタンスを Pydantic モデルに変換

---

### 4. GraphQL クエリの実行

FastAPI が起動した後、`/graphql` エンドポイントにアクセスすることで、GraphQL API を実行できます。例えば、以下のような GraphQL クエリを実行できます。

```graphql
query {
  getActors {
    id
    first_name
    last_name
  }
}
```

---

### 5. ミューテーションの実装

データの変更が必要な場合、ミューテーションを作成します。例えば、`Actor` の新規作成ミューテーションは次のように実装できます。

```python
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_actor(self, first_name: str, last_name: str) -> ActorPydantic:
        db: Session = SessionLocal()
        actor = Actor(first_name=first_name, last_name=last_name)
        db.add(actor)
        db.commit()
        db.refresh(actor)
        return ActorPydantic.from_orm(actor)

schema = strawberry.Schema(query=Query, mutation=Mutation)
```

これにより、GraphQL 経由でデータを作成することができます。

---

### まとめ

FastAPI で GraphQL API を構築する際の流れを整理した結果、以下のステップで実装が進められます：

1. **SQLAlchemy モデルの自動生成**：  
   - `sqlacodegen` を使用して既存のデータベースから SQLAlchemy モデルを生成。

2. **Pydantic モデルの自動生成**：  
   - `sqlalchemy2-pydantic` を使用して、SQLAlchemy モデルから対応する Pydantic モデルを生成。

3. **FastAPI と GraphQL の統合**：  
   - `strawberry-graphql` を使用して GraphQL API を FastAPI に統合し、SQLAlchemy と Pydantic モデルを活用したデータの操作を行う。

これにより、FastAPI と GraphQL を使用した強力な API を構築できます。



==========================================
## 使用するライブラリなどの概要

## SQLAlchemy
ORM（Object-Relational Mapping）ツール

## SQLAlchemyモデル
・データベースとのやり取り
・SQLAlchemy と Pydantic モデルの統合
※SQLAlchemy モデルはデータベースとのやり取りを担当し、Pydantic モデルはそのデータを API レスポンスとして返す役割を果たす
・データの検証と整形
※Pydantic モデルを使用して、受け取ったデータを検証したり、送信するデータを整形をする。
たとえば、POST リクエストで送られてきたデータを受け取って、Pydantic モデルでバリデーションを行った後、データベースに保存するために SQLAlchemy モデルに変換。

## Pydantic
Python のデータバリデーションとデータシリアライゼーションを簡単に行うためのライブラリ

## Pydanticモデル


## fastapi
Python で高速で高性能な API を作成するための Web フレームワーク

## strawberry
GraphQL のスキーマを定義し、GraphQL サーバーを構築するためのライブラリ

===

SQLAlchemy モデルと Pydantic モデルを使用して、Strawberry で GraphQL スキーマを定義する方法について説明します。このパターンでは、SQLAlchemy モデルをデータベースとのインタラクションに使用し、Pydantic モデルをデータの検証に使用します。そして、Strawberry で GraphQL スキーマを作成します。

### 構成
1. **SQLAlchemy モデル** - データベースのテーブルを定義するために使用します。
2. **Pydantic モデル** - データ検証やシリアライゼーションを行うために使用します。
3. **Strawberry GraphQL** - GraphQL スキーマを定義します。

以下は、このパターンを実現するコードの例です。

### 1. 必要なパッケージのインストール

```bash
pip install strawberry-graphql sqlalchemy pydantic fastapi
```

### 2. SQLAlchemy モデルの定義

まず、SQLAlchemy モデルを定義して、データベースのテーブルを作成します。

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# SQLAlchemy モデル
class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

この `UserModel` は、`users` テーブルを表し、`id`, `name`, `email` のフィールドを持っています。

### 3. Pydantic モデルの定義

次に、Pydantic モデルを定義します。これを使ってデータの検証を行い、GraphQL のレスポンスとして返すデータを整形します。

```python
from pydantic import BaseModel

# Pydantic モデル
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy モデルとPydantic モデルの相互変換を有効にする
```

- `UserBase` は共通のフィールド（`name` と `email`）を定義します。
- `UserCreate` は新しいユーザー作成のために使用する Pydantic モデルです。
- `UserOut` はクエリの結果として返すユーザーデータの形式を定義し、`orm_mode = True` によって、SQLAlchemy モデルと Pydantic モデル間の変換を可能にします。

### 4. Strawberry で GraphQL スキーマの定義

次に、Strawberry を使って GraphQL スキーマを定義します。

```python
import strawberry
from typing import List

@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> List[User]:
        # データベースからユーザーを取得する
        # ここでは仮のデータを返します
        users = [
            User(id=1, name="Alice", email="alice@example.com"),
            User(id=2, name="Bob", email="bob@example.com")
        ]
        return users

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        # ユーザー作成のロジック
        # 仮に新しいユーザーを返す
        new_user = User(id=3, name=name, email=email)
        return new_user

# スキーマの作成
schema = strawberry.Schema(query=Query, mutation=Mutation)
```

### 5. FastAPI との統合

Strawberry を FastAPI と統合して、GraphQL サーバーを立ち上げます。

```python
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# FastAPI アプリケーションの作成
app = FastAPI()

# GraphQL ルーターの作成
graphql_app = GraphQLRouter(schema)

# FastAPI に GraphQL ルーターを追加
app.include_router(graphql_app, prefix="/graphql")
```

これで、FastAPI 上で動作する GraphQL サーバーが立ち上がります。

### 6. データベースとの統合

上記のコード例では、データベースとの統合を簡単にするため、仮のデータを返していますが、実際には SQLAlchemy を使ってデータベースからユーザーを取得したり、ユーザーを追加したりする必要があります。

以下は、SQLAlchemy セッションを使用して実際のデータベースと連携する例です。

```python
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# データベースの接続設定
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベースからのデータ取得を行う関数
def get_users(db: Session):
    return db.query(UserModel).all()

# クエリで使用する例
@strawberry.type
class Query:
    @strawberry.field
    def get_users(self, db: Session = Depends(get_db)) -> List[UserOut]:
        users = get_users(db)
        return [UserOut.from_orm(user) for user in users]

# ミューテーションでのユーザー作成例
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str, db: Session = Depends(get_db)) -> UserOut:
        db_user = UserModel(name=name, email=email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return UserOut.from_orm(db_user)
```

- `get_db` は、FastAPI の依存関係注入を使用してデータベースセッションを提供するための関数です。
- `UserOut.from_orm(user)` は、SQLAlchemy モデルから Pydantic モデルに変換するために使用します。

### まとめ

- **SQLAlchemy モデル**: データベース操作（データの取得、更新）を行います。
- **Pydantic モデル**: データ検証とシリアライゼーションを行います。
- **Strawberry**: GraphQL スキーマを定義し、クエリやミューテーションを通じてデータを操作します。

このパターンにより、SQLAlchemy モデルでデータベース操作を行い、Pydantic モデルでデータを検証・整形し、Strawberry で GraphQL API を提供することができます。

===

上記の例をベースにしたプロジェクトのファイル構成を整理すると、以下のようになります。この構成は、SQLAlchemy を使ってデータベース操作を行い、Pydantic モデルでデータの検証・シリアライズを行い、Strawberry と FastAPI を使って GraphQL API を提供するためのものです。

### 推奨ファイル構成

```
my_project/
│
├── app/
│   ├── __init__.py                # パッケージとして認識されるための空ファイル
│   ├── models.py                  # SQLAlchemy モデル（データベースのテーブル定義）
│   ├── schemas.py                 # Pydantic モデル（データ検証とシリアライズ）
│   ├── crud.py                    # データベース操作（クエリや挿入操作）
│   ├── graphql.py                 # GraphQL スキーマの定義（Strawberry）
│   ├── database.py                # データベース接続とセッション管理
│   └── main.py                    # FastAPI アプリケーションのエントリーポイント
│
├── alembic/                        # Alembic マイグレーションの設定
├── migrations/                     # マイグレーションファイル
├── requirements.txt                # 必要なパッケージリスト
└── .env                            # 環境変数設定（データベースURLなど）
```

### 各ファイルの内容

#### 1. `app/models.py` - SQLAlchemy モデル

SQLAlchemy モデルはデータベースのテーブル構造を定義します。

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

#### 2. `app/schemas.py` - Pydantic モデル

Pydantic モデルはデータの検証・シリアライズを行います。

```python
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy モデルとの変換を有効にする
```

#### 3. `app/crud.py` - データベース操作

データベースの操作を分離し、`SQLAlchemy` セッションを使ってデータの取得や挿入を行います。

```python
from sqlalchemy.orm import Session
from .models import UserModel
from .schemas import UserCreate

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(UserModel).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = UserModel(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

#### 4. `app/graphql.py` - GraphQL スキーマの定義

Strawberry で GraphQL のクエリとミューテーションを定義します。

```python
import strawberry
from typing import List
from .crud import get_users, create_user
from .schemas import UserOut
from sqlalchemy.orm import Session
from fastapi import Depends
from .database import get_db

@strawberry.type
class User:
    id: int
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self, db: Session = Depends(get_db)) -> List[UserOut]:
        users = get_users(db)
        return [UserOut.from_orm(user) for user in users]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str, db: Session = Depends(get_db)) -> UserOut:
        user_create = UserCreate(name=name, email=email)
        db_user = create_user(db, user_create)
        return UserOut.from_orm(db_user)

schema = strawberry.Schema(query=Query, mutation=Mutation)
```

#### 5. `app/database.py` - データベース接続とセッション管理

データベース接続の設定とセッション管理を行います。

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .models import Base
from fastapi import Depends
import os

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベースセッションを提供する依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# テーブルを作成する
Base.metadata.create_all(bind=engine)
```

#### 6. `app/main.py` - FastAPI アプリケーション

FastAPI のエントリーポイントで、GraphQL ルーターを設定して、API を立ち上げます。

```python
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .graphql import schema

app = FastAPI()

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
```

#### 7. `requirements.txt` - 必要なパッケージ

```txt
fastapi
strawberry-graphql
sqlalchemy
pydantic
uvicorn
```

#### 8. `.env` - 環境変数設定

データベース URL などの設定を `.env` ファイルに保存して、環境変数を使います。

```
DATABASE_URL=sqlite:///./test.db
```

### 9. `alembic/` と `migrations/` - データベースマイグレーション

データベースのマイグレーションを管理するために、[Alembic](https://alembic.sqlalchemy.org/) を使用する場合、`alembic.ini` ファイルとマイグレーション用のスクリプトが `alembic/` と `migrations/` に配置されます。

この部分はデータベーススキーマの変更を追跡し、マイグレーションを自動化するためのものです。

---

### 結論

この構成では、FastAPI と Strawberry を使って、SQLAlchemy モデル（データベース操作）と Pydantic モデル（データ検証）を統合し、クリーンでモジュール化されたコードを作成することができます。`crud.py` でデータベース操作を分けることで、ロジックが整理され、メンテナンスしやすくなります。
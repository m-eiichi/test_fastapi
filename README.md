#　 fastapi（python）のテスト用

sqlacodegenがsqlalchemyのバージョン2に対応していないためsqlalchemyバージョン1を使用
1まではOK

以下は、FastAPI で GraphQL API を通す際のフローの目次です。これを基に、実装のステップを整理していきます。

---

## 目次

1. [`sqlacodegen` を使って、既存のデータベースから SQLAlchemy モデルを自動生成](#1-sqlacodegen-を使って既存のデータベースから-sqlalchemy-モデルを自動生成)
    - 1.1. `sqlacodegen` のインストール
    - 1.2. データベーススキーマからモデルの生成

2. [`sqlalchemy2-pydantic` を使って、SQLAlchemy モデルから Pydantic モデルを自動生成](#2-sqlalchemy2-pydantic-を使って-sqlalchemy-モデルから-pydantic-モデルを自動生成)
    - 2.1. `sqlalchemy2-pydantic` のインストール
    - 2.2. Pydantic モデルの生成

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

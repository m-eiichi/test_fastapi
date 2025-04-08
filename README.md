２をどうするが？

Strawberry を使用して GraphQL API を実装する場合、SQLAlchemy モデルを自動生成した後に必要なステップを簡潔に説明します。以下の手順を順を追って実行することで、GraphQL API が完成します。

1. SQLAlchemy モデルを自動生成
   まず、SQLAlchemy のモデルを自動的に生成した後、Strawberry 用の GraphQL スキーマを作成するために必要なステップを進めます。

すでに SQLAlchemy モデルは生成されていると仮定し、次のステップに進みます。

2. Pydantic モデルを作成（Optional）
   GraphQL クエリを介して受け取るデータをバリデーションするために、Pydantic モデルを使うことを推奨します。

例えば、User モデルがある場合、以下のような Pydantic モデルを作成します。

python
コピーする
編集する
from pydantic import BaseModel

class UserCreate(BaseModel):
name: str
email: str

class UserUpdate(BaseModel):
name: str
email: str 3. Strawberry GraphQL 型の定義
次に、SQLAlchemy モデルに対応する GraphQL タイプを定義します。これにより、GraphQL API のレスポンスとして使用されるオブジェクトを指定できます。

python
コピーする
編集する
import strawberry
from .models import User

@strawberry.type
class UserType:
id: int
name: str
email: str
このように、Strawberry の@strawberry.type デコレーターを使って、SQLAlchemy の User モデルに対応する GraphQL タイプを作成します。

4. データベース操作関数の作成（CRUD）
   データの操作を行う関数（CRUD）を作成します。これは、SQLAlchemy を使ってデータベースに対する操作を抽象化したものです。

すでに提供した汎用的な CRUD 関数を使用して、モデルに対する操作を実装します。

python
コピーする
編集する
from sqlalchemy.orm import Session
from .models import User

def get_user(db: Session, user_id: int):
return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session):
return db.query(User).all()

def create_user(db: Session, name: str, email: str):
db_user = User(name=name, email=email)
db.add(db_user)
db.commit()
db.refresh(db_user)
return db_user

def update_user(db: Session, user_id: int, name: str, email: str):
user = db.query(User).filter(User.id == user_id).first()
if user:
user.name = name
user.email = email
db.commit()
db.refresh(user)
return user
return None

def delete_user(db: Session, user_id: int):
user = db.query(User).filter(User.id == user_id).first()
if user:
db.delete(user)
db.commit()
return True
return False 5. GraphQL Query と Mutation の定義
Query および Mutation を定義して、GraphQL API のエンドポイントを実装します。これにより、データの取得（Query）やデータの変更（Mutation）を GraphQL 経由で行うことができます。

python
コピーする
編集する
import strawberry
from typing import List
from .crud import get_users, get_user, create_user, update_user, delete_user
from .db import get_db

@strawberry.type
class Query:
@strawberry.field
def users(self) -> List[UserType]:
db = next(get_db())
return get_users(db)

    @strawberry.field
    def user(self, id: int) -> UserType | None:
        db = next(get_db())
        return get_user(db, id)

@strawberry.type
class Mutation:
@strawberry.mutation
def create_user(self, name: str, email: str) -> UserType:
db = next(get_db())
return create_user(db, name=name, email=email)

    @strawberry.mutation
    def update_user(self, id: int, name: str, email: str) -> UserType:
        db = next(get_db())
        return update_user(db, id, name, email)

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        db = next(get_db())
        return delete_user(db, id)

schema = strawberry.Schema(query=Query, mutation=Mutation) 6. FastAPI と統合
最後に、Strawberry のスキーマを FastAPI に統合します。これにより、GraphQL エンドポイントが作成され、HTTP リクエストを通じて GraphQL クエリが実行できるようになります。

python
コピーする
編集する
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schema import schema

app = FastAPI()

# GraphQL エンドポイントを FastAPI に追加

app.include_router(GraphQLRouter(schema)) 7. テストとデバッグ
最後に、FastAPI サーバを起動し、GraphQL エンドポイントを確認します。

bash
コピーする
編集する
uvicorn app:app --reload
http://127.0.0.1:8000/graphql にアクセスして、GraphQL Playground や GraphQL IDE を使って GraphQL クエリをテストします。

例えば、以下のような GraphQL クエリを送ることができます：

graphql
コピーする
編集する
query {
users {
id
name
email
}
}
まとめ
SQLAlchemy モデル → Pydantic モデル（オプション） → GraphQL タイプ → CRUD 関数 → Query / Mutation → FastAPI 統合という流れで、Strawberry と FastAPI を使った GraphQL API を構築します。

FastAPI に GraphQL を統合することで、API として利用可能な GraphQL エンドポイントが提供されます。

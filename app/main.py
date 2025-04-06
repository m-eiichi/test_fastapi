# # main.py
# import strawberry  # Strawberry (GraphQL ライブラリ) をインポート
# from graphql_schema.index import Query  # GraphQLのQueryスキーマをインポート

# # GraphQLスキーマを作成（Queryをスキーマのルートとして設定）
# schema = strawberry.Schema(query=Query)

# # FastAPIとの統合
# from fastapi import FastAPI  # FastAPI フレームワークをインポート
# from strawberry.fastapi import GraphQLRouter  # StrawberryのFastAPI用GraphQLルーターをインポート

# # FastAPIアプリケーションのインスタンスを作成
# app = FastAPI()

# # GraphQL用のルーターを作成
# graphql_app = GraphQLRouter(schema)

# # `/graphql` エンドポイントにGraphQLのルーターを追加
# app.include_router(graphql_app, prefix="/graphql")

# これにより、FastAPIのサーバーが起動すると `/graphql` でGraphQLのAPIにアクセスできるようになる
# ===================================================================

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
import models.sql_models
from graphql_types import generate_query, generate_mutation

# SQLAlchemyのセットアップ
# .env から環境変数を読み込む
if not load_dotenv():
    print(".env ファイルが見つかりません")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL が設定されていません")

print(DATABASE_URL)

# ログ出力を制御
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
engine = create_engine(DATABASE_URL, echo=DEBUG_MODE)
Session = sessionmaker(bind=engine)

# GraphQLクエリとミューテーションを動的に生成
Query = generate_query(models.sql_models)
Mutation = generate_mutation(models.sql_models)

# Strawberry GraphQL サーバーのセットアップ
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

# FastAPI アプリケーションを作成
app = FastAPI()

# GraphQLエンドポイントを追加
app.include_router(graphql_app, prefix="/graphql")

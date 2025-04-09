# import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from graphql_schema import schema 
# from graphql_types import generate_query, generate_mutation


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

# # GraphQLクエリとミューテーションを動的に生成
# Query = generate_query(models)
# Mutation = generate_mutation(models)

# # Strawberry GraphQL サーバーのセットアップ
# schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

# FastAPI アプリケーションを作成
app = FastAPI()

# GraphQLエンドポイントを追加
app.include_router(graphql_app, prefix="/graphql")

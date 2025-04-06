# main.py
import strawberry  # Strawberry (GraphQL ライブラリ) をインポート
from graphql_schema.index import Query  # GraphQLのQueryスキーマをインポート

# GraphQLスキーマを作成（Queryをスキーマのルートとして設定）
schema = strawberry.Schema(query=Query)

# FastAPIとの統合
from fastapi import FastAPI  # FastAPI フレームワークをインポート
from strawberry.fastapi import GraphQLRouter  # StrawberryのFastAPI用GraphQLルーターをインポート

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# GraphQL用のルーターを作成
graphql_app = GraphQLRouter(schema)

# `/graphql` エンドポイントにGraphQLのルーターを追加
app.include_router(graphql_app, prefix="/graphql")

# これにより、FastAPIのサーバーが起動すると `/graphql` でGraphQLのAPIにアクセスできるようになる

# import strawberry
# from fastapi import FastAPI
# from strawberry.fastapi import GraphQLRouter
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import models
# from graphql_types import generate_all_graphql_types

# # SQLAlchemyのセットアップ
# engine = create_engine('sqlite:///example.db')
# Session = sessionmaker(bind=engine)

# # モデルからGraphQL型を動的に生成
# graphql_types = generate_all_graphql_types(models)

# # Queryクラスを定義
# @strawberry.type
# class Query:
#     @strawberry.field
#     def get_items(self) -> List[graphql_types['Item']]:
#         # ここでSQLAlchemyを使ってDBからデータを取得
#         with Session() as session:
#             items = session.query(models.Item).all()
#             return items

#     @strawberry.field
#     def get_customers(self) -> List[graphql_types['Customer']]:
#         # ここでSQLAlchemyを使ってDBからデータを取得
#         with Session() as session:
#             customers = session.query(models.Customer).all()
#             return customers

# # Strawberry GraphQL サーバーのセットアップ
# schema = strawberry.Schema(query=Query)
# graphql_app = GraphQLRouter(schema)

# # FastAPI アプリケーションを作成
# app = FastAPI()

# # GraphQLエンドポイントを追加
# app.include_router(graphql_app, prefix="/graphql")

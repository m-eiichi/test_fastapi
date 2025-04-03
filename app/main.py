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

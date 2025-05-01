# graphql api

このプロジェクトは、Python を使用して構築された GraphQL API を提供するアプリケーションです。   
dbはneonをデータ自体はDVD Rental Sample Databaseを使用しています。

以下にアーキテクチャの概要を説明します。

## プロジェクト概要(実行手順)

1. vscodeで開発コンテナー：コンテナでフォルダを開くを実行  
1. sqlacodegen を使用して SQLAlchemyモデルを自動生成（初回のみ）  
　=> models.pyの生成  
1. run_generators.shの実行(コンテナ内のターミナル（appファルダ）で./run_generators.shを実行)  
　=> graphql_typesフォルダに各type / graphql_schema.py　の生成
1. Uvicornを使用してFastAPIアプリケーションを実行
1. GraphQLのエンドポイントhttp://localhost:8000/graphqlが起動。


## 主な構成要素

### FastAPI:

このプロジェクトの Web フレームワークとして使用されています。  
main.py で FastAPI アプリケーションが作成され、GraphQL エンドポイントが設定されています。
     
     FastAPIとは、PythonでWeb APIを高速に開発するための軽量で高性能なWebフレームワークです。

### Strawberry GraphQL:

GraphQL **スキーマの定義とリゾルバの実装**に使用されています。  
GraphQL スキーマは app/graphql_schema.py で定義され、strawberry.Schema を使用して構築されています。

     Strawberry GraphQLは、PythonでGraphQL APIを簡単に構築するための型ヒントベースのGraphQLライブラリです。FastAPIと非常に相性が良く、Pythonのモダンな書き方（型アノテーション）に沿って、直感的にGraphQLスキーマやリゾルバを記述できます。

### SQLAlchemyモデル:

データベース操作のために使用されています。  
モデルは app/models.py で定義されており、PostgreSQL データベースを対象としています。

     SQLAlchemyモデルとは、PythonのORM（Object Relational Mapper）ライブラリであるSQLAlchemyを使って、データベースのテーブル構造をPythonクラスとして表現したものです。
     SQLのテーブルをPythonクラスとして記述することで、Pythonコード内でデータベース操作を直感的に行える仕組みです。

### Asyncpg:

非同期データベース接続を実現するために使用されています。  
データ取得ロジックは app/graphql*schema.py 内の fetch*\*関数で実装されています。

### 自動生成スクリプト:

generate_graphql_type.py: SQLAlchemy モデルから GraphQL タイプを生成。
generate_graphql_schema.py: GraphQL スキーマを生成。

### Docker

.devcontainer ディレクトリ内に Docker 関連ファイルがあり、開発環境をコンテナ化しています。
docker-compose.yml でサービスを定義し、uvicorn を使用してアプリケーションを起動します。

### ディレクトリ構造

**app:** アプリケーションの主要なコードが含まれるディレクトリ。  
**models.py:** データベースモデル。  
**graphql_types/:** GraphQL タイプ定義。  
**graphql_schema.py:** GraphQL スキーマとリゾルバ。  
**main.py:** アプリケーションのエントリポイント。  
**.devcontainer:** 開発環境の設定ファイル。  
**README.md:** プロジェクトの概要。

### データフロー

クライアントが GraphQL エンドポイントにリクエストを送信。  
Strawberry GraphQL がリクエストを解析し、対応するリゾルバ関数を呼び出す。  
リゾルバ関数が asyncpg を使用してデータベースからデータを取得。  
データが GraphQL スキーマに基づいて整形され、クライアントに返却。  
このアーキテクチャにより、非同期処理を活用した効率的なデータ取得と、柔軟な GraphQL API の提供が可能になっています。

### .env

プロジェクト直下に.env ファイルを配置し以下を設定
DATABASE_URL=postgresql+asyncpg://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX?sslmode=require  
DB_USER=XXXXXXXXXXXX  
DB_PASSWORD=XXXXXXXXXXXX  
DB_NAME=XXXXXXXXXXXX  
DB_HOST=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

### DB

neon に対応


### その他

#### model.py / graphql_types/xxxxxxx.py / graphql_schema.pyの関係性
**model.py**
役割：アプリケーション内のデータモデル定義
Django / SQLAlchemy / Pydantic などで使われる、Pythonクラスベースのデータ定義
GraphQLの型やスキーマ生成の元になる

**graphql_types/xxxxxxx.py**
役割：GraphQLの型定義（type definitions）を自動生成
model.py などのモデル情報をもとに、GraphQLの type, input, enum などを生成

**graphql_schema.py**
役割：GraphQLスキーマを定義（型とリゾルバを紐づけ）
graphql_types で定義された型を使って、実際にクエリやミューテーションを定義
Graphene や Ariadne のような GraphQL ライブラリで使う

```
model.py（データモデル定義）
     ↓
graphql_types（GraphQL型定義を生成）
     ↓
graphql_schema.py（スキーマ・クエリ・リゾルバ構築）
```


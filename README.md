# graphql api

このプロジェクトは、Python を使用して構築された GraphQL API を提供するアプリケーションです。以下にアーキテクチャの概要を説明します。

## 主な構成要素

### FastAPI:

このプロジェクトの Web フレームワークとして使用されています。
main.py で FastAPI アプリケーションが作成され、GraphQL エンドポイントが設定されています。

### Strawberry GraphQL:

GraphQL スキーマの定義とリゾルバの実装に使用されています。
GraphQL スキーマは app/graphql_schema.py で定義され、strawberry.Schema を使用して構築されています。

### SQLAlchemy:

データベース操作のために使用されています。
モデルは app/models.py で定義されており、PostgreSQL データベースを対象としています。

### Asyncpg:

非同期データベース接続を実現するために使用されています。
データ取得ロジックは app/graphql*schema.py 内の fetch*\*関数で実装されています。

### 自動生成スクリプト:

GraphQL タイプやスキーマを自動生成するためのスクリプトが用意されています。
generate_graphql_type.py: SQLAlchemy モデルから GraphQL タイプを生成。
generate_graphql_schema.py: GraphQL スキーマを生成。
Docker 環境:

### Docker

.devcontainer ディレクトリ内に Docker 関連ファイルがあり、開発環境をコンテナ化しています。
docker-compose.yml でサービスを定義し、uvicorn を使用してアプリケーションを起動します。

### ディレクトリ構造

app: アプリケーションの主要なコードが含まれるディレクトリ。
models.py: データベースモデル。
graphql_types/: GraphQL タイプ定義。
graphql_schema.py: GraphQL スキーマとリゾルバ。
main.py: アプリケーションのエントリポイント。
.devcontainer: 開発環境の設定ファイル。
README.md: プロジェクトの概要。

### データフロー

クライアントが GraphQL エンドポイントにリクエストを送信。
Strawberry GraphQL がリクエストを解析し、対応するリゾルバ関数を呼び出す。
リゾルバ関数が asyncpg を使用してデータベースからデータを取得。
データが GraphQL スキーマに基づいて整形され、クライアントに返却。
このアーキテクチャにより、非同期処理を活用した効率的なデータ取得と、柔軟な GraphQL API の提供が可能になっています。

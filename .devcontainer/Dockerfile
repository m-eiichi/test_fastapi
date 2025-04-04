FROM python:3.11

# 作業ディレクトリ
WORKDIR /app

# Python環境のセットアップ
COPY requirements.txt .

# 本番用に依存関係をインストール（開発用にはコメントアウト）
RUN pip install --no-cache-dir -r requirements.txt

# entrypoint.sh をコピー
# COPY .devcontainer/entrypoint.sh /app/entrypoint.sh

# スクリプトに実行権限を与える
# RUN chmod +x /app/entrypoint.sh

# ENTRYPOINT ["/app/entrypoint.sh"]

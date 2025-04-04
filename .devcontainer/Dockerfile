FROM python:3.11

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    python3-pip \
    && rm -rf /var/lib/apt/lists/* 

# 作業ディレクトリ
WORKDIR /app

# Python環境のセットアップ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 環境変数を設定（Pythonのモジュール検索パスを追加）
ENV PYTHONPATH=/app

# CMD ["python"]




# FROM python:3.10

# WORKDIR /app
# COPY entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

# # sqlacodegen のインストール
# RUN pip install sqlacodegen psycopg2-binary

# # 環境変数を有効にしてエントリーポイントを設定
# ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python", "app.py"]  # 任意のアプリ起動コマンド

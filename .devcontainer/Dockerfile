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

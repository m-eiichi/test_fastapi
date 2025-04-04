#!/bin/sh
set -e

# 環境変数が正しく読み込まれているかチェック
if [ -z "$DATABASE_URL" ]; then
    echo "DATABASE_URL is not set. Exiting..."
    exit 1
fi

# 初回のみ sqlacodegen を実行
if [ ! -f /app/models.py ]; then
    echo "Generating models.py..."
    sqlacodegen "$DATABASE_URL" --outfile /app/models.py
else
    echo "models.py already exists. Skipping generation."
fi

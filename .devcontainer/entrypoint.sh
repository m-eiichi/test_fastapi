#!/bin/bash
set -e

GENERATED_FILE="models/__init__.py"

# 初回のみ実行: models/__init__.py がない場合に限り実行
if [ ! -f "$GENERATED_FILE" ]; then
    echo "sqlacodegen を初回実行中..."
    sqlacodegen postgresql://user:password@db:5432/mydb --outfile $GENERATED_FILE
else
    echo "sqlacodegen は既に実行済み"
fi

# アプリケーション実行（例: uvicorn or flask or custom）
# exec python your_app.py

#!/bin/bash
set -e

GENERATED_DIR="/app/models"
GENERATED_FILE="$GENERATED_DIR/__init__.py"

if [ ! -f "$GENERATED_FILE" ]; then
    echo "sqlacodegen を初回実行中..."
    mkdir -p "$GENERATED_DIR"
    sqlacodegen "$DATABASE_URL" --outfile "$GENERATED_FILE" #SQLAlchemyモデルを自動的に生成
else
    echo "sqlacodegen は既に実行済み"
fi

exec "$@"
# exec python your_app.py
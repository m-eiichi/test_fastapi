#!/bin/bash
set -e
set -x  # ここでデバッグ出力を有効

GENERATED_FILE="/app/models_sqlalchemy.py"
GENERATED_FILE2="/app/models_pydantic.py"

if [ ! -f "$GENERATED_FILE" ]; then
    echo "sqlacodegen を初回実行中..."
    sqlacodegen "$DATABASE_URL" --outfile "$GENERATED_FILE" #SQLAlchemyモデルを自動的に生成
else
    echo "sqlacodegen は既に実行済み"
fi

exec "$@"
# exec python your_app.py
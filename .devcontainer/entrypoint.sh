#!/bin/bash
set -e

echo "Checking Neon DB connection..."
until psql "$DATABASE_URL" -c '\q' 2>/dev/null; do
  echo "Waiting for Neon DB..."
  sleep 1
done

MODEL_FILE="app/models.py"

if [ ! -f "$MODEL_FILE" ]; then
  echo "Running sqlacodegen..."
  sqlacodegen "$DATABASE_URL" --outfile "$MODEL_FILE"
else
  echo "Model already exists"
fi

echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload --log-level debug


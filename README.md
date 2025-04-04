#　 fastapi（python）のテスト用


## sqlacodegen自動化

`devcontainer` (`.devcontainer/devcontainer.json`) を使って `sqlacodegen` の初回実行を自動化する方法を説明します。

---

## **手順**
### **1. `.devcontainer/devcontainer.json` を作成・修正**
開発コンテナの設定を定義します。

```json
{
  "name": "My Dev Container",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "runArgs": ["--env-file", ".env"],  // .env を読み込む
  "postCreateCommand": "/bin/sh /app/entrypoint.sh",
  "remoteUser": "vscode",
  "mounts": [
    "source=${localWorkspaceFolder},target=/app,type=bind"
  ],
  "extensions": [
    "ms-python.python"
  ]
}
```
- `runArgs`: `.env` を環境変数として渡す。
- `postCreateCommand`: 初回起動時に `entrypoint.sh` を実行。

---

### **2. `.env` を作成**
`.devcontainer/.env` にデータベースの接続情報を記載します。

```
DATABASE_URL=postgresql://dvdrental_owner:xxxxxxxxx@xxxxxxxxx/dvdrental
```

---

### **3. `entrypoint.sh` を作成**
`models.py` がない場合のみ `sqlacodegen` を実行します。

```sh
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
```

---

### **4. `Dockerfile` を作成**
Python の開発環境をセットアップします。

```dockerfile
FROM python:3.10

WORKDIR /app
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# sqlacodegen のインストール
RUN pip install sqlacodegen psycopg2-binary
```

---

### **5. `.gitignore` に `.env` を追加**
`.env` ファイルが Git にコミットされないように `.gitignore` に追加します。

```
.devcontainer/.env
```

---

## **動作確認**
1. **VS Code で Dev Container を起動**
   - 「**Remote - Containers**」拡張機能をインストール
   - `F1` → `Remote-Containers: Reopen in Container` を選択

2. **コンテナが起動**
   - `postCreateCommand` により `entrypoint.sh` が実行される
   - `models.py` がない場合のみ `sqlacodegen` が実行される

3. **再起動時**
   - `models.py` がある場合は `sqlacodegen` は実行されない

---

### **まとめ**
`.devcontainer` を使うことで、Docker Compose なしで開発コンテナを管理しつつ、初回のみ `sqlacodegen` を実行できるようになりました！
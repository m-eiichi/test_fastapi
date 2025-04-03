はい、**接続しているデータベース（例：PostgreSQL）から自動的に Pydantic モデルを生成する方法**はあります。  
これは、特にテーブルが多いプロジェクトで、手動で `BaseModel` を書くのが大変なときにとても便利です。

以下のような方法が主に使われます：

---

## ✅ 1. **SQLAlchemy + Pydantic の自動生成**

まず、SQLAlchemy の ORM モデルを使ってデータベースからテーブル構造を取得し、そこから Pydantic モデルを自動生成するのが一般的です。

### ステップ 1：SQLAlchemy モデルを自動生成する（db-first）
```bash
pip install sqlacodegen psycopg2-binary
```

```bash
sqlacodegen postgresql://ユーザー名:パスワード@ホスト名:ポート/データベース名 --outfile models.py
```

例：
```bash
sqlacodegen postgresql://dvdrental_owner:xxxxxxxxx@xxxxxxxxx/dvdrental --outfile models.py
```

これで `models.py` に SQLAlchemy の ORM モデルが出力されます。

---

### ステップ 2：SQLAlchemy モデルから Pydantic モデルを自動生成

```python
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from models import Customer  # さっき作ったSQLAlchemyモデル

CustomerSchema = sqlalchemy_to_pydantic(Customer)
```

または、すこし手動で制御したい場合：

```python
CustomerSchema = sqlalchemy_to_pydantic(Customer, exclude=["some_column"])
```

> `pydantic_sqlalchemy` パッケージを使う場合：
```bash
pip install pydantic_sqlalchemy
```

---

## ✅ 2. **`sqlmodel` を使う方法（SQLAlchemy + Pydanticが統合されたモデル）**
これも便利ですが、既存のDBからの自動生成には対応していないため、最初のステップでは `sqlacodegen` などで SQLAlchemy モデルを作成し、手動で `sqlmodel.SQLModel` に変換する必要があります。

---

## 🔁 自動生成のまとめ
| 方法 | 内容 |
|------|------|
| `sqlacodegen` | DBからSQLAlchemyモデルを生成 |
| `pydantic_sqlalchemy` | SQLAlchemyモデルからPydanticモデルを生成 |
| `sqlmodel` | SQLAlchemy + Pydantic の統合モデル（自動生成には向かない） |

---

## ✨ 補足：FastAPI + GraphQL 用なら...
GraphQL スキーマも自動生成したい場合、SQLAlchemy モデル → Strawberry type への変換ライブラリ（またはカスタム関数）を使うこともできます。必要であればそちらも紹介します！

---

必要な部分だけでなく、全体を自動で整備したい場合もあると思うので、
「SQLAlchemyモデルからPydantic＋Strawberry両方に落としたい」などの方針があれば教えてください。それに合ったベストな構成を提案します。
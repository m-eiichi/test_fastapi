# Flow
main 
↓
graphql_schema
↓
schemas/db
=====================================================

# 用語
---

## **Pydantic の `Schema`**

### **役割**
- **Pydantic** は Python のデータ検証および設定管理ライブラリです。  
- **`Schema`** は、データのバリデーションやデシリアライズ/シリアライズのために使用される **Pydantic モデル** です。
  - 例えば、GraphQL のレスポンスやリクエストボディで使われます。

### **主な特徴**
- **データ検証**：データが正しい形式かどうかを検証します（例えば、文字列が `str` 型かどうか、日付が `datetime` 型かどうかなど）。
- **シリアライズ**：Python のオブジェクト（例えば SQLAlchemy モデル）を JSON 形式に変換します。
- **デシリアライズ**：JSON 形式のデータを Python のオブジェクトに変換します。

### **例：`CustomerSchema`**
```python
from pydantic import BaseModel

class CustomerSchema(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    active: bool

    class Config:
        from_attributes = True  # SQLAlchemy モデルから変換可能にする
```

### **主な用途**
- API のレスポンスやリクエストで使われます。
- データベースとのやり取りではなく、データの検証と変換を主に担当します。

---

## **SQLAlchemy の ORM モデル**

### **役割**
- **SQLAlchemy** は Python の **ORM（Object-Relational Mapping）** ライブラリで、SQL と Python オブジェクトを簡単に相互変換するためのツールです。
- **ORM モデル** は、データベースのテーブルを表す Python クラスで、SQLAlchemy がこのモデルを使って SQL クエリを生成したり、データベースとのやり取りを管理します。

### **主な特徴**
- **テーブルマッピング**：Python クラスがデータベースのテーブルと1対1で対応し、クラスのインスタンスがデータベースのレコードを表します。
- **クエリ実行**：ORM モデルを使ってデータベースに対するクエリ（SELECT, INSERT, UPDATE, DELETE）を発行します。
- **セッション管理**：データベースとの接続やトランザクション管理を担当します。

### **例：`CustomerModel`（SQLAlchemy ORM モデル）**
```python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 基底クラスを作成

class CustomerModel(Base):
    __tablename__ = 'customer'  # データベースのテーブル名

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    active = Column(Boolean, default=True)
```

### **主な用途**
- **データベースとの直接的なやり取り**：SQLAlchemy ORM モデルは、データベースに対して直接クエリを実行するために使用されます。
- **データベーステーブルと対応**：Python オブジェクトとデータベースレコードの変換を管理します。

---

## **Pydantic の `CustomerSchema` と SQLAlchemy の ORM モデルの違い**

| 項目                   | **Pydantic (`CustomerSchema`)**                                | **SQLAlchemy ORM モデル (`CustomerModel`)**                |
|------------------------|---------------------------------------------------------------|------------------------------------------------------------|
| **役割**               | データ検証、デシリアライズ、シリアライズ                       | データベースとのやり取り（テーブルの定義、クエリ実行）      |
| **用途**               | API リクエスト/レスポンスのデータ形式の検証                   | データベーステーブルのマッピングとクエリ実行                |
| **データ検証**         | ✅ 入力データの検証（例：型、必須項目）                        | ❌ 入力データの検証機能なし（SQLAlchemy のモデル自体は検証しない）|
| **シリアライズ/デシリアライズ** | ✅ JSON との変換（Pydantic モデル → JSON）                     | ❌ シリアライズ/デシリアライズ機能なし（SQLAlchemy モデル自体は対象外） |
| **データベース操作**   | ❌ SQLAlchemy モデルを介して直接的なデータベース操作は行わない   | ✅ データベースへのクエリ（INSERT, SELECT など）を実行      |

---

## **結論**
- **Pydantic モデル (`CustomerSchema`)** は主に **データのバリデーションや変換** を行うために使用されます。これを GraphQL や API で使用します。
- **SQLAlchemy ORM モデル (`CustomerModel`)** は、**データベースとのやり取り**を管理するためのものです。これを使ってデータベースに対してクエリを実行します。

両者は用途が異なり、`SQLAlchemy ORM モデル` はデータベース操作を担当し、`Pydantic モデル` はデータの検証や変換を担当します。そのため、クエリ実行時には SQLAlchemy の ORM モデルを使用し、レスポンスデータを返す時に Pydantic モデルに変換して返す形が一般的です。
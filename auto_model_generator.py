from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy import Table
import inspect

# .env から環境変数を読み込む
if not load_dotenv():
    print(".env ファイルが見つかりません")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL が設定されていません")

# エンジンの作成
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# データベースからテーブルをリフレクションで取得
metadata.reflect(bind=engine)

# Baseクラスを宣言
Base = declarative_base(metadata=metadata)

# テーブルをリフレクションで取得して、自動的にクラスを作成
def auto_generate_models():
    models = {}
    for table_name, table in metadata.tables.items():
        # 動的にクラスを生成
        class_name = table_name.capitalize()  # クラス名はテーブル名を大文字に
        model_class = type(class_name, (Base,), {'__tablename__': table_name})
        # カラムを動的に定義
        for column in table.columns:
            setattr(model_class, column.name, column)
        models[class_name] = model_class
    return models

# モデルを自動生成
models = auto_generate_models()

# 例えば、User モデルを取得
User = models['Users']

# セッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic

# データベース URL
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# SQLAlchemy モデルの定義場所
MODEL_FILE = "models_sqlalchemy.py"

# 出力する Pydantic モデルファイル
OUTPUT_FILE = "models_pydantic.py"

# モデルをインポートする
# models_sqlalchemy.py からすべての SQLAlchemy モデルをインポート
# (exec を使って動的にインポートする)
with open(MODEL_FILE) as f:
    exec(f.read())

# Pydantic モデルを生成してファイルに書き込む
with open(OUTPUT_FILE, 'w') as pydantic_file:
    pydantic_file.write('from pydantic import BaseModel\n\n')

    # SQLAlchemy モデルのクラスをループで回す
    for model_name in dir():
        model = globals().get(model_name)
        if isinstance(model, type) and hasattr(model, '__tablename__'):
            # SQLAlchemy モデルから Pydantic モデルを生成
            pydantic_model = sqlalchemy_to_pydantic(model)
            
            # Pydantic モデルをファイルに書き込む
            pydantic_file.write(f"\n\nclass {model_name}Pydantic(BaseModel):\n")
            
            # Pydantic モデルのフィールドを追加
            for field in pydantic_model.__annotations__:
                pydantic_file.write(f"    {field}: {pydantic_model.__annotations__[field]}\n")
            
            # Pydantic モデルの Config を追加
            pydantic_file.write("    class Config:\n")
            pydantic_file.write("        orm_mode = True\n")

print(f"Pydantic モデルが {OUTPUT_FILE} に生成されました。")

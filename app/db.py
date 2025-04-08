from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
import os
from dotenv import load_dotenv

# .env から環境変数を読み込む
if not load_dotenv():
    print(".env ファイルが見つかりません")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL が設定されていません")

print(DATABASE_URL)

# ログ出力を制御
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
engine = create_engine(DATABASE_URL, echo=DEBUG_MODE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 既存のテーブルを自動マッピング
# Base = automap_base()
# Base.prepare(autoload_with=engine) 

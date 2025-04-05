# generate_pydantic_models.py

import os
import importlib.util
from typing import Type
from pathlib import Path

from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.orm import DeclarativeMeta

# SQLAlchemyモデルのパス
SQL_MODEL_PATH = Path("/app/models/sql_models.py")
PYDANTIC_MODEL_PATH = Path("/app/models/pydantic_models.py")

# モジュールを動的に読み込む
spec = importlib.util.spec_from_file_location("sql_models", SQL_MODEL_PATH)
sql_models = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sql_models)

# ベースクラスの取得（Baseクラス継承で判定）
Base: DeclarativeMeta = sql_models.Base
models = []

for name in dir(sql_models):
    attr = getattr(sql_models, name)
    if isinstance(attr, type) and hasattr(attr, "__tablename__"):
        models.append(attr)

# Pydanticモデルの出力内容
lines = [
    "from pydantic import BaseModel\n",
    "from typing import Optional, List\n",
    "import datetime\n",
    "\n"
]

for model in models:
    model_name = model.__name__
    create_model = sqlalchemy_to_pydantic(model, exclude=["id"])
    response_model = sqlalchemy_to_pydantic(model)

    lines.append(f"class {model_name}Create({create_model.__name__}):\n    pass\n\n")
    lines.append(f"class {model_name}Response({response_model.__name__}):\n    pass\n\n")

# ファイルとして保存
with open(PYDANTIC_MODEL_PATH, "w") as f:
    f.writelines(lines)

print(f"Pydantic モデルを {PYDANTIC_MODEL_PATH} に生成しました。")

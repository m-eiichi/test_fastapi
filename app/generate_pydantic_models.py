# generate_pydantic_models.py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from models.sql_models import Base
from sqlalchemy.orm import class_mapper
from typing import List, Type

def generate_pydantic_models(base_class: Type[Base]):
    # SQLAlchemy モデルをリスト化
    models = [cls for cls in base_class._decl_class_registry.values() if isinstance(cls, type) and issubclass(cls, Base)]
    
    pydantic_models = {}

    for model in models:
        model_name = model.__name__
        
        # Create モデルを生成
        user_create_model = sqlalchemy_to_pydantic(model, exclude=["actor_id", "category_id", "country_id"])  # 主キーは除外
        pydantic_models[f'{model_name}Create'] = user_create_model
        
        # Response モデルを生成
        user_response_model = sqlalchemy_to_pydantic(model)
        pydantic_models[f'{model_name}Response'] = user_response_model

    # pydantic_models に保存
    with open("models/pydantic_models.py", "w") as f:
        for model_name, model in pydantic_models.items():
            f.write(f"{model_name} = {model}\n")

# 自動生成を実行
generate_pydantic_models(Base)

# generate_pydantic_models.py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
import models

# モデルリストを取得
models_list = [getattr(models, attr) for attr in dir(models) if isinstance(getattr(models, attr), type) and issubclass(getattr(models, attr), models.Base)]

# SQLAlchemyモデルからPydanticモデルを生成
for model in models_list:
    pydantic_model = sqlalchemy_to_pydantic(model)
    globals()[f"{model.__name__}Pydantic"] = pydantic_model

    # 生成されたPydanticモデルを確認するために出力
    print(f"Pydantic model generated for {model.__name__}: {pydantic_model}")

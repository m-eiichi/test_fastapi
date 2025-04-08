from sqlalchemy_to_pydantic import sqlalchemy_to_pydantic
import models

models_list = [
    getattr(models, attr)
    for attr in dir(models)
    if isinstance(getattr(models, attr), type)
    and issubclass(getattr(models, attr), models.Base)
    and getattr(models, attr) is not models.Base
]

for model in models_list:
    # 全体のベースモデル
    PydanticBase = sqlalchemy_to_pydantic(model)

    # Read（すべてのフィールドを含める）
    ReadModel = type(f"{model.__name__}Read", (PydanticBase,), {})

    # Create/Update（主キーなどを除外したい場合はカスタマイズが必要）
    # ここでは一旦ベースと同じにしている
    CreateUpdateModel = type(f"{model.__name__}CreateUpdate", (PydanticBase,), {})

    # 動作確認
    print(f"✅ {model.__name__} → Read: {ReadModel.__name__}, CreateUpdate: {CreateUpdateModel.__name__}")

    # 必要に応じて globals に追加
    globals()[f"{model.__name__}Read"] = ReadModel
    globals()[f"{model.__name__}CreateUpdate"] = CreateUpdateModel

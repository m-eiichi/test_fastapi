from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import class_mapper
from typing import List, Type
from sqlalchemy.ext.declarative import declarative_base

# # SQLAlchemy モデルを定義するベースクラス
Base = declarative_base()

# # 以下は例として、SQLAlchemy モデルの定義です（あなたのコードと同様）
# class Actor(Base):
#     __tablename__ = 'actor'
#     actor_id = Column(Integer, primary_key=True)
#     first_name = Column(String(45))
#     last_name = Column(String(45))
#     last_update = Column(DateTime, server_default=text('now()'))
#     film_actor = relationship('FilmActor', back_populates='actor')

# class Category(Base):
#     __tablename__ = 'category'
#     category_id = Column(Integer, primary_key=True)
#     name = Column(String(25))
#     last_update = Column(DateTime, server_default=text('now()'))
#     film_category = relationship('FilmCategory', back_populates='category')

# class Country(Base):
#     __tablename__ = 'country'
#     country_id = Column(Integer, primary_key=True)
#     country = Column(String(50))
#     last_update = Column(DateTime, server_default=text('now()'))

# 自動生成する関数
def generate_pydantic_models(base_class: Type[Base]):
    # Base.metadata.tables で定義されたすべてのテーブルを取得
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

    return pydantic_models


# Pydantic モデルを生成
generated_models = generate_pydantic_models(Base)

# 生成された Pydantic モデルの確認
for model_name, model in generated_models.items():
    print(f"Generated Pydantic model: {model_name}")
    print(model.schema())

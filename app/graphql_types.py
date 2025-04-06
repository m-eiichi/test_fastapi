import strawberry
from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Type, Optional
import os
from dotenv import load_dotenv

# SQLAlchemy Baseの定義
Base: DeclarativeMeta = declarative_base()

# セッションの作成
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

# SQLAlchemyモデルクラスからGraphQL型を動的に生成する関数
def generate_graphql_type(model_class: Type[DeclarativeMeta]):
    model_columns = inspect(model_class).c

    annotations = {}
    for column in model_columns:
        field_type = str
        if column.type.__class__.__name__ == 'Integer':
            field_type = int
        elif column.type.__class__.__name__ == 'DateTime':
            field_type = str  # 日付型も文字列で
        annotations[column.name] = field_type

    # 動的クラス作成
    graphql_type = type(
        f"{model_class.__name__}Type",
        (),
        {
            "__annotations__": annotations,
            "__module__": __name__,
        }
    )

    return strawberry.type(graphql_type)

def generate_all_graphql_types(models_module):
    """
    モジュール内の全てのSQLAlchemyモデルからGraphQL型を生成
    """
    graphql_types = {}
    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, Base) and hasattr(model, '__tablename__'):
            graphql_types[name] = generate_graphql_type(model)
    return graphql_types

def generate_query(models_module):
    query_fields = {}

    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, Base) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)
            query_fields[f'get_{name.lower()}s'] = strawberry.field(lambda self, info: get_items(model))

    query_class = type("Query", (), query_fields)
    return strawberry.type(query_class)

def generate_mutation(models_module):
    mutation_fields = {}

    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, Base) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)
            mutation_fields[f'create_{name.lower()}'] = strawberry.mutation(lambda self, obj: create_item(model, obj))
            mutation_fields[f'update_{name.lower()}'] = strawberry.mutation(lambda self, obj: update_item(model, obj))
            mutation_fields[f'delete_{name.lower()}'] = strawberry.mutation(lambda self, id: delete_item(model, id))

    # 動的にクラスを定義して strawberry.type でラップ
    mutation_class = type("Mutation", (), mutation_fields)
    return strawberry.type(mutation_class)

def get_items(model):
    """
    指定されたモデルに基づいてデータを取得する関数
    """
    with SessionLocal() as session:  # SessionLocalを使ってセッションを開始
        items = session.query(model).all()
        return items

def create_item(model, obj):
    """
    指定されたモデルの新しいレコードを作成する
    """
    with SessionLocal() as session:  # SessionLocalを使ってセッションを開始
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

def update_item(model, obj):
    """
    指定されたモデルのレコードを更新する
    """
    with SessionLocal() as session:  # SessionLocalを使ってセッションを開始
        session.merge(obj)  # merge はオブジェクトを更新
        session.commit()
        session.refresh(obj)
        return obj

def delete_item(model, id):
    """
    指定されたモデルのレコードを削除する
    """
    with SessionLocal() as session:  # SessionLocalを使ってセッションを開始
        obj = session.query(model).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False

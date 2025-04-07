import strawberry
from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from typing import Any, List, Optional, Type
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
    # GraphQLタイプを一度だけ生成
    graphql_type_name = f'{model_class.__name__}Type'

    if hasattr(model_class, '__strawberry_definition__'):
        return model_class.__strawberry_definition__

    # 新しく生成する
    graphql_type = strawberry.type(model_class, name=graphql_type_name)
    model_class.__strawberry_definition__ = graphql_type
    return graphql_type


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

def generate_query(models_module, base_class):
    query_fields = {}

    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, base_class) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)

            # ラムダの代わりに明示的な関数でクロージャ
            def make_get_items_resolver(model):
                def resolver(self, info) -> list[graphql_type]:  # 型ヒントもOK
                    return get_items(model)
                return resolver

            query_fields[f'get_{name.lower()}s'] = strawberry.field(resolver=make_get_items_resolver(model))

    query_class = type("Query", (), query_fields)
    return strawberry.type(query_class)



def generate_mutation(models_module, base_class):
    mutation_fields = {}

    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, base_class) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)

            def make_create(m, g_type):
                @strawberry.mutation
                def create(self, obj: Any) -> g_type:  # 👈 Here: Return type is graphql_type
                    return create_item(m, obj)
                return create

            def make_update(m, g_type):
                @strawberry.mutation
                def update(self, obj: Any) -> g_type:
                    return update_item(m, obj)
                return update

            def make_delete(m):
                @strawberry.mutation
                def delete(self, id: int) -> bool:  # 👈 Explicit bool return
                    return delete_item(m, id)
                return delete

            mutation_fields[f'create_{name.lower()}'] = make_create(model, graphql_type)
            mutation_fields[f'update_{name.lower()}'] = make_update(model, graphql_type)
            mutation_fields[f'delete_{name.lower()}'] = make_delete(model)

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

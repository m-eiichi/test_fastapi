import strawberry
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import List, Type, Optional

# SQLAlchemyモデルクラスからGraphQL型を動的に生成する関数
def generate_graphql_type(model_class: DeclarativeMeta):
    """
    SQLAlchemyモデルクラスからGraphQL型を動的に生成する
    """
    model_columns = inspect(model_class).c

    # フィールドを動的に作成
    fields = {}
    for column in model_columns:
        field_type = str  # デフォルトを文字列型に設定
        if column.type.__class__.__name__ == 'Integer':
            field_type = int
        elif column.type.__class__.__name__ == 'String':
            field_type = str
        elif column.type.__class__.__name__ == 'DateTime':
            field_type = str  # 日付型も文字列として扱う場合
        fields[column.name] = strawberry.field(type=field_type)

    # GraphQLタイプを定義
    return strawberry.type(model_class.__name__, **fields)

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
    """
    モジュール内のSQLAlchemyモデルに基づいてGraphQLのQueryクラスを動的に生成する
    """
    query_fields = {}

    # 各モデルに対して、Queryフィールドを作成
    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, Base) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)  # モデルに対応するGraphQLタイプを生成
            query_fields[f'get_{name.lower()}s'] = strawberry.field(lambda self, _: get_items(model))

    # Queryクラスを動的に生成
    return strawberry.type("Query", **query_fields)

def generate_mutation(models_module):
    """
    モジュール内のSQLAlchemyモデルに基づいてGraphQLのMutationクラスを動的に生成する
    """
    mutation_fields = {}

    # 各モデルに対して、Mutationフィールドを作成
    for name in dir(models_module):
        model = getattr(models_module, name)
        if isinstance(model, type) and issubclass(model, Base) and hasattr(model, '__tablename__'):
            graphql_type = generate_graphql_type(model)  # モデルに対応するGraphQLタイプを生成
            mutation_fields[f'create_{name.lower()}'] = strawberry.mutation(lambda self, obj: create_item(model, obj))
            mutation_fields[f'update_{name.lower()}'] = strawberry.mutation(lambda self, obj: update_item(model, obj))
            mutation_fields[f'delete_{name.lower()}'] = strawberry.mutation(lambda self, id: delete_item(model, id))

    # Mutationクラスを動的に生成
    return strawberry.type("Mutation", **mutation_fields)

def get_items(model):
    """
    指定されたモデルに基づいてデータを取得する関数
    """
    with Session() as session:
        items = session.query(model).all()
        return items

def create_item(model, obj):
    """
    指定されたモデルの新しいレコードを作成する
    """
    with Session() as session:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

def update_item(model, obj):
    """
    指定されたモデルのレコードを更新する
    """
    with Session() as session:
        session.merge(obj)  # merge はオブジェクトを更新
        session.commit()
        session.refresh(obj)
        return obj

def delete_item(model, id):
    """
    指定されたモデルのレコードを削除する
    """
    with Session() as session:
        obj = session.query(model).get(id)
        if obj:
            session.delete(obj)
            session.commit()
            return True
        return False

from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from typing import List, Optional
from .models import Base
from sqlalchemy.orm import Query

# 汎用的な CRUD 操作を定義するための関数
def create(db: Session, model_class: Base, **kwargs) -> Base:
    """
    Create a new record in the database.
    """
    instance = model_class(**kwargs)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance


def get(db: Session, model_class: Base, model_id: int) -> Optional[Base]:
    """
    Get a record by id.
    """
    return db.query(model_class).filter(model_class.id == model_id).first()


def get_all(db: Session, model_class: Base) -> List[Base]:
    """
    Get all records.
    """
    return db.query(model_class).all()


def update_record(db: Session, model_class: Base, model_id: int, **kwargs) -> Optional[Base]:
    """
    Update an existing record.
    """
    instance = db.query(model_class).filter(model_class.id == model_id).first()
    if instance:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        db.commit()
        db.refresh(instance)
        return instance
    return None


def delete_record(db: Session, model_class: Base, model_id: int) -> bool:
    """
    Delete a record.
    """
    instance = db.query(model_class).filter(model_class.id == model_id).first()
    if instance:
        db.delete(instance)
        db.commit()
        return True
    return False


# モデルに基づいた CRUD 関数の自動生成
def generate_crud_for_model(model_class: Base):
    """
    Generate CRUD operations for a given model class.
    """
    model_name = model_class.__name__

    globals()[f"create_{model_name.lower()}"] = lambda db, **kwargs: create(db, model_class, **kwargs)
    globals()[f"get_{model_name.lower()}"] = lambda db, model_id: get(db, model_class, model_id)
    globals()[f"get_all_{model_name.lower()}"] = lambda db: get_all(db, model_class)
    globals()[f"update_{model_name.lower()}"] = lambda db, model_id, **kwargs: update_record(db, model_class, model_id, **kwargs)
    globals()[f"delete_{model_name.lower()}"] = lambda db, model_id: delete_record(db, model_class, model_id)

# 使用例
# from .models import User, Post  # モデルのインポート

# # 自動生成された CRUD 関数を使用
# generate_crud_for_model(User)
# generate_crud_for_model(Post)

# これで自動生成された関数が以下のように使用できます
# create_user(db, name="John", email="john@example.com")
# get_user(db, user_id=1)
# get_all_user(db)
# update_user(db, user_id=1, name="Updated Name")
# delete_user(db, user_id=1)

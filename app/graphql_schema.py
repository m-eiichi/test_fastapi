import strawberry
from db import SessionLocal  # SQLAlchemyのセッションを作成する関数をインポート
from models import Customer as CustomerModel  # SQLAlchemy の ORM モデルをインポート
from schemas import CustomerSchema  # Pydantic のスキーマをインポート
from sqlalchemy.orm import Session  # SQLAlchemyのセッション管理をインポート
from typing import List, Optional  # 型ヒントのために List, Optional をインポート
from datetime import datetime

# Pydanticモデル（CustomerSchema）をGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=CustomerSchema, all_fields=True)
class Customer:
    pass  # フィールドは Pydantic から取得されるため定義不要

@strawberry.type
class Query:
    # Query型を定義
    @strawberry.field
    def get_customers(
        self,
        customer_id: Optional[int] = None,  # customer_id をオプション引数として受け取る
        store_id: Optional[int] = None,  # 店舗ID（整数型）
        first_name: Optional[str] = None, # 顧客の名前（文字列型）
        last_name: Optional[str]= None, # 顧客の苗字（文字列型）
        email: Optional[str] = None,# 顧客のメールアドレス（文字列型）
        address_id: Optional[int]= None,  # 顧客の住所ID（整数型）
        active: Optional[int] = None,# 顧客がアクティブかどうか（真偽値）
        create_date: Optional[datetime] = None, # 顧客の作成日（文字列型、日付を文字列として格納）
        last_update: Optional[datetime] = None,# 最後の更新日（文字列型、日付を文字列として格納）
    ) -> List[Customer]:  # 戻り値は Customer オブジェクトのリスト
        db: Session = SessionLocal()  # SQLAlchemy のセッションを開始
        query = db.query(CustomerModel)  # ORM モデルをクエリ

        # 動的にWHERE句を追加（フィルタリング）
        if customer_id:
            query = query.filter(CustomerModel.customer_id == customer_id)
        if store_id:
            query = query.filter(CustomerModel.store_id == store_id)
        if first_name:
            query = query.filter(CustomerModel.first_name.like(f"%{first_name}%"))
        if last_name:
            query = query.filter(CustomerModel.last_name.like(f"%{last_name}%"))
        if email:
            query = query.filter(CustomerModel.email.like(f"%{email}%"))
        if address_id:
            query = query.filter(CustomerModel.address_id == address_id)
        if active is not None:  # `active` が None でない場合、フィルタリング
            query = query.filter(CustomerModel.active == active)
        if create_date:
            query = query.filter(CustomerModel.create_date == create_date)
        if last_update:
            query = query.filter(CustomerModel.last_update == last_update)

        customer = query.all()  # クエリを実行し、結果を取得
        db.close()  # セッションを閉じる

        # SQLAlchemy の結果を Pydantic のスキーマに変換し、さらに GraphQL の Customer 型に変換
        return [Customer.from_pydantic(CustomerSchema.from_orm(c)) for c in customer]

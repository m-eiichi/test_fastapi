from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# CustomerSchema は Pydantic を利用してバリデーションとデータ変換を行うためのモデル(Pydanticモデル)
class CustomerSchema(BaseModel):
    customer_id:  Optional[int] = None   # 顧客ID（整数型）
    store_id: Optional[int] = None  # 店舗ID（整数型）
    first_name: Optional[str] = None # 顧客の名前（文字列型）
    last_name: Optional[str]= None # 顧客の苗字（文字列型）
    email: Optional[str] = None# 顧客のメールアドレス（文字列型）
    address_id: Optional[int]= None  # 顧客の住所ID（整数型）
    active: Optional[int] = None# 顧客がアクティブかどうか（真偽値）
    create_date: Optional[datetime] = None # 顧客の作成日（文字列型、日付を文字列として格納）
    last_update: Optional[datetime] = None # 最後の更新日（文字列型、日付を文字列として格納）
    

    # Pydantic の設定
    class Config:
        # SQLAlchemy の ORM モデルから Pydantic モデルに変換する際に、属性として定義されたものを利用できるようにする設定
        from_attributes = True

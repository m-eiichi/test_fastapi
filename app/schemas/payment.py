from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# PaymentSchema は Pydantic を利用してバリデーションとデータ変換を行うためのモデル(Pydanticモデル)
class PaymentSchema(BaseModel):
    payment_id: Optional[int] = None
    customer_id: Optional[int] = None
    staff_id: Optional[int] = None
    rental_id: Optional[int] = None
    amount: Optional[int] = None
    payment_date: Optional[datetime] = None

    # Pydantic の設定
    class Config:
        # SQLAlchemy の ORM モデルから Pydantic モデルに変換する際に、属性として定義されたものを利用できるようにする設定
        from_attributes = True
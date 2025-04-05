from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from db import SessionLocal
from sql_models import Payment as PaymentModel
from schemas.payment import PaymentSchema
import strawberry

@strawberry.experimental.pydantic.type(model=PaymentSchema, all_fields=True)
class Payment:
    pass

def get_payment(
    payment_id : Optional[int] = None,
    customer_id : Optional[int] = None,
    staff_id : Optional[int] = None,
    rental_id : Optional[int] = None,
    amount : Optional[int] = None,
    payment_date : Optional[datetime] = None,

) -> List[Payment]:
    db: Session = SessionLocal()
    query = db.query(PaymentModel)

    if payment_id:
        query = query.filter(PaymentModel.payment_id == payment_id)
    if customer_id:
        query = query.filter(PaymentModel.customer_id== customer_id)
    if staff_id:
        query = query.filter(PaymentModel.staff_id == staff_id)
    if amount:
        query = query.filter(PaymentModel.amount == amount)
    if rental_id:
        query = query.filter(PaymentModel.rental_id == rental_id)
    if payment_date:
        query = query.filter(PaymentModel.payment_date == payment_date)

    Payment = query.all()
    db.close()

    return [Payment.from_pydantic(PaymentSchema.model_construct(**c.__dict__)) for c in Payment]

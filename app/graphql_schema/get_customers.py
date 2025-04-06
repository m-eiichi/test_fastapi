from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from db import SessionLocal
from models.sql_models import Customer as CustomerModel
from schemas.customer import CustomerSchema
import strawberry

@strawberry.experimental.pydantic.type(model=CustomerSchema, all_fields=True)
class Customer:
    pass

def get_customers(
    customer_id: Optional[int] = None,
    store_id: Optional[int] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[str] = None,
    address_id: Optional[int] = None,
    active: Optional[int] = None,
    create_date: Optional[datetime] = None,
    last_update: Optional[datetime] = None,
) -> List[Customer]:
    db: Session = SessionLocal()
    query = db.query(CustomerModel)

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
    if active is not None:
        query = query.filter(CustomerModel.active == active)
    if create_date:
        query = query.filter(CustomerModel.create_date == create_date)
    if last_update:
        query = query.filter(CustomerModel.last_update == last_update)

    customers = query.all()
    db.close()

    return [Customer.from_pydantic(CustomerSchema.model_construct(**c.__dict__)) for c in customers]

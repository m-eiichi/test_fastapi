import strawberry
import datetime

@strawberry.type
class Customer:
    customer_id: int
    store_id: int
    first_name: str
    last_name: str
    address_id: int
    activebool: bool
    create_date: str
    email: str
    last_update: datetime.datetime
    active: int
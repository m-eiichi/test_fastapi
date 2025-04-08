import strawberry
import datetime

@strawberry.type
class Payment:
    payment_id: int
    customer_id: int
    staff_id: int
    rental_id: int
    amount: str
    payment_date: datetime.datetime
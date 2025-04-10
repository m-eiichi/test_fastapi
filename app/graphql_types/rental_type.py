import strawberry
import datetime

@strawberry.type
class Rental:
    rental_id: int
    rental_date: datetime.datetime
    inventory_id: int
    customer_id: int
    staff_id: int
    last_update: datetime.datetime
    return_date: datetime.datetime
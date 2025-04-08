import strawberry
import datetime

@strawberry.type
class Store:
    store_id: int
    manager_staff_id: int
    address_id: int
    last_update: datetime.datetime
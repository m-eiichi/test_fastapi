import strawberry
import datetime

@strawberry.type
class Inventory:
    inventory_id: int
    film_id: int
    store_id: int
    last_update: datetime.datetime
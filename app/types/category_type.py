import strawberry
import datetime

@strawberry.type
class Category:
    category_id: int
    name: str
    last_update: datetime.datetime
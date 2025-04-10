import strawberry
import datetime

@strawberry.type
class Actor:
    actor_id: int
    first_name: str
    last_name: str
    last_update: datetime.datetime
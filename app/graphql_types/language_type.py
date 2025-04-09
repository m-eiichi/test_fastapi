import strawberry
import datetime

@strawberry.type
class Language:
    language_id: int
    name: str
    last_update: datetime.datetime
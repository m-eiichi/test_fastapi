import strawberry
import datetime

@strawberry.type
class Country:
    country_id: int
    country: str
    last_update: datetime.datetime
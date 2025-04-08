import strawberry
import datetime

@strawberry.type
class City:
    city_id: int
    city: str
    country_id: int
    last_update: datetime.datetime
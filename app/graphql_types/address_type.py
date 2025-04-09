import strawberry
import datetime

@strawberry.type
class Address:
    address_id: int
    address: str
    district: str
    city_id: int
    phone: str
    last_update: datetime.datetime
    address2: str
    postal_code: str
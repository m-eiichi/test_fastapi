import strawberry
import datetime

@strawberry.type
class Staff:
    staff_id: int
    first_name: str
    last_name: str
    address_id: int
    store_id: int
    active: bool
    username: str
    last_update: datetime.datetime
    email: str
    password: str
    picture: str
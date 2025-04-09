import strawberry
import datetime

@strawberry.type
class FilmCategory:
    film_id: int
    category_id: int
    last_update: datetime.datetime
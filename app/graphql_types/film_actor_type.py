import strawberry
import datetime

@strawberry.type
class FilmActor:
    actor_id: int
    film_id: int
    last_update: datetime.datetime
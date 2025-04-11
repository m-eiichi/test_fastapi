import strawberry
import datetime

@strawberry.type
class Film:
    film_id: int
    title: str
    language_id: int
    rental_duration: int
    rental_rate: str
    replacement_cost: str
    last_update: datetime.datetime
    fulltext: str
    description: str
    release_year: int
    length: int
    rating: str
    special_features: str
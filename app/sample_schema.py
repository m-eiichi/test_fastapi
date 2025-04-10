import strawberry
from typing import List
import datetime
import asyncpg
import os
from dotenv import load_dotenv
from graphql_types.film_category_type import FilmCategory
from graphql_types.staff_type import Staff
from graphql_types.city_type import City
from graphql_types.country_type import Country
from graphql_types.rental_type import Rental
from graphql_types.customer_type import Customer
from graphql_types.actor_type import Actor
from graphql_types.inventory_type import Inventory
from graphql_types.address_type import Address
from graphql_types.film_actor_type import FilmActor
from graphql_types.store_type import Store
from graphql_types.language_type import Language
from graphql_types.payment_type import Payment
from graphql_types.category_type import Category


load_dotenv()

@strawberry.type
class Query:
    @strawberry.field
    async def filmcategorys(self) -> List[FilmCategory]:
        return await fetch_filmcategorys()  # asyncpgでデータを取得


async def fetch_filmcategorys():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM film_category')
    await conn.close()
    return [FilmCategory(category_id=row['category_id'],film_id=row['film_id'],last_update=row['last_update']) for row in rows]
   


schema = strawberry.Schema(query=Query)
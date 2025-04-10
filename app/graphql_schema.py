import strawberry
from typing import List
import datetime
import asyncpg
import os
from dotenv import load_dotenv
from graphql_types.actor_type import Actor
from graphql_types.address_type import Address
from graphql_types.store_type import Store
from graphql_types.city_type import City
from graphql_types.inventory_type import Inventory
from graphql_types.film_category_type import FilmCategory
from graphql_types.staff_type import Staff
from graphql_types.customer_type import Customer
from graphql_types.payment_type import Payment
from graphql_types.rental_type import Rental
from graphql_types.language_type import Language
from graphql_types.country_type import Country
from graphql_types.film_actor_type import FilmActor
from graphql_types.category_type import Category


load_dotenv()



async def fetch_actors():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM actor')
    await conn.close()
    return [Actor(**row) for row in rows]


async def fetch_addresss():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM address')
    await conn.close()
    return [Address(**row) for row in rows]


async def fetch_stores():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM store')
    await conn.close()
    return [Store(**row) for row in rows]


async def fetch_citys():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM city')
    await conn.close()
    return [City(**row) for row in rows]


async def fetch_inventorys():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM inventory')
    await conn.close()
    return [Inventory(**row) for row in rows]


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
    return [FilmCategory(**row) for row in rows]


async def fetch_staffs():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM staff')
    await conn.close()
    return [Staff(**row) for row in rows]


async def fetch_customers():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM customer')
    await conn.close()
    return [Customer(**row) for row in rows]


async def fetch_payments():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM payment')
    await conn.close()
    return [Payment(**row) for row in rows]


async def fetch_rentals():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM rental')
    await conn.close()
    return [Rental(**row) for row in rows]


async def fetch_languages():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM language')
    await conn.close()
    return [Language(**row) for row in rows]


async def fetch_countrys():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM country')
    await conn.close()
    return [Country(**row) for row in rows]


async def fetch_filmactors():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM film_actor')
    await conn.close()
    return [FilmActor(**row) for row in rows]


async def fetch_categorys():
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    rows = await conn.fetch('SELECT * FROM category')
    await conn.close()
    return [Category(**row) for row in rows]

@strawberry.type
class Query:
    @strawberry.field
    async def actors(self) -> List[Actor]:
        return await fetch_actors()  # asyncpgでデータを取得
    @strawberry.field
    async def addresss(self) -> List[Address]:
        return await fetch_addresss()  # asyncpgでデータを取得
    @strawberry.field
    async def stores(self) -> List[Store]:
        return await fetch_stores()  # asyncpgでデータを取得
    @strawberry.field
    async def citys(self) -> List[City]:
        return await fetch_citys()  # asyncpgでデータを取得
    @strawberry.field
    async def inventorys(self) -> List[Inventory]:
        return await fetch_inventorys()  # asyncpgでデータを取得
    @strawberry.field
    async def filmcategorys(self) -> List[FilmCategory]:
        return await fetch_filmcategorys()  # asyncpgでデータを取得
    @strawberry.field
    async def staffs(self) -> List[Staff]:
        return await fetch_staffs()  # asyncpgでデータを取得
    @strawberry.field
    async def customers(self) -> List[Customer]:
        return await fetch_customers()  # asyncpgでデータを取得
    @strawberry.field
    async def payments(self) -> List[Payment]:
        return await fetch_payments()  # asyncpgでデータを取得
    @strawberry.field
    async def rentals(self) -> List[Rental]:
        return await fetch_rentals()  # asyncpgでデータを取得
    @strawberry.field
    async def languages(self) -> List[Language]:
        return await fetch_languages()  # asyncpgでデータを取得
    @strawberry.field
    async def countrys(self) -> List[Country]:
        return await fetch_countrys()  # asyncpgでデータを取得
    @strawberry.field
    async def filmactors(self) -> List[FilmActor]:
        return await fetch_filmactors()  # asyncpgでデータを取得
    @strawberry.field
    async def categorys(self) -> List[Category]:
        return await fetch_categorys()  # asyncpgでデータを取得

schema = strawberry.Schema(query=Query)
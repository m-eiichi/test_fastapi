import strawberry
from typing import List, Optional
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


async def fetch_actors(actor_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM actor'
    conditions = []
    values = []
    if actor_id is not None:
        conditions.append(f"actor_id = ${len(values) + 1}")
        values.append(actor_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Actor(**dict(row)) for row in rows]

async def fetch_addresss(address_id: Optional[int] = None, city_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM address'
    conditions = []
    values = []
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if city_id is not None:
        conditions.append(f"city_id = ${len(values) + 1}")
        values.append(city_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Address(**dict(row)) for row in rows]

async def fetch_stores(store_id: Optional[int] = None, manager_staff_id: Optional[int] = None, address_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM store'
    conditions = []
    values = []
    if store_id is not None:
        conditions.append(f"store_id = ${len(values) + 1}")
        values.append(store_id)
    if manager_staff_id is not None:
        conditions.append(f"manager_staff_id = ${len(values) + 1}")
        values.append(manager_staff_id)
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Store(**dict(row)) for row in rows]

async def fetch_citys(city_id: Optional[int] = None, country_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM city'
    conditions = []
    values = []
    if city_id is not None:
        conditions.append(f"city_id = ${len(values) + 1}")
        values.append(city_id)
    if country_id is not None:
        conditions.append(f"country_id = ${len(values) + 1}")
        values.append(country_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [City(**dict(row)) for row in rows]

async def fetch_inventorys(inventory_id: Optional[int] = None, film_id: Optional[int] = None, store_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM inventory'
    conditions = []
    values = []
    if inventory_id is not None:
        conditions.append(f"inventory_id = ${len(values) + 1}")
        values.append(inventory_id)
    if film_id is not None:
        conditions.append(f"film_id = ${len(values) + 1}")
        values.append(film_id)
    if store_id is not None:
        conditions.append(f"store_id = ${len(values) + 1}")
        values.append(store_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Inventory(**dict(row)) for row in rows]

async def fetch_filmcategorys(film_id: Optional[int] = None, category_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM film_category'
    conditions = []
    values = []
    if film_id is not None:
        conditions.append(f"film_id = ${len(values) + 1}")
        values.append(film_id)
    if category_id is not None:
        conditions.append(f"category_id = ${len(values) + 1}")
        values.append(category_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [FilmCategory(**dict(row)) for row in rows]

async def fetch_staffs(staff_id: Optional[int] = None, address_id: Optional[int] = None, store_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM staff'
    conditions = []
    values = []
    if staff_id is not None:
        conditions.append(f"staff_id = ${len(values) + 1}")
        values.append(staff_id)
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if store_id is not None:
        conditions.append(f"store_id = ${len(values) + 1}")
        values.append(store_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Staff(**dict(row)) for row in rows]

async def fetch_customers(customer_id: Optional[int] = None, store_id: Optional[int] = None, address_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM customer'
    conditions = []
    values = []
    if customer_id is not None:
        conditions.append(f"customer_id = ${len(values) + 1}")
        values.append(customer_id)
    if store_id is not None:
        conditions.append(f"store_id = ${len(values) + 1}")
        values.append(store_id)
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Customer(**dict(row)) for row in rows]

async def fetch_payments(payment_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, rental_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM payment'
    conditions = []
    values = []
    if payment_id is not None:
        conditions.append(f"payment_id = ${len(values) + 1}")
        values.append(payment_id)
    if customer_id is not None:
        conditions.append(f"customer_id = ${len(values) + 1}")
        values.append(customer_id)
    if staff_id is not None:
        conditions.append(f"staff_id = ${len(values) + 1}")
        values.append(staff_id)
    if rental_id is not None:
        conditions.append(f"rental_id = ${len(values) + 1}")
        values.append(rental_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Payment(**dict(row)) for row in rows]

async def fetch_rentals(rental_id: Optional[int] = None, inventory_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM rental'
    conditions = []
    values = []
    if rental_id is not None:
        conditions.append(f"rental_id = ${len(values) + 1}")
        values.append(rental_id)
    if inventory_id is not None:
        conditions.append(f"inventory_id = ${len(values) + 1}")
        values.append(inventory_id)
    if customer_id is not None:
        conditions.append(f"customer_id = ${len(values) + 1}")
        values.append(customer_id)
    if staff_id is not None:
        conditions.append(f"staff_id = ${len(values) + 1}")
        values.append(staff_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Rental(**dict(row)) for row in rows]

async def fetch_languages(language_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM language'
    conditions = []
    values = []
    if language_id is not None:
        conditions.append(f"language_id = ${len(values) + 1}")
        values.append(language_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Language(**dict(row)) for row in rows]

async def fetch_countrys(country_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM country'
    conditions = []
    values = []
    if country_id is not None:
        conditions.append(f"country_id = ${len(values) + 1}")
        values.append(country_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Country(**dict(row)) for row in rows]

async def fetch_filmactors(actor_id: Optional[int] = None, film_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM film_actor'
    conditions = []
    values = []
    if actor_id is not None:
        conditions.append(f"actor_id = ${len(values) + 1}")
        values.append(actor_id)
    if film_id is not None:
        conditions.append(f"film_id = ${len(values) + 1}")
        values.append(film_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [FilmActor(**dict(row)) for row in rows]

async def fetch_categorys(category_id: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM category'
    conditions = []
    values = []
    if category_id is not None:
        conditions.append(f"category_id = ${len(values) + 1}")
        values.append(category_id)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Category(**dict(row)) for row in rows]

@strawberry.type
class Query:

    @strawberry.field
    async def actors(self, actor_id: Optional[int] = None) -> List[Actor]:
        return await fetch_actors(actor_id=actor_id)

    @strawberry.field
    async def addresss(self, address_id: Optional[int] = None, city_id: Optional[int] = None) -> List[Address]:
        return await fetch_addresss(address_id=address_id, city_id=city_id)

    @strawberry.field
    async def stores(self, store_id: Optional[int] = None, manager_staff_id: Optional[int] = None, address_id: Optional[int] = None) -> List[Store]:
        return await fetch_stores(store_id=store_id, manager_staff_id=manager_staff_id, address_id=address_id)

    @strawberry.field
    async def citys(self, city_id: Optional[int] = None, country_id: Optional[int] = None) -> List[City]:
        return await fetch_citys(city_id=city_id, country_id=country_id)

    @strawberry.field
    async def inventorys(self, inventory_id: Optional[int] = None, film_id: Optional[int] = None, store_id: Optional[int] = None) -> List[Inventory]:
        return await fetch_inventorys(inventory_id=inventory_id, film_id=film_id, store_id=store_id)

    @strawberry.field
    async def filmcategorys(self, film_id: Optional[int] = None, category_id: Optional[int] = None) -> List[FilmCategory]:
        return await fetch_filmcategorys(film_id=film_id, category_id=category_id)

    @strawberry.field
    async def staffs(self, staff_id: Optional[int] = None, address_id: Optional[int] = None, store_id: Optional[int] = None) -> List[Staff]:
        return await fetch_staffs(staff_id=staff_id, address_id=address_id, store_id=store_id)

    @strawberry.field
    async def customers(self, customer_id: Optional[int] = None, store_id: Optional[int] = None, address_id: Optional[int] = None) -> List[Customer]:
        return await fetch_customers(customer_id=customer_id, store_id=store_id, address_id=address_id)

    @strawberry.field
    async def payments(self, payment_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, rental_id: Optional[int] = None) -> List[Payment]:
        return await fetch_payments(payment_id=payment_id, customer_id=customer_id, staff_id=staff_id, rental_id=rental_id)

    @strawberry.field
    async def rentals(self, rental_id: Optional[int] = None, inventory_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None) -> List[Rental]:
        return await fetch_rentals(rental_id=rental_id, inventory_id=inventory_id, customer_id=customer_id, staff_id=staff_id)

    @strawberry.field
    async def languages(self, language_id: Optional[int] = None) -> List[Language]:
        return await fetch_languages(language_id=language_id)

    @strawberry.field
    async def countrys(self, country_id: Optional[int] = None) -> List[Country]:
        return await fetch_countrys(country_id=country_id)

    @strawberry.field
    async def filmactors(self, actor_id: Optional[int] = None, film_id: Optional[int] = None) -> List[FilmActor]:
        return await fetch_filmactors(actor_id=actor_id, film_id=film_id)

    @strawberry.field
    async def categorys(self, category_id: Optional[int] = None) -> List[Category]:
        return await fetch_categorys(category_id=category_id)

schema = strawberry.Schema(query=Query)
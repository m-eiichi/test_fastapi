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
from graphql_types.film_type import Film
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


async def fetch_actors(actor_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, last_update: Optional[int] = None):
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
    if first_name is not None:
        conditions.append(f"first_name = ${len(values) + 1}")
        values.append(first_name)
    if last_name is not None:
        conditions.append(f"last_name = ${len(values) + 1}")
        values.append(last_name)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Actor(**dict(row)) for row in rows]

async def fetch_addresss(address_id: Optional[int] = None, address: Optional[int] = None, district: Optional[int] = None, city_id: Optional[int] = None, phone: Optional[int] = None, last_update: Optional[int] = None, address2: Optional[int] = None, postal_code: Optional[int] = None):
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
    if address is not None:
        conditions.append(f"address = ${len(values) + 1}")
        values.append(address)
    if district is not None:
        conditions.append(f"district = ${len(values) + 1}")
        values.append(district)
    if city_id is not None:
        conditions.append(f"city_id = ${len(values) + 1}")
        values.append(city_id)
    if phone is not None:
        conditions.append(f"phone = ${len(values) + 1}")
        values.append(phone)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if address2 is not None:
        conditions.append(f"address2 = ${len(values) + 1}")
        values.append(address2)
    if postal_code is not None:
        conditions.append(f"postal_code = ${len(values) + 1}")
        values.append(postal_code)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Address(**dict(row)) for row in rows]

async def fetch_stores(store_id: Optional[int] = None, manager_staff_id: Optional[int] = None, address_id: Optional[int] = None, last_update: Optional[int] = None):
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
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Store(**dict(row)) for row in rows]

async def fetch_citys(city_id: Optional[int] = None, city: Optional[int] = None, country_id: Optional[int] = None, last_update: Optional[int] = None):
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
    if city is not None:
        conditions.append(f"city = ${len(values) + 1}")
        values.append(city)
    if country_id is not None:
        conditions.append(f"country_id = ${len(values) + 1}")
        values.append(country_id)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [City(**dict(row)) for row in rows]

async def fetch_inventorys(inventory_id: Optional[int] = None, film_id: Optional[int] = None, store_id: Optional[int] = None, last_update: Optional[int] = None):
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
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Inventory(**dict(row)) for row in rows]

async def fetch_films(film_id: Optional[int] = None, title: Optional[int] = None, language_id: Optional[int] = None, rental_duration: Optional[int] = None, rental_rate: Optional[int] = None, replacement_cost: Optional[int] = None, last_update: Optional[int] = None, fulltext: Optional[int] = None, description: Optional[int] = None, release_year: Optional[int] = None, length: Optional[int] = None, rating: Optional[int] = None, special_features: Optional[int] = None):
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        ssl=True
    )
    query = 'SELECT * FROM film'
    conditions = []
    values = []
    if film_id is not None:
        conditions.append(f"film_id = ${len(values) + 1}")
        values.append(film_id)
    if title is not None:
        conditions.append(f"title = ${len(values) + 1}")
        values.append(title)
    if language_id is not None:
        conditions.append(f"language_id = ${len(values) + 1}")
        values.append(language_id)
    if rental_duration is not None:
        conditions.append(f"rental_duration = ${len(values) + 1}")
        values.append(rental_duration)
    if rental_rate is not None:
        conditions.append(f"rental_rate = ${len(values) + 1}")
        values.append(rental_rate)
    if replacement_cost is not None:
        conditions.append(f"replacement_cost = ${len(values) + 1}")
        values.append(replacement_cost)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if fulltext is not None:
        conditions.append(f"fulltext = ${len(values) + 1}")
        values.append(fulltext)
    if description is not None:
        conditions.append(f"description = ${len(values) + 1}")
        values.append(description)
    if release_year is not None:
        conditions.append(f"release_year = ${len(values) + 1}")
        values.append(release_year)
    if length is not None:
        conditions.append(f"length = ${len(values) + 1}")
        values.append(length)
    if rating is not None:
        conditions.append(f"rating = ${len(values) + 1}")
        values.append(rating)
    if special_features is not None:
        conditions.append(f"special_features = ${len(values) + 1}")
        values.append(special_features)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Film(**dict(row)) for row in rows]

async def fetch_filmcategorys(film_id: Optional[int] = None, category_id: Optional[int] = None, last_update: Optional[int] = None):
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
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [FilmCategory(**dict(row)) for row in rows]

async def fetch_staffs(staff_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, address_id: Optional[int] = None, store_id: Optional[int] = None, active: Optional[int] = None, username: Optional[int] = None, last_update: Optional[int] = None, email: Optional[int] = None, password: Optional[int] = None, picture: Optional[int] = None):
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
    if first_name is not None:
        conditions.append(f"first_name = ${len(values) + 1}")
        values.append(first_name)
    if last_name is not None:
        conditions.append(f"last_name = ${len(values) + 1}")
        values.append(last_name)
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if store_id is not None:
        conditions.append(f"store_id = ${len(values) + 1}")
        values.append(store_id)
    if active is not None:
        conditions.append(f"active = ${len(values) + 1}")
        values.append(active)
    if username is not None:
        conditions.append(f"username = ${len(values) + 1}")
        values.append(username)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if email is not None:
        conditions.append(f"email = ${len(values) + 1}")
        values.append(email)
    if password is not None:
        conditions.append(f"password = ${len(values) + 1}")
        values.append(password)
    if picture is not None:
        conditions.append(f"picture = ${len(values) + 1}")
        values.append(picture)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Staff(**dict(row)) for row in rows]

async def fetch_customers(customer_id: Optional[int] = None, store_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, address_id: Optional[int] = None, activebool: Optional[int] = None, create_date: Optional[int] = None, email: Optional[int] = None, last_update: Optional[int] = None, active: Optional[int] = None):
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
    if first_name is not None:
        conditions.append(f"first_name = ${len(values) + 1}")
        values.append(first_name)
    if last_name is not None:
        conditions.append(f"last_name = ${len(values) + 1}")
        values.append(last_name)
    if address_id is not None:
        conditions.append(f"address_id = ${len(values) + 1}")
        values.append(address_id)
    if activebool is not None:
        conditions.append(f"activebool = ${len(values) + 1}")
        values.append(activebool)
    if create_date is not None:
        conditions.append(f"create_date = ${len(values) + 1}")
        values.append(create_date)
    if email is not None:
        conditions.append(f"email = ${len(values) + 1}")
        values.append(email)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if active is not None:
        conditions.append(f"active = ${len(values) + 1}")
        values.append(active)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Customer(**dict(row)) for row in rows]

async def fetch_payments(payment_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, rental_id: Optional[int] = None, amount: Optional[int] = None, payment_date: Optional[int] = None):
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
    if amount is not None:
        conditions.append(f"amount = ${len(values) + 1}")
        values.append(amount)
    if payment_date is not None:
        conditions.append(f"payment_date = ${len(values) + 1}")
        values.append(payment_date)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Payment(**dict(row)) for row in rows]

async def fetch_rentals(rental_id: Optional[int] = None, rental_date: Optional[int] = None, inventory_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, last_update: Optional[int] = None, return_date: Optional[int] = None):
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
    if rental_date is not None:
        conditions.append(f"rental_date = ${len(values) + 1}")
        values.append(rental_date)
    if inventory_id is not None:
        conditions.append(f"inventory_id = ${len(values) + 1}")
        values.append(inventory_id)
    if customer_id is not None:
        conditions.append(f"customer_id = ${len(values) + 1}")
        values.append(customer_id)
    if staff_id is not None:
        conditions.append(f"staff_id = ${len(values) + 1}")
        values.append(staff_id)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if return_date is not None:
        conditions.append(f"return_date = ${len(values) + 1}")
        values.append(return_date)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Rental(**dict(row)) for row in rows]

async def fetch_languages(language_id: Optional[int] = None, name: Optional[int] = None, last_update: Optional[int] = None):
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
    if name is not None:
        conditions.append(f"name = ${len(values) + 1}")
        values.append(name)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Language(**dict(row)) for row in rows]

async def fetch_countrys(country_id: Optional[int] = None, country: Optional[int] = None, last_update: Optional[int] = None):
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
    if country is not None:
        conditions.append(f"country = ${len(values) + 1}")
        values.append(country)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Country(**dict(row)) for row in rows]

async def fetch_filmactors(actor_id: Optional[int] = None, film_id: Optional[int] = None, last_update: Optional[int] = None):
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
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [FilmActor(**dict(row)) for row in rows]

async def fetch_categorys(category_id: Optional[int] = None, name: Optional[int] = None, last_update: Optional[int] = None):
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
    if name is not None:
        conditions.append(f"name = ${len(values) + 1}")
        values.append(name)
    if last_update is not None:
        conditions.append(f"last_update = ${len(values) + 1}")
        values.append(last_update)
    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)
    rows = await conn.fetch(query, *values)
    await conn.close()
    return [Category(**dict(row)) for row in rows]

@strawberry.type
class Query:

    @strawberry.field
    async def actors(self, actor_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, last_update: Optional[int] = None) -> List[Actor]:
        return await fetch_actors(actor_id=actor_id, first_name=first_name, last_name=last_name, last_update=last_update)

    @strawberry.field
    async def addresss(self, address_id: Optional[int] = None, address: Optional[int] = None, district: Optional[int] = None, city_id: Optional[int] = None, phone: Optional[int] = None, last_update: Optional[int] = None, address2: Optional[int] = None, postal_code: Optional[int] = None) -> List[Address]:
        return await fetch_addresss(address_id=address_id, address=address, district=district, city_id=city_id, phone=phone, last_update=last_update, address2=address2, postal_code=postal_code)

    @strawberry.field
    async def stores(self, store_id: Optional[int] = None, manager_staff_id: Optional[int] = None, address_id: Optional[int] = None, last_update: Optional[int] = None) -> List[Store]:
        return await fetch_stores(store_id=store_id, manager_staff_id=manager_staff_id, address_id=address_id, last_update=last_update)

    @strawberry.field
    async def citys(self, city_id: Optional[int] = None, city: Optional[int] = None, country_id: Optional[int] = None, last_update: Optional[int] = None) -> List[City]:
        return await fetch_citys(city_id=city_id, city=city, country_id=country_id, last_update=last_update)

    @strawberry.field
    async def inventorys(self, inventory_id: Optional[int] = None, film_id: Optional[int] = None, store_id: Optional[int] = None, last_update: Optional[int] = None) -> List[Inventory]:
        return await fetch_inventorys(inventory_id=inventory_id, film_id=film_id, store_id=store_id, last_update=last_update)

    @strawberry.field
    async def films(self, film_id: Optional[int] = None, title: Optional[int] = None, language_id: Optional[int] = None, rental_duration: Optional[int] = None, rental_rate: Optional[int] = None, replacement_cost: Optional[int] = None, last_update: Optional[int] = None, fulltext: Optional[int] = None, description: Optional[int] = None, release_year: Optional[int] = None, length: Optional[int] = None, rating: Optional[int] = None, special_features: Optional[int] = None) -> List[Film]:
        return await fetch_films(film_id=film_id, title=title, language_id=language_id, rental_duration=rental_duration, rental_rate=rental_rate, replacement_cost=replacement_cost, last_update=last_update, fulltext=fulltext, description=description, release_year=release_year, length=length, rating=rating, special_features=special_features)

    @strawberry.field
    async def filmcategorys(self, film_id: Optional[int] = None, category_id: Optional[int] = None, last_update: Optional[int] = None) -> List[FilmCategory]:
        return await fetch_filmcategorys(film_id=film_id, category_id=category_id, last_update=last_update)

    @strawberry.field
    async def staffs(self, staff_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, address_id: Optional[int] = None, store_id: Optional[int] = None, active: Optional[int] = None, username: Optional[int] = None, last_update: Optional[int] = None, email: Optional[int] = None, password: Optional[int] = None, picture: Optional[int] = None) -> List[Staff]:
        return await fetch_staffs(staff_id=staff_id, first_name=first_name, last_name=last_name, address_id=address_id, store_id=store_id, active=active, username=username, last_update=last_update, email=email, password=password, picture=picture)

    @strawberry.field
    async def customers(self, customer_id: Optional[int] = None, store_id: Optional[int] = None, first_name: Optional[int] = None, last_name: Optional[int] = None, address_id: Optional[int] = None, activebool: Optional[int] = None, create_date: Optional[int] = None, email: Optional[int] = None, last_update: Optional[int] = None, active: Optional[int] = None) -> List[Customer]:
        return await fetch_customers(customer_id=customer_id, store_id=store_id, first_name=first_name, last_name=last_name, address_id=address_id, activebool=activebool, create_date=create_date, email=email, last_update=last_update, active=active)

    @strawberry.field
    async def payments(self, payment_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, rental_id: Optional[int] = None, amount: Optional[int] = None, payment_date: Optional[int] = None) -> List[Payment]:
        return await fetch_payments(payment_id=payment_id, customer_id=customer_id, staff_id=staff_id, rental_id=rental_id, amount=amount, payment_date=payment_date)

    @strawberry.field
    async def rentals(self, rental_id: Optional[int] = None, rental_date: Optional[int] = None, inventory_id: Optional[int] = None, customer_id: Optional[int] = None, staff_id: Optional[int] = None, last_update: Optional[int] = None, return_date: Optional[int] = None) -> List[Rental]:
        return await fetch_rentals(rental_id=rental_id, rental_date=rental_date, inventory_id=inventory_id, customer_id=customer_id, staff_id=staff_id, last_update=last_update, return_date=return_date)

    @strawberry.field
    async def languages(self, language_id: Optional[int] = None, name: Optional[int] = None, last_update: Optional[int] = None) -> List[Language]:
        return await fetch_languages(language_id=language_id, name=name, last_update=last_update)

    @strawberry.field
    async def countrys(self, country_id: Optional[int] = None, country: Optional[int] = None, last_update: Optional[int] = None) -> List[Country]:
        return await fetch_countrys(country_id=country_id, country=country, last_update=last_update)

    @strawberry.field
    async def filmactors(self, actor_id: Optional[int] = None, film_id: Optional[int] = None, last_update: Optional[int] = None) -> List[FilmActor]:
        return await fetch_filmactors(actor_id=actor_id, film_id=film_id, last_update=last_update)

    @strawberry.field
    async def categorys(self, category_id: Optional[int] = None, name: Optional[int] = None, last_update: Optional[int] = None) -> List[Category]:
        return await fetch_categorys(category_id=category_id, name=name, last_update=last_update)

schema = strawberry.Schema(query=Query)
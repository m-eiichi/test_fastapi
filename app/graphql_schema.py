import strawberry
from typing import List
import datetime
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

@strawberry.type
class Query:
    @strawberry.field
    def all_filmcategorys(self) -> List[FilmCategory]:
        return [
            FilmCategory()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_staffs(self) -> List[Staff]:
        return [
            Staff()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_citys(self) -> List[City]:
        return [
            City()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_countrys(self) -> List[Country]:
        return [
            Country()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_rentals(self) -> List[Rental]:
        return [
            Rental()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_customers(self) -> List[Customer]:
        return [
            Customer()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_actors(self) -> List[Actor]:
        # return [
        #     Actor()  # TODO: フィールドに合わせて初期値を設定
        # ]
        return []
    @strawberry.field
    def all_inventorys(self) -> List[Inventory]:
        return [
            Inventory()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_addresss(self) -> List[Address]:
        return [
            Address()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_filmactors(self) -> List[FilmActor]:
        return [
            FilmActor()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_stores(self) -> List[Store]:
        return [
            Store()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_languages(self) -> List[Language]:
        return [
            Language()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_payments(self) -> List[Payment]:
        return [
            Payment()  # TODO: フィールドに合わせて初期値を設定
        ]
    @strawberry.field
    def all_categorys(self) -> List[Category]:
        return [
            Category()  # TODO: フィールドに合わせて初期値を設定
        ]

schema = strawberry.Schema(query=Query)
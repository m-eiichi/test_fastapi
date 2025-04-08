import strawberry
from typing import List
import datetime
from types.actor_type import Actor
from types.address_type import Address
from types.store_type import Store
from types.city_type import City
from types.inventory_type import Inventory
from types.staff_type import Staff
from types.customer_type import Customer
from types.payment_type import Payment
from types.rental_type import Rental
from types.language_type import Language
from types.filmcategory_type import Filmcategory
from types.country_type import Country
from types.category_type import Category
from types.filmactor_type import Filmactor

@strawberry.type
class Query:
    @strawberry.field
    def all_actors(self) -> List[Actor]:
        return []  # TODO: 実装
    @strawberry.field
    def all_addresss(self) -> List[Address]:
        return []  # TODO: 実装
    @strawberry.field
    def all_stores(self) -> List[Store]:
        return []  # TODO: 実装
    @strawberry.field
    def all_citys(self) -> List[City]:
        return []  # TODO: 実装
    @strawberry.field
    def all_inventorys(self) -> List[Inventory]:
        return []  # TODO: 実装
    @strawberry.field
    def all_staffs(self) -> List[Staff]:
        return []  # TODO: 実装
    @strawberry.field
    def all_customers(self) -> List[Customer]:
        return []  # TODO: 実装
    @strawberry.field
    def all_payments(self) -> List[Payment]:
        return []  # TODO: 実装
    @strawberry.field
    def all_rentals(self) -> List[Rental]:
        return []  # TODO: 実装
    @strawberry.field
    def all_languages(self) -> List[Language]:
        return []  # TODO: 実装
    @strawberry.field
    def all_filmcategorys(self) -> List[Filmcategory]:
        return []  # TODO: 実装
    @strawberry.field
    def all_countrys(self) -> List[Country]:
        return []  # TODO: 実装
    @strawberry.field
    def all_categorys(self) -> List[Category]:
        return []  # TODO: 実装
    @strawberry.field
    def all_filmactors(self) -> List[Filmactor]:
        return []  # TODO: 実装

schema = strawberry.Schema(query=Query)
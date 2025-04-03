import strawberry
from graphql_schema.get_customers import get_customers
from graphql_schema.get_payment import get_payment
from schemas.customer import CustomerSchema
from schemas.payment import PaymentSchema

# Pydanticモデル（CustomerSchema）をGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=CustomerSchema, all_fields=True)
class Customer:
    pass

# Pydanticモデル（PaymentSchema）をGraphQLの型に変換
@strawberry.experimental.pydantic.type(model=PaymentSchema, all_fields=True)
class Payment:
    pass

@strawberry.type
class Query:
    get_customers = strawberry.field(resolver=get_customers)
    get_payment = strawberry.field(resolver=get_payment)

schema = strawberry.Schema(query=Query)

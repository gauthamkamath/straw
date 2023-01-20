import strawberry

@strawberry.type
class Query:

    foo: str

schema = strawberry.Schema(Query)

# straw/schemas/player.py
import strawberry
from straw.schemas.pagination import Connection

@strawberry.type
class Player:
    id: strawberry.ID
    name: str

@strawberry.type
class PlayerQuery:
    @strawberry.field
    def players(self) -> Connection[Player]:
        pass

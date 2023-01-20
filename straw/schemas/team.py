# straw/schemas/team.py
import strawberry
from typing import TYPE_CHECKING, Annotated
from straw.schemas.pagination import Connection

if TYPE_CHECKING:
    from straw.schemas.player import Player

@strawberry.type
class Team:
    id: strawberry.ID
    name: str

    @strawberry.field
    def players(self, first: int = 2, after: str | None = None) -> Connection[Annotated["Player", strawberry.lazy("straw.schemas.player")]]:
        pass

@strawberry.type
class TeamQuery:
    @strawberry.field
    def teams(self) -> Connection[Team]:
        pass

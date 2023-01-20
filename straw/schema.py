# straw/schema.py
import strawberry
from straw.schemas import team
from straw.schemas import player


@strawberry.type
class Query(
    team.TeamQuery,
    player.PlayerQuery,
):
    pass

schema = strawberry.Schema(query=Query)

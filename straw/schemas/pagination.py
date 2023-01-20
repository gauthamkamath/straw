# straw/schemas/pagination.py
# Same as in documentation
from typing import List, Generic, TypeVar, Optional
import strawberry
from strawberry import UNSET

GenericType = TypeVar("GenericType")

@strawberry.type
class Connection(Generic[GenericType]):
    page_info: "PageInfo"
    edges: List["Edge[GenericType]"]

@strawberry.type
class PageInfo:
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str]
    end_cursor: Optional[str]

@strawberry.type
class Edge(Generic[GenericType]):
    node: GenericType
    cursor: str

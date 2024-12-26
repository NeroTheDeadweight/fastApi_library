from pydantic import BaseModel
from datetime import date

class BookBase(BaseModel):
    title: str
    description: str | None = None
    author_id: int
    available_copies: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    author_id: int | None = None
    available_copies: int | None = None

class BookRead(BookBase):
    id: int

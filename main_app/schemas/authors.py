from pydantic import BaseModel
from datetime import date

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date | None = None

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    date_of_birth: date | None = None

class AuthorRead(AuthorBase):
    id: int


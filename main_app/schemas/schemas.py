from pydantic import BaseModel
from datetime import date


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date | None = None

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None

class AuthorRead(AuthorBase):
    id: int




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

    class Config:
        orm_mode = True


from pydantic import BaseModel
from datetime import date

class BorrowBase(BaseModel):
    book_id: int
    reader_name: str
    borrow_date: date

class BorrowCreate(BorrowBase):
    pass

class BorrowReturn(BaseModel):
    return_date: date

class BorrowRead(BorrowBase):
    id: int
    return_date: date | None = None

    class Config:
        orm_mode = True
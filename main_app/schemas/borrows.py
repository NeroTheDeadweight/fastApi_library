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

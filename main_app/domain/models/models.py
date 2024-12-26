from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    available_copies = Column(Integer, default=0)

    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)

    books = relationship("Book", back_populates="author")

class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reader_name = Column(String, nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship("Book", back_populates="borrows")
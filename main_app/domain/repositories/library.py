from sqlalchemy import create_engine
from main_app.domain.models.models import Author, Book, Borrow
from sqlalchemy.orm import Session

sqlite_database = "sqlite:///library.db"
engine = create_engine(sqlite_database, echo=True)

class Library_repository:
    async def add_book(self, book: Book):
        with Session(autoflush=False, bind=engine) as session:
            added = book
            session.add(added)
            session.commit()

    async def add_author(self, author: Author):
        with Session(autoflush=False, bind=engine) as session:
            added = author
            session.add(added)
            session.commit()
    async def add_issue(self, issue: Borrow):
        with Session(autoflush=False, bind=engine) as session:
            added = issue
            session.add(added)
            session.commit()
    async def get_book(self, title: str = None, author: str = None, id: int = None ):
        with Session(autoflush=False, bind=engine) as session:
            content = session.query(Book).filter(Book.title == title or Book.author == author).all()
            if content:
                return content
    async def get_author(self, author_first: str = None, author_last: str = None):
        with Session(autoflush=False, bind=engine) as session:
            content = session.query(Author).filter(Author.first_name == author_first and Author.last_name == author_last).all()
            if content:
                return content

    async  def get_issue(self, book_id: int = None, reader: str = None):
        with Session(autoflush=False, bind=engine) as session:
            content = session.query(Borrow).filter(Borrow.book_id == book_id or Borrow.reader_name == reader).all()
            if content:
                return content


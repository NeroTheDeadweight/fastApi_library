from sqlalchemy.ext.asyncio import AsyncSession
from main_app.domain.models.models import Book
from main_app.schemas.books import BookCreate, BookUpdate
from main_app.domain.repositories.books import BookRepository

class BookService:
    @staticmethod
    async def create_book(db: AsyncSession, book_data: BookCreate) -> Book:
        book = Book(**book_data.dict())
        return await BookRepository.create(db, book)

    @staticmethod
    async def get_books(db: AsyncSession) -> list[Book]:
        return await BookRepository.get_all(db)

    @staticmethod
    async def get_book(db: AsyncSession, book_id: int) -> Book | None:
        return await BookRepository.get_by_id(db, book_id)

    @staticmethod
    async def update_book(db: AsyncSession, book_id: int, book_data: BookUpdate) -> Book | None:
        book = await BookRepository.get_by_id(db, book_id)
        if not book:
            return None
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(book, key, value)
        return await BookRepository.create(db, book)

    @staticmethod
    async def delete_book(db: AsyncSession, book_id: int) -> bool:
        book = await BookRepository.get_by_id(db, book_id)
        if not book:
            return False
        await BookRepository.delete(db, book)
        return True

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from main_app.domain.models.models import Book

class BookRepository:
    @staticmethod
    async def create(db: AsyncSession, book: Book):
        db.add(book)
        await db.commit()
        await db.refresh(book)
        return book

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Book))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db: AsyncSession, book_id: int):
        result = await db.execute(select(Book).filter_by(id=book_id))
        return result.scalar_one_or_none()

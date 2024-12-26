from sqlalchemy import create_engine
from main_app.domain.models.models import Author, Book, Borrow
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from main_app.domain.models.models import Author

class AuthorRepository:
    @staticmethod
    async def create(db: AsyncSession, author: Author):
        db.add(author)
        await db.commit()
        await db.refresh(author)
        return author

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Author))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db: AsyncSession, author_id: int):
        result = await db.execute(select(Author).filter_by(id=author_id))
        return result.scalar_one_or_none()
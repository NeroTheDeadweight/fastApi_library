from sqlalchemy import create_engine
from main_app.domain.models.models import Author, Book, Borrow
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class BorrowRepository:
    @staticmethod
    async def create(db: AsyncSession, borrow: Borrow):
        db.add(borrow)
        await db.commit()
        await db.refresh(borrow)
        return borrow

    @staticmethod
    async def get_all(db: AsyncSession):
        result = await db.execute(select(Borrow))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(db: AsyncSession, borrow_id: int):
        result = await db.execute(select(Borrow).filter_by(id=borrow_id))
        return result.scalar_one_or_none()
from sqlalchemy.ext.asyncio import AsyncSession
from main_app.domain.models.models import Borrow
from main_app.schemas.borrows import BorrowCreate, BorrowReturn
from main_app.domain.repositories.borrows import BorrowRepository

class BorrowService:
    @staticmethod
    async def create_borrow(db: AsyncSession, borrow_data: BorrowCreate) -> Borrow:
        borrow = Borrow(**borrow_data.dict())
        return await BorrowRepository.create(db, borrow)

    @staticmethod
    async def get_borrows(db: AsyncSession) -> list[Borrow]:
        return await BorrowRepository.get_all(db)

    @staticmethod
    async def get_borrow(db: AsyncSession, borrow_id: int) -> Borrow | None:
        return await BorrowRepository.get_by_id(db, borrow_id)

    @staticmethod
    async def return_borrow(db: AsyncSession, borrow_id: int, borrow_return: BorrowReturn) -> Borrow | None:
        borrow = await BorrowRepository.get_by_id(db, borrow_id)
        if not borrow:
            return None
        borrow.return_date = borrow_return.return_date
        return await BorrowRepository.create(db, borrow)

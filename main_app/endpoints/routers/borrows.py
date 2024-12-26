from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from main_app.schemas.borrows import BorrowCreate, BorrowRead, BorrowReturn
from main_app.services.borrow_usecase import BorrowService
from main_app.endpoints.depends import get_db

router = APIRouter()

@router.post("/", response_model=BorrowRead)
async def create_borrow(borrow: BorrowCreate, db: AsyncSession = Depends(get_db)):
    return await BorrowService.create_borrow(db, borrow)

@router.get("/", response_model=list[BorrowRead])
async def get_borrows(db: AsyncSession = Depends(get_db)):
    return await BorrowService.get_borrows(db)

@router.get("/{borrow_id}", response_model=BorrowRead)
async def get_borrow(borrow_id: int, db: AsyncSession = Depends(get_db)):
    borrow = await BorrowService.get_borrow(db, borrow_id)
    if not borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return borrow

@router.patch("/{borrow_id}/return", response_model=BorrowRead)
async def return_borrow(borrow_id: int, borrow_return: BorrowReturn, db: AsyncSession = Depends(get_db)):
    updated_borrow = await BorrowService.return_borrow(db, borrow_id, borrow_return)
    if not updated_borrow:
        raise HTTPException(status_code=404, detail="Borrow not found")
    return updated_borrow
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from main_app.schemas.books import BookCreate, BookRead, BookUpdate
from main_app.services.book_usecase import BookService
from main_app.endpoints.depends import get_db

router = APIRouter()

@router.post("/", response_model=BookRead)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await BookService.create_book(db, book)

@router.get("/", response_model=list[BookRead])
async def get_books(db: AsyncSession = Depends(get_db)):
    return await BookService.get_books(db)

@router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    book = await BookService.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)):
    updated_book = await BookService.update_book(db, book_id, book)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    success = await BookService.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from main_app.schemas.authors import AuthorCreate, AuthorRead, AuthorUpdate
from main_app.services.author_usecase import AuthorService
from main_app.endpoints.depends import get_db

router = APIRouter()

@router.post("/", response_model=AuthorRead)
async def create_author(author: AuthorCreate, db: AsyncSession = Depends(get_db)):
    return await AuthorService.create_author(db, author)

@router.get("/", response_model=list[AuthorRead])
async def get_authors(db: AsyncSession = Depends(get_db)):
    return await AuthorService.get_authors(db)

@router.get("/{author_id}", response_model=AuthorRead)
async def get_author(author_id: int, db: AsyncSession = Depends(get_db)):
    author = await AuthorService.get_author(db, author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=AuthorRead)
async def update_author(author_id: int, author: AuthorUpdate, db: AsyncSession = Depends(get_db)):
    updated_author = await AuthorService.update_author(db, author_id, author)
    if not updated_author:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

@router.delete("/{author_id}", status_code=204)
async def delete_author(author_id: int, db: AsyncSession = Depends(get_db)):
    success = await AuthorService.delete_author(db, author_id)
    if not success:
        raise HTTPException(status_code=404, detail="Author not found")
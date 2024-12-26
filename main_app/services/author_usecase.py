from sqlalchemy.ext.asyncio import AsyncSession
from main_app.domain.models.models import Author
from main_app.schemas.authors import AuthorCreate, AuthorUpdate
from main_app.domain.repositories.authors import AuthorRepository

class AuthorService:
    @staticmethod
    async def create_author(db: AsyncSession, author_data: AuthorCreate) -> Author:
        author = Author(**author_data.dict())
        print(author.__dict__)
        return await AuthorRepository.create(db, author)

    @staticmethod
    async def get_authors(db: AsyncSession) -> list[Author]:
        return await AuthorRepository.get_all(db)

    @staticmethod
    async def get_author(db: AsyncSession, author_id: int) -> Author | None:
        return await AuthorRepository.get_by_id(db, author_id)

    @staticmethod
    async def update_author(db: AsyncSession, author_id: int, author_data: AuthorUpdate) -> Author | None:
        author = await AuthorRepository.get_by_id(db, author_id)
        if not author:
            return None
        for key, value in author_data.dict(exclude_unset=True).items():
            setattr(author, key, value)
        return await AuthorRepository.create(db, author)

    @staticmethod
    async def delete_author(db: AsyncSession, author_id: int) -> bool:
        author = await AuthorRepository.get_by_id(db, author_id)
        if not author:
            return False
        await AuthorRepository.delete(db, author)
        return True

from sqlalchemy.ext.asyncio import AsyncSession
from main_app.database import Session_db

async def get_db() -> AsyncSession:

    async with Session_db() as session:
        yield session
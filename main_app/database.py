from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from main_app.domain.models.models import Base
import os

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:1234@db:5432/wallet_db")
database_url = "postgresql+asyncpg://postgres:1234@localhost:5432/library_fastapi"
# engine = create_async_engine(database_url, echo=True, future=True)

engine = create_async_engine(database_url,echo=False)
Session_db = async_sessionmaker(engine
                                        , expire_on_commit=False, class_=AsyncSession,
                                        autoflush=False)
# Session_db = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
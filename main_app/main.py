from fastapi import FastAPI
from main_app.endpoints.routers import authors, books, borrows
from main_app.database import init_db

app = FastAPI()

# Подключение роутов
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(borrows.router, prefix="/borrows", tags=["borrows"])

# Инициализация базы данных
@app.on_event("startup")
async def startup_event():
    await init_db()
from app import settings
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.domain.services import AuthService
from app.domain.repositories import AbstractUserRepository, InMemoryUserRepository
from app.infrastructure.database import engine, SessionLocal
from app.infrastructure.repositories import SqlAlchemyUserRepository
from app.api.routes import user_router

app = FastAPI()


def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_user_repository() -> AbstractUserRepository:
    return SqlAlchemyUserRepository()


app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # Change host and port as per your requirement

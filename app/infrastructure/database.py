from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL (e.g. for SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the engine and the session factory
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the declarative base
Base = declarative_base()

# Import the User entity and include it in the declarative base
from app.infrastructure.models import SqlAlchemyUser
Base.metadata.create_all(bind=engine)

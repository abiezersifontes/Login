from app.domain.entities import User
from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base


class SqlAlchemyUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def to_entity(self) -> User:
        return User(id=self.id, username=self.username, email=self.email, password=self.password)
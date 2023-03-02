from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entities import User as UserEntity
from app.domain.value_objects import User as UserValueObject
from app.domain.repositories import AbstractUserRepository
from app.infrastructure.models import SqlAlchemyUser


class SqlAlchemyUserRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user: UserEntity) -> UserEntity:
        db_user = SqlAlchemyUser(username=user.username, email=user.email, password=user.password)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return UserEntity(
            id=db_user.id,
            username=db_user.username,
            email=db_user.email,
            password=db_user.password
            )

    def get_user_by_username(self, username: str) -> Optional[UserEntity]:
        db_user = self.session.query(SqlAlchemyUser).filter(SqlAlchemyUser.username == username).first()
        return UserEntity(
            id=db_user.id,
            username=db_user.username,
            email=db_user.email,
            password=db_user.password
            ) if db_user else None

    def get_user_by_email(self, email: str) -> Optional[UserEntity]:
        db_user = self.session.query(SqlAlchemyUser).filter(SqlAlchemyUser.email == email).first()
        return UserEntity(
            id=db_user.id,
            username=db_user.username,
            email=db_user.email,
            password=db_user.password
            ) if db_user else None


from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities import User


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

class InMemoryUserRepository(AbstractUserRepository):
    def __init__(self):
        self.users = {}
    
    def create_user(self, user: User) -> User:
        self.users[user.username] = user
        return user
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.users[username] if username in self.users else None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        return next(
            (user for user in self.users.values() if user.email == email), None
        )
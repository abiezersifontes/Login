from app.domain.repositories import AbstractUserRepository
from app.domain.value_objects import User as UserValueObject
from app.domain.entities import User as UserEntity


class AuthService:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def sign_in(self, username: str, password: str) -> bool:
        user = self.user_repository.get_user_by_username(username)
        if user is None:
            return False
        return self._verify_password(password, user.password)

    def sign_out(self, username: str) -> bool:
        user = self.user_repository.get_user_by_username(username)
        return user is not None

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        # Your password verification logic here
        return plain_password == hashed_password


class UserService:
    def __init__(self, user_repository: AbstractUserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, email: str, password: str) -> UserEntity:
        user = UserValueObject(username=username, email=email, password=password)
        user_id = self.user_repository.create_user(user)
        return UserEntity(id=user_id ,username=username, email=email, password=password)

    def is_unique(self, username: str) -> bool:
        user = self.user_repository.get_user_by_username(username)
        return user is None
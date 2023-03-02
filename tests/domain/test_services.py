import pytest
from app.domain.entities import User
from app.domain.repositories import AbstractUserRepository, InMemoryUserRepository
from app.domain.services import AuthService


class TestAuthService:
    def test_sign_in_success(self):
        user_repository = self._create_user_repository()
        user = User(
            id=1,
            username="testuser",
            email="testuser@example.com",
            password="password",
        )
        user_repository.create_user(user)
        auth_service = AuthService(user_repository)
        assert auth_service.sign_in(user.username, user.password) is True

    def test_sign_in_failure(self):
        user_repository = self._create_user_repository()
        auth_service = AuthService(user_repository)
        assert auth_service.sign_in("nonexistent", "password") is False
        assert auth_service.sign_in("testuser", "wrongpassword") is False

    def test_sign_out_success(self):
        user_repository = self._create_user_repository()
        user = User(
            id=1,
            username="testuser",
            email="testuser@example.com",
            password="password",
        )
        user_repository.create_user(user)
        auth_service = AuthService(user_repository)
        assert auth_service.sign_out(user.username) is True

    def test_sign_out_failure(self):
        user_repository = self._create_user_repository()
        auth_service = AuthService(user_repository)
        assert auth_service.sign_out("nonexistent") is False

    def _create_user_repository(self) -> AbstractUserRepository:
        # Instantiate and return a concrete user repository implementation here

        # For example, an in-memory repository:
        return InMemoryUserRepository()
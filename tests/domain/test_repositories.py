from faker import Faker
from app.domain.entities import User
from app.domain.repositories import AbstractUserRepository, InMemoryUserRepository

fake = Faker()

class TestUserRepository:
    def test_create_user(self):
        repository = self._create_repository()
        user = User(
            id=fake.random_int(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        created_user = repository.create_user(user)
        assert created_user.id is not None
        assert created_user.username == user.username
        assert created_user.email == user.email
        assert created_user.password == user.password

    def test_get_user_by_username(self):
        repository = self._create_repository()
        user = User(
            id=fake.random_int(),
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        repository.create_user(user)
        retrieved_user = repository.get_user_by_username(user.username)
        assert retrieved_user is not None
        assert retrieved_user.username == user.username
        assert retrieved_user.email == user.email
        assert retrieved_user.password == user.password

    def test_get_user_by_username_nonexistent(self):
        repository = self._create_repository()
        retrieved_user = repository.get_user_by_username("nonexistent")
        assert retrieved_user is None

    def _create_user_repository(self) -> AbstractUserRepository:
        # Instantiate and return a concrete user repository implementation here

        # For example, an in-memory repository:
        return InMemoryUserRepository()
    
    def _create_repository(self) -> AbstractUserRepository:
        return InMemoryUserRepository()
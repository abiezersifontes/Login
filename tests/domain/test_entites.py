import pytest
from app.domain.entities import User


def test_user_entity():
    id = 1
    username = "testuser"
    email = "testuser@example.com"
    password = "password"
    user = User(
        id=id,
        username=username,
        email=email,
        password=password,
    )
    assert user.id == id
    assert user.username == username
    assert user.email == email
    assert user.password == password

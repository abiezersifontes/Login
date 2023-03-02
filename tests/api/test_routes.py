from faker import Faker
import json
from fastapi.testclient import TestClient
from app.main import app

fake = Faker()

client = TestClient(app)


def test_create_user():
    # Send a request to create a new user
    data = {
        "username": fake.user_name(), 
        "email": fake.email(), 
        "password": fake.password()
    }
    response = client.post("/user", json=data)
    assert response.status_code == 201

    

def test_sign_in():
    # create a new user
    data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }
    response = client.post("/user", json=data)
    response2 = client.post("/signin", json={"username": data.get("username"), "password": data.get("password")})
    assert response2.status_code == 200

def test_sign_out():
    # create a new user
    data = {
        "username": fake.user_name(),
        "email": fake.email(),
        "password": fake.password()
    }
    response = client.post("/user", json=data)
    response2 = client.post("/signin", json={"username": data.get("username"), "password": data.get("password")})
    response3 = client.post("/signout", json={"username": data.get("username")})
    assert response3.status_code == 200


    

# Add more test functions for other API routes as needed

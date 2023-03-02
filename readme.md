In order to Run this project you will have to follow the next steps:
====================================================================
    1. install pipenv
    2. install the Dependencies with the command pipenv install
    3. run the migrations
    4. run the server with the command python -m main.app

Running this Project with Docker
================================
    1. install docker
    2. run the command docker-compose up --build
    3. run the migrations
    4. run the server with the command python -m main.app

Running the Migrations
======================
    1. run the command alembic upgrade head
    2. to create a migration run the command alembic revision --autogenerate -m "migration name"

Running the Tests
=================
    1. run the command pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.infrastructure.database import Base, engine

@pytest.fixture(scope="session", autouse=True)
def reset_db():
    # drop all tables
    Base.metadata.drop_all(bind=engine)

    # create all tables
    Base.metadata.create_all(bind=engine)

    yield

    # delete the database file
    os.remove("test.db")

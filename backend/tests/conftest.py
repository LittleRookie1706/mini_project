import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[1] 
sys.path.append(str(package_root_directory))
# 

import warnings
import os
import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
import alembic
from alembic.config import Config
from base.event_handle import db

# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    from database.postgres.sqlaclchemy.sync import init_db
    init_db()
    from base.test_conf.sample_data import create_sample_data
    # yield
    # alembic.command.downgrade(config, "base")

# Create a new application for testing
@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from base.settings import app
    return app

# Grab a reference to our database when needed
@pytest.fixture
def db(app: FastAPI) -> db:
    return app.state._db

# Make requests in our tests
@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"}
        ) as client:
            yield client

### Note: 
# - fixture will call every test
# - fixture with session will call once

#  default
import os
import peewee

# local
from .settings import app
from .exeption_handle import *
from database.postgres.peewee.sync import PeeweeConnectionState, db
from all_env import POSTGRES_USER, POSTGRES_PASS, POSTGRES_DB, POSTGRES_PORT, POSTGRES_HOST
# from database.redis.sync import redis
# os.environ["TESTING"] = "1"

@app.on_event("startup")
async def startup():
    global db

    # Database setting
    TESTING = os.environ.get("TESTING")
    if TESTING:
        db = peewee.PostgresqlDatabase(
            f"{POSTGRES_DB}_test", user=POSTGRES_USER, password=POSTGRES_PASS, host=POSTGRES_HOST, port=POSTGRES_PORT
        )
    #     print("----------------------TEST DB------------------------------")
    # else:
    #     print("----------------------REAL DB------------------------------")

    db._state = PeeweeConnectionState()

    try:
        if db.is_closed():
            db.connect()
        app.state._db = db
    except Exception as e:
        print("--- DB CONNECTION ERROR ---", f"Detail:{e}")

    # router
    from user import (
        authentication, 
        news,
        search_engine
    )
    import admin

    app.include_router(authentication.router)
    app.include_router(news.router)
    app.include_router(search_engine.router)
    app.include_router(admin.router)

    # create fake data for TESTING
    # if TESTING:
    #     from database.postgres.sqlaclchemy.sync import init_db
    #     init_db()
    #     from base.test_conf.sample_data import create_sample_data

    
@app.on_event("shutdown")
async def shutdown():
    db.close()
from .settings import app
from database.postgres.peewee.sync import db
from database.redis.sync import redis

@app.on_event("startup")
async def startup():
    pass
    # if db.is_closed():
    #     db.connect()



@app.on_event("shutdown")
async def shutdown():
    db.close()
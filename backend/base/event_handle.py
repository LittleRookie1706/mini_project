from .settings import app
# from database.postgres.peewee.sync import db

@app.on_event("startup")
async def startup():
    pass
    # if db.is_closed():
    #     db.connect()


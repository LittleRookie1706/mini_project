import os
from sqlmodel import create_engine, SQLModel, Session
from all_env import DATABASE_URL

TESTING = os.environ.get("TESTING")
if TESTING:
    DATABASE_URL += '_test'

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
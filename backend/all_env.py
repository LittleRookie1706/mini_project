import os
import urllib

from dotenv import load_dotenv
load_dotenv()

#environ
environ = os.getenv("environ")

#fastapi
docs_url = os.getenv("docs_url")

#mongodb
database_url = os.environ.get('database_url')

#discord_oauth
CLIENT_ID = os.environ.get('CLIENT_ID')
TOKEN = os.environ.get('TOKEN')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URL = os.environ.get('REDIRECT_URL')

#bot api
bot_api = os.environ.get('bot_api')


###  postgres
# local db
POSTGRES_HOST = os.environ.get('POSTGRES_SERVER', 'localhost')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', '5432')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'fastapi')
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASS = os.environ.get('POSTGRES_PASSWORD', 'secret')
ssl_mode = os.environ.get('ssl_mode','prefer')

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, ssl_mode)

# docker db
# DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@db:5432'

# docker async db
DATABASE_URL = 'postgresql+asyncpg://postgres:postgres@db:5432'
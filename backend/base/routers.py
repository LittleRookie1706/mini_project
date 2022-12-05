from .settings import app
from .exeption_handle import *
from .event_handle import *
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

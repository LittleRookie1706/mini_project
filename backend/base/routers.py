from .settings import app
from .exeption_handle import *
from apps import (
    authentication, 
    news,
    admin 
)

app.include_router(authentication.router)
app.include_router(news.router)
app.include_router(admin.router)

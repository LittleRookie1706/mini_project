from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["News"],
    responses={404: {"description": "Not found"}},
)

from .news import *
from .tags import *
from .comments import *
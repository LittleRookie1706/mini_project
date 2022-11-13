from fastapi import APIRouter

router = APIRouter(
    # prefix="/news",
    tags=["News"],
    responses={404: {"description": "Not found"}},
)

from .news import *
from .tags import *
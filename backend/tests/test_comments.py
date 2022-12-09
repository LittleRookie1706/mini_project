import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED, 
    HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
)
pytestmark = pytest.mark.anyio
access_token = "XQlYdTHW5G02ZG1N6rOR2Y50A8uYSs"

@pytestmark
async def test_get_news_comments_by_id(client: AsyncClient) -> None:
    test_data = []
    response = await client.get("api/news/1/comments/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == test_data

@pytestmark
async def test_get_news_comments_by_id_not_exist(client: AsyncClient) -> None:
    response = await client.get("api/news/0/comments/")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": {"error": "Not found news"}}

# @pytestmark
# async def test_post_news_comments_by_id(client: AsyncClient) -> None:
#     response = await client.post(
#         "api/news/comments/",
#         headers={'Authorization': f'Bearer {access_token}'},
#         json={
#             'news': 1,
#             'rating': 5,
#             'content': 'qua hay luon'
#         },
#     )
#     assert response.status_code == HTTP_201_CREATED
#     assert response.json() == {"detail": {"error": "Not found news"}}

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import (
    HTTP_200_OK, HTTP_201_CREATED, 
    HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
)
pytestmark = pytest.mark.anyio

@pytestmark
async def test_get_news_by_id(client: AsyncClient) -> None:
    response = await client.get("api/news/2/")
    assert response.status_code == HTTP_200_OK

@pytestmark
async def test_get_news_by_id_not_exist(client: AsyncClient) -> None:
    response = await client.get("api/news/0/")
    assert response.status_code == HTTP_404_NOT_FOUND
    assert response.json() == {"detail": {"error": "Not found news"}}

@pytestmark
async def test_get_all_tags(client: AsyncClient) -> None:
    test_data =[
        {
            "id": 1,
            "name": "Khoa học",
            "tag_group": "Khoa học hàn lâm"
        },
        {
            "id": 2,
            "name": "Lịch sử",
            "tag_group": "Khoa học hàn lâm"
        },
        {
            "id": 3,
            "name": "Địa lí",
            "tag_group": "Khoa học hàn lâm"
        },
        {
            "id": 4,
            "name": "Sinh học",
            "tag_group": "Khoa học hàn lâm"
        },
        {
            "id": 5,
            "name": "10 vạn câu hỏi vì sao",
            "tag_group": "Nâng tầm hiểu biết"
        },
        {
            "id": 6,
            "name": "Sự thật thú vị",
            "tag_group": "Nâng tầm hiểu biết"
        },
        {
            "id": 7,
            "name": "1001 bí ẩn",
            "tag_group": "Nâng tầm hiểu biết"
        },
        {
            "id": 8,
            "name": "Danh nhân thế  giới",
            "tag_group": "Nâng tầm hiểu biết"
        },
        {
            "id": 9,
            "name": "Thế giới động vật",
            "tag_group": "Nâng tầm hiểu biết"
        },
        {
            "id": 10,
            "name": "Y học-sức khỏe",
            "tag_group": "Kiến thức thực tế"
        }
    ]
    response = await client.get("api/tags/")
    assert response.status_code == HTTP_200_OK
    assert response.json() == test_data


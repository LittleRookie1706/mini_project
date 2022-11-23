import os
from fastapi import Request, Response
from fastapi_redis_cache import FastApiRedisCache
from database.postgres.peewee.sync import PeeweeModel

LOCAL_REDIS_URL  =  "redis://redis:6379"

redis_cache = FastApiRedisCache()
redis_cache.init(
    host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
    prefix="myapi-cache",
    response_header="X-MyAPI-Cache",
    ignore_arg_types=[Request, Response]
)

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

REDIS_URL  =  "redis://redis:6379"

redis = aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=True)
FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
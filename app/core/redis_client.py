import redis.asyncio as redis
from app.core.config import settings

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    password=settings.redis_password,
    decode_responses=True
)

async def get_redis_client():
    return redis_client

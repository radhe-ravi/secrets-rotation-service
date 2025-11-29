import aioredis
from core.settings import settings


class RedisClient:
    def __init__(self):
        self.redis = None

    async def connect(self):
        self.redis = await aioredis.from_url(
            f"redis://{settings.redis_host}:{settings.redis_port}",
            decode_responses=True,
        )

    async def get_client(self):
        if self.redis is None:
            self.redis = self.connect()
        return self.redis


redis = RedisClient()

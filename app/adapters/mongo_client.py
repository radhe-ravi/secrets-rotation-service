from motor.motor_asyncio import AsyncIOMotorClient
from core.settings import settings


class MongoClient:
    def __init__(self):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_url)
        self.db = self.client.get_default_database()

    def get_collection(self, name: str):
        return self.db[name]


mongoose = MongoClient()

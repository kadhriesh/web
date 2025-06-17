# api/utils/mongo_connection.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoDBConnection:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._client = MongoClient(os.getenv('MONGODB_URL'))
        return cls._instance

    @property
    def client(self):
        return self._client

    def get_database(self, db_name=None):
        db_name = db_name or os.getenv('MONGODB_DB')
        return self._client[db_name]
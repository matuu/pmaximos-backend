import os
from pymongo import MongoClient

class MongoDbConnection:
    def __init__(self):
        self._password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        self._user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
        self._db_name = os.getenv("MONGO_INITDB_DATABASE")
        self._client = MongoClient(f'mongodb://{self._user}:{self._password}@database:27017/')
        self._db = self._client[self._db_name]

    @property
    def db(self):
        return self._db


db = MongoDbConnection().db
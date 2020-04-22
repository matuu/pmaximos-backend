import os
from pymongo import MongoClient

class MongoDbConnection:
    def __init__(self):
        self._password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        self._user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
        self._db_name = os.getenv("MONGO_INITDB_DATABASE")
        self._protocol = os.getenv("MONGO_INITDB_PROTOCOL", 'mongodb')
        self._host = os.getenv('MONGO_INITDB_HOST', 'database')
        self._port = os.getenv('MONGO_INITDB_PORT')
        host = self._host
        if self._port is not None:
            host = f"{self._host}:{self._port}"

        self._client = MongoClient(f'{self._protocol}://{self._user}:{self._password}@{host}/{self._db_name}')
        self._db = self._client[self._db_name]

    @property
    def db(self):
        return self._db


db = MongoDbConnection().db
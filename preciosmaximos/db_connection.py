import os
from pymongo import MongoClient

class MongoDbConnection:
    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")
        db_name = os.getenv("MONGO_INITDB_DATABASE")
        if mongo_uri is not None:
            self._client = MongoClient(mongo_uri)
        else:
            password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
            user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
            self._client = MongoClient(f'mongodb://{user}:{password}@database:27017/{db_name}')
        self._db = self._client[db_name]

    @property
    def db(self):
        return self._db


db = MongoDbConnection().db
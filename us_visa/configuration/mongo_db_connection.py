import sys
import os
import pymongo
import certifi

from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME

ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME):
        try:
            mongo_db_url = os.getenv("MONGODB_URL")
            if mongo_db_url is None:
                raise Exception("Environment variable MONGODB_URL is not set.")
            
            if MongoDBClient.client is None:
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)

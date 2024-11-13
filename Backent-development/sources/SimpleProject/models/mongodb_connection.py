# models/mongodb_connection.py

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnection:
    def __init__(self, mongodb_ip="localhost", port=27017, db_name="MYDB"):
        self.mongodb_ip = mongodb_ip
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(f'mongodb://{self.mongodb_ip}:{self.port}/')
            self.db = self.client[self.db_name]
            self.client.admin.command('ping')
            print("Connected to MongoDB server successfully.")
            return self.db
        except ConnectionFailure:
            print("Failed to connect to MongoDB server.")
            raise

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

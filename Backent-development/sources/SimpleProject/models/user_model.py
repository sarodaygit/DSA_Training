# models/user_model.py

from bson.objectid import ObjectId
from models.mongodb_connection import MongoDBConnection

class UserModel:
    def __init__(self):
        self.mongodb = MongoDBConnection()
        self.db = self.mongodb.connect()
        self.user_collection = self.db['USERS']

    def add_user(self, user_data):
        try:
            result = self.user_collection.insert_one(user_data)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error inserting user: {e}")
            raise

    def get_all_users(self):
        try:
            users = list(self.user_collection.find())
            for user in users:
                user["_id"] = str(user["_id"])  # Convert _id to string for JSON response
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            raise

    def get_user_by_id(self, user_id):
        try:
            user = self.user_collection.find_one({"_id": ObjectId(user_id)})
            if user:
                user["_id"] = str(user["_id"])  # Convert _id to string for JSON response
                return user
            return None
        except Exception as e:
            print(f"Error retrieving user by ID: {e}")
            raise

    def get_user_by_name(self, name):
        try:
            # Search for a user where the 'username' field matches the provided name
            user = self.user_collection.find_one({"username": name})  # exact match for username
            
            if user:
                user["_id"] = str(user["_id"])  # Convert _id to string for JSON response
                return user
            return None
        except Exception as e:
            print(f"Error retrieving user by name: {e}")
            raise

    def delete_user_by_name(self, username):
        try:
            result = self.user_collection.delete_one({"username": username})
            if result.deleted_count > 0:
                return True
            return False
        except Exception as e:
            print(f"Error deleting user by name: {e}")
            raise
    
    def get_user_count(self):
        try:
            return self.user_collection.count_documents({})
        except Exception as e:
            print(f"Error retrieving user count: {e}")
            raise
    
    def get_users_by_age(self, min_age=25):
        try:
            # Query the collection for users with age >= min_age
            users = list(self.user_collection.find({"age": {"$gte": min_age}}))
            for user in users:
                user["_id"] = str(user["_id"])  # Convert _id to string for JSON response
            return users
        except Exception as e:
            print(f"Error retrieving users by age: {e}")
            raise
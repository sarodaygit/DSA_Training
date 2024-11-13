from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# Localhost connection settings
mongodb_ip = "localhost"  # or use "127.0.0.1"
port = 27017  # Default MongoDB port

try:
    # Connect to MongoDB on the local machine
    client = MongoClient(f'mongodb://{mongodb_ip}:{port}/', serverSelectionTimeoutMS=5000)
    client.admin.command('ping')  # Ping the server to confirm connection
    print("Connected to MongoDB server successfully.")

    # Access a specific database
    db = client['MYDB']  # Replace with your database name

    # List all collections to verify the connection
    collections = db.list_collection_names()
    print("Collections in the database:", collections)

except ConnectionFailure:
    print("Failed to connect to MongoDB server.")
except OperationFailure:
    print("Operation failure occurred (check server permissions or settings).")
finally:
    # Close the connection when done
    client.close()
    print("Connection closed.")

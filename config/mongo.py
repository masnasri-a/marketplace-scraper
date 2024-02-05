from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access environment variables
mongo_host = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")

def get_mongo_collection(mongo_collection: str = None):
    # Create a MongoDB client
    client = MongoClient(mongo_host)

    # Access the specified database and collection
    db = client[mongo_db]
    collection = db[mongo_collection] if mongo_collection else db['Accounts']

    return client, collection

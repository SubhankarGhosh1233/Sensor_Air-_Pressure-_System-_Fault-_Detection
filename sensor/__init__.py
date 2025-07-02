from pymongo import MongoClient
from dotenv import load_dotenv
import os
print(f"Loading environment variable from .env file")
load_dotenv()
client = MongoClient(os.getenv("MONGO_DB_URL"))
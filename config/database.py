from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("DB_URI"))

db = client.blog_db

collection_name = db["blog_collection"]

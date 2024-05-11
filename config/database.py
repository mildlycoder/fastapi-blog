from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://pranavismic:jtty81DYjjPpIai1@cluster0.gf9lutj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client.blog_db

collection_name = db["blog_collection"]

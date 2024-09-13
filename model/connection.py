from pymongo import MongoClient
from setup.environment import Setup
setup=Setup()
client = MongoClient(setup.url)
db = client[setup.db_name]
collection = db[setup.collection_name]
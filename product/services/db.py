from pymongo import MongoClient
from pymongo.server_api import ServerApi


DB_NAME = 'Product'
password='devsecops2023'
uri = "mongodb+srv://tesis:{password}@tesisdevsecops2023.wdmpqj0.mongodb.net/?retryWrites=true&w=majority"

connection = MongoClient(uri, server_api=ServerApi('1'))
db_client = connection[DB_NAME]

from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = 'Product'
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
uri = ("mongodb+srv://{username}:{password}"
       "@tesisdevsecops2023.wdmpqj0.mongodb.net/"
       "?retryWrites=true&w=majority")


connection: MongoCloud = MongoClient(uri, server_api=ServerApi('1'))
db_client = MongoCloud[DB_NAME]

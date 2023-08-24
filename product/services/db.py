import os

from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

DB_NAME = 'Product'
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
if username is None or password is None:
    print("Error: Las variables de entorno DB_USERNAME y/o DB_PASSWORD no están definidas")
else:
    uri = ("mongodb+srv://" + username + ":" + password +
           "@tesisdevsecops2023.wdmpqj0.mongodb.net/" +
           "?retryWrites=true&w=majority")


connection: MongoClient = MongoClient(uri, server_api=ServerApi('1'))
db_client = connection[DB_NAME]

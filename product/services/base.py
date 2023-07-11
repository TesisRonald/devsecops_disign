from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

DB_NAME = 'Product'
COLLECTION_NAME = 'products'

uri = "mongodb+srv://rvquichimbo:ron1VIC21995@tesisdevsecops2023.wdmpqj0.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the 'product' database
db = client[DB_NAME]

# Access the 'products' collection
collection = db[COLLECTION_NAME]

# Find all documents in the 'products' collection
results = collection.find()

# Print the results
for document in results:
    print(document)

from pymongo import MongoClient

connection = MongoClient()
db = connection.testUser # Connect to database testUser
col = db.vault001 # Collection vault001

query = {"_id": "lb01"}
newvalues = {"$set": {"state": 1}}

col.update(query, newvalues)
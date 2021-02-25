from pymongo import MongoClient
import datetime

connection = MongoClient()
db = connection.testUser # Connection with databse testUser

def insertUserData():
    data = {"_id": "toy001",
            "details": {"userName": "Marakov",
                        "email": "marakovzanaruk5@hotmail.com",
                        "password": "$2b$12$MomCfvu/EC0DS5D4YNRtd..yfEedhVpo05CFsl/4u0yeXwy65BAqq",
                        "pin": "1111"},
            "date": datetime.datetime.now()}

    users = db.users # Create Collection name users
    insert_data = users.insert(data) # Insert data to collection users

def insertVaultData():
    data = {"_id": "toy001",
            "detailsBulb01": {"bulbId": "lb001", "state": "0"},
            "detailsBulb02": {"bulbId": "lb002", "state": "0"},
            "detailsBulb03": {"bulbId": "lb003", "state": "0"},
            "detailsBulb04": {"bulbId": "lb004", "state": "0"},
            "detailsBulb05": {"bulbId": "lb005", "state": "0"},
            "detailsBulb06": {"bulbId": "lb006", "state": "0"}}
    bulbs = db.bulbs  # Create Collection name bulbs
    insert_data = bulbs.insert(data) # Insert data to collection bulbs

# insertUserData()
# insertVaultData()
import pymongo
import asyncio
import json
from decouple import config


MONGO_DETAILS = config('MONGO_DETAILS')

client = pymongo.MongoClient(MONGO_DETAILS)

db = client.testDB

collection = db.vault001_for_app_collection


def updateOneValueForAppCollection(old_value, new_value):
    collection.update_one(old_value, new_value)

def checkState(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "color": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["state"]

def checkColor(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "state": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["color"]

def checkTimeOnHour(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "state": 0, "color": 0, "setTimeOn_min": 0, "setTimeOff_hour": 0, "setTimeOff_min": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["setTimeOn_hour"]

def checkTimeOnMin(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "state": 0, "color": 0, "setTimeOn_hour": 0, "setTimeOff_hour": 0, "setTimeOff_min": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["setTimeOn_min"]

def checkTimeOffHour(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "state": 0, "color": 0, "setTimeOn_hour": 0, "setTimeOn_min": 0, "setTimeOff_min": 0}) 
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["setTimeOff_hour"]

def checkTimeOffMin(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "state": 0, "color": 0, "setTimeOn_hour": 0, "setTimeOn_min": 0, "setTimeOff_hour": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["setTimeOff_min"]




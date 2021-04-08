import pymongo
import asyncio
import json
from decouple import config


MONGO_DETAILS = config('MONGO_DETAILS')

client = pymongo.MongoClient(MONGO_DETAILS)

db = client.testDB

collection = db.vault001_collection


def checkState(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["state"]


def checkColor(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["color"]


async def updateOneValue(old_value, new_value):
    collection.update_one(old_value, new_value)


def checkCalTime(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["calTime_start"]


def checkTotalTime(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["totalTime"]



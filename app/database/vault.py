import pymongo
import asyncio
import json
from decouple import config

#client = pymongo.MongoClient("mongodb+srv://mktsy:makiitheslayer@cluster0.hg6xy.mongodb.net/LightDatabase?retryWrites=true&w=majority")

MONGO_DETAILS = config('MONGO_DETAILS')

client = pymongo.MongoClient(MONGO_DETAILS)

db = client.testDB

collection = db.vault001_collection


def check_state(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["state"]

def check_color(light_number):
    pass


async def update_one_value(old_value, new_value):
    collection.update_one(old_value, new_value)
    #task = asyncio.create_task(collection.update_one(old_value, new_value))
    #await task
    #print("Database updated.")


def check_cal_time(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["calTime_start"]

def check_total_time(light_number):
    value = collection.find_one({"lightNumber": light_number}, {"_id": 0, "startTime": 0, "endTime": 0})
    convert_value = json.dumps(value)
    load_value = json.loads(convert_value)
    return load_value["totalTime"]



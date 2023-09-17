from typing import Collection
from django.shortcuts import render
from django.http import HttpResponse
from bson.objectid import ObjectId


import pymongo 


def mongoConnection_collection():
    client = pymongo.MongoClient("mongodb://harshxtanwar:db12345@ac-zdnook2-shard-00-00.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-01.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-02.dvbpycz.mongodb.net:27017/?ssl=true&replicaSet=atlas-83le6q-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["eco"]
    collection = db["event_details"]
    return collection


def mongoConnection_registered_collection():
    client = pymongo.MongoClient("mongodb://harshxtanwar:db12345@ac-zdnook2-shard-00-00.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-01.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-02.dvbpycz.mongodb.net:27017/?ssl=true&replicaSet=atlas-83le6q-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["eco"]
    collection = db["registered"]
    return collection


def post_db(request):
    # name = request.get("name")
    # instructions = request.get("")
    collection = mongoConnection_collection()
    collection.insert_one(request)


def get_db_browse(request):
    if request.method == "GET":

        collection = mongoConnection_collection()
        query = list(collection.find())

        listt = []
        for i in query:
            dic = {
                'id' : i.get('_id'),
                'event_name' : i.get('event_name'),
                'event_date' : i.get('event_date'),
                'event_time' : i.get('event_time'),
                'event_location' : i.get('event_location')
            }
            listt.append(dic)


        
        print ((listt))
    return listt

def query_by_id(id):
    collection = mongoConnection_collection()
    query = collection.find_one({"_id": ObjectId(id)})
    return (query, id)


def post_mongodb_registered(name, email, event_name):

    collection = mongoConnection_registered_collection()
    collection.insert_one({
        'event_name': event_name,
        'name':name,
        'email': email
    })
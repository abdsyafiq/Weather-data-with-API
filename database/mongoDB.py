from pymongo import MongoClient, errors
import json

from helper import logger


def mongo_conn(username: str, password: str, server_1: str, server_2: str, server_3: str, port: str, auth_db: str, replica_set: str):
    # Connect to MongoClient
    uri = f"mongodb://{username}:{password}@{server_1}:{port},{server_2}:{port},{server_3}:{port}/{auth_db}?replicaSet={replica_set}"
    return MongoClient(uri)


def insert_one(mongo_client: MongoClient, response: json, db: str, collection: str) -> None:
    try:
        db = mongo_client[db]
        collection = db[collection]

        # Insert to Mongo Database
        if response.get("cod") == 200:
            collection.insert_one(response)
            logger("Weather data inserted into MongoDB successfully.")
        else:
            logger(">> Failed to retrieve weather data from API.")

    except errors.ServerSelectionTimeoutError as e:
        logger(f">> Error '{e}'")


def find_all_data(mongo_client: MongoClient, db: str, collection: str):
    try:
        db = mongo_client[db]
        collection = db[collection]

        # Find Data
        return collection.find().sort("_id", 1)

    except errors.ServerSelectionTimeoutError as e:
        logger(f">> Error '{e}'")
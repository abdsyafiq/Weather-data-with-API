from pymongo import MongoClient, errors
import json

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from helper import logger


def insert_one(username: str, password: str, server_1: str, server_2: str, server_3: str, port: str, auth_db: str, replica_set: str, response: json, db: str, collection: str) -> None:
    try:
        # Connect to MongoClient
        uri = f"mongodb://{username}:{password}@{server_1}:{port},{server_2}:{port},{server_3}:{port}/{auth_db}?replicaSet={replica_set}"
        client = MongoClient(uri)
        db = client[db]
        collection = db[collection]

        # Insert to Mongo Database
        if response.get("cod") == 200:
            collection.insert_one(response)
            logger("Weather data inserted into MongoDB successfully.")
        else:
            logger(">> Failed to retrieve weather data from API.")

    except errors.ServerSelectionTimeoutError as e:
        logger(f">> Error '{e}'")
import time

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

weather_api_dir = os.path.join(parent_dir, "weatherAPI")
mongoDB_dir = os.path.join(parent_dir, "database")
sys.path.append(weather_api_dir)
sys.path.append(mongoDB_dir)

from weatherAPI.API import weather_api
from database.mongoDB import mongo_conn
from database.mongoDB import insert_one


# Weather API Params
city = "city"

# MongoDB Configs
mongo_conf = {
    "server_1": "192.168.1.131",
    "server_2": "192.168.8.177",
    "server_3": "192.168.8.146",
    "port": "27017",
    "username": "psn",
    "password": "psn2024.",
    "auth_db": "admin",
    "replica_set": "rs0",
}
db = "weatherTestingAPI3"
collection = "weather"

while True:
    insert_one(mongo_client=mongo_conn(**mongo_conf), response=weather_api(city), db=db, collection=collection)
    # time.sleep(10)
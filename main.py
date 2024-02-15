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
from database.mongoDB import insert_one


# Weather API Params
city = "city"

# MongoDB Configs
mongo_conf = {
    "server_1": "ip1",
    "server_2": "ip2",
    "server_3": "ip3",
    "port": "port",
    "username": "user",
    "password": "pass",
    "auth_db": "auth",
    "replica_set": "replication_name",
    "db": "database",
    "collection": "collection",
}

while True:
    insert_one(**mongo_conf, response=weather_api(city))
    # time.sleep(10)
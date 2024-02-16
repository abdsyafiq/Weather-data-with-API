import time
from helper import logger

from weatherAPI.API import weather_api
from database.mongoDB import mongo_conn
from database.mongoDB import insert_one

import traceback


# Weather API Params
city = "city"

# MongoDB Configs
mongo_conf = {
    "server_1": "ip1",
    "server_2": "ip2",
    "server_3": "ip3",
    "port": "port",
    "username": "user",
    "password": "password",
    "auth_db": "db",
    "replica_set": "name",
}
db = "weatherTestingAPI3"
collection = "weather"

logger("Starting to retrieve data and insert it into the database.")
while True:
    try:
        insert_one(mongo_client=mongo_conn(**mongo_conf), response=weather_api(city), db=db, collection=collection)
        time.sleep(5)

    except Exception as e:
        error_message = f">> Error: {str(e)}\n{traceback.format_exc()}"
        logger(error_message)
        continue

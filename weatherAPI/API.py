import requests
import json

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from helper import logger


def weather_api(city: str) -> json:
    try:
        # Get Weather Data
        API_KEY = open("./weatherAPI/api_key", "r").read().strip()
        URL = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"

        return requests.get(URL).json()

    except Exception as e:
        logger(f">> Error '{e}'")

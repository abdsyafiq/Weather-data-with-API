import requests
import json

import traceback

from helper import logger


def weather_api(city: str) -> json:
    try:
        # Get Weather Data
        API_KEY = open("./weatherAPI/api_key", "r").read().strip()
        URL = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"

        return requests.get(URL).json()

    except Exception as e:
        error_message = f">> Error: {str(e)}\n{traceback.format_exc()}"
        logger(error_message)

from datetime import datetime
from datetime import timezone
import pandas as pd


def logger(message: str) -> None:
    """This function logs the mentioned message at a given stage of the code execution to a log file.
    Function returns nothing"""

    now = datetime.now().strftime("%d-%h-%Y %H:%M:%S")
    with open("./log/process.log", "a") as f: 
        f.write(f"[{now}]" + " " + message + "\n")

    if message.startswith(">> "):
        with open("./log/error.log", "a") as f: 
            f.write(f"[{now}]" + " " + message + "\n")


def convert_unix_timestamp(unix: int, offset: int) -> pd.Timestamp:
    return datetime.fromtimestamp(
        unix + offset, timezone.utc
    ).isoformat()


def kelvin_to_celcius(kelvin: float) -> float:
    return kelvin - 273.15


def round_to_nearest_hour(timestamp: pd.Timestamp):
    return timestamp.floor('H')

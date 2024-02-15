from datetime import datetime


def logger(message: str) -> None:
    """This function logs the mentioned message at a given stage of the code execution to a log file.
    Function returns nothing"""

    now = datetime.now().strftime("%d-%h-%Y %H:%M:%S")
    with open("./log/process.log", "a") as f: 
        f.write(f"[{now}]" + " " + message + "\n")

    if message.startswith(">> "):
        with open("./log/error.log", "a") as f: 
            f.write(f"[{now}]" + " " + message + "\n")

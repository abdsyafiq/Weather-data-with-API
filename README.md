# Weather Data with REST API

This repository contains a Python script (`main.py`) that retrieves weather data from the OpenWeatherMap API based on the city name provided by the user. The retrieved data, in JSON format, is then inserted into a MongoDB database.

## Installation

1. Clone the repository.
2. Install the required Python packages.
3. Ensure you have MongoDB installed and running on your system.

## Usage

1. Replace the city to get the weather data you want.
2. Replace mongodb configuration according to your specifications.
3. Run the `main.py` script.
4. The script will fetch weather data from OpenWeatherMap API and insert it into the MongoDB database.

## Logging

- All process logs are documented in the `log/process.log` file.
- Error logs are stored in the `log/error.log` file, which only contains information about errors encountered during the process.


## Dependencies

- [requests](https://pypi.org/project/requests/): Used for making HTTP requests to the OpenWeatherMap API.
- [pymongo](https://pypi.org/project/pymongo/): Python driver for MongoDB.

## MongoDB Replication for High Availability

This project implements MongoDB replication with three servers to ensure high availability. The MongoDB configuration (`mongo_conf`) includes three server addresses (`server_1`, `server_2`, `server_3`) and utilizes a replica set (`replica_set`). In the event of the primary server failure, one of the secondary servers will automatically take over as the primary server, ensuring continuous availability of the database.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
UVICORN_WORKERS_COUNT = os.environ.get("UVICORN_WORKERS_COUNT")
ENVIRONMENT = os.environ.get("ENVIRONMENT")
ELASTICSEARCH_PORT = int(os.environ.get("ELASTICSEARCH_PORT"))

CANADA_FIPS_CODE = {
    "01": "AB",
    "02": "BC",
    "03": "MB",
    "04": "NB",
    "05": "NL",
    "07": "NS",
    "08": "ON",
    "09": "PE",
    "10": "QC",
    "11": "SK",
    "12": "YT",
    "13": "NT",
    "14": "NU",
}

COUNTRY_NAME = {"US": "USA", "CA": "Canada"}

import os
from typing import List

API_ID = os.environ.get("API_ID", "29171167")
API_HASH = os.environ.get("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7251898668 1337857036"))

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002190352334"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002442422204 -1001785093771").split())) # Add Multiple channel ids

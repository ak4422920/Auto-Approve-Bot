import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "8371607189"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/KzxDQL7n/photo-2025-08-05-13-46-11-7535097427330596884.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002190352334"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"  # Set "True" For accept new requests

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001785093771 -1002714455064").split())) # Add Multiple channel ids

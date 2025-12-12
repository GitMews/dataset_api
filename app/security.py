import configparser
from pathlib import Path
from fastapi import Header, HTTPException   

# Get conf file
CONFIG_FILE = Path("config.ini")

# Load key
def load_api_key():
    config = configparser.RawConfigParser()
    config.read(CONFIG_FILE)
    return config["api"]["key"]

API_KEY = load_api_key()

def check_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
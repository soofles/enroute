import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(name: str):
    key = os.getenv(name)
    if not key:
        raise RuntimeError(f"{name} Not Found")
    return key
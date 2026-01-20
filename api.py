import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def get_api_key(env_var_name):
    return os.getenv(env_var_name)

def get_excuse(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        excuse = response.json()
        return excuse.get("reason") or excuse.get("excuse") or excuse.get("text")
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except (ValueError, json.JSONDecodeError):
        return "Error decoding JSON"

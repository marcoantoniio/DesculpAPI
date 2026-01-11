import os
from dotenv import load_dotenv
import requests
import json

def get_api_key(your_api_key):
    load_dotenv()
    return os.getenv(your_api_key)

def get_excuse(api_key):
    try:
        response = requests.get(api_key)
        response.raise_for_status()
        excuse = response.json()
        return excuse["reason"]
    
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

    except (ValueError, json.JSONDecodeError):
        return "Error decoding JSON"

    except KeyError:
        return "Field 'reason' not found in response"

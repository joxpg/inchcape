import sys
import requests
import logging
from config import credentials
# Configure logging
logging.basicConfig(level=logging.INFO)

def handler(event, context):
    url = credentials.URL_TYPICODE
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.info("Data fetched successfully.")
        return data
    else:
        logging.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

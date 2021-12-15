import os
from dotenv import dotenv_values, load_dotenv

def load_warehouse_credentials():
    credentials = {
        'user': os.getenv('WAREHOUSE_USER'),
        'password': os.getenv('WAREHOUSE_PASSWORD'),
        'db': os.getenv('WAREHOUSE_DB'),
        'host': os.getenv('WAREHOUSE_HOST'),
        'port': int(os.getenv('WAREHOUSE_PORT', 5432)),
    }

    return credentials


def get_auth():
	
	# Load secret form .env
	keys = dotenv_values(".env")

	# Set params for API token retrieval
	URL = "https://id.twitch.tv/oauth2/token"
	PARAMS = {
	"client_id": keys["CLIENT_ID"],
	"client_secret": keys["CLIENT_SECRET"],
	"grant_type": "client_credentials"
	}

	# POST request for token
	r = requests.post(url = URL, params = PARAMS)
	# Fetch token from return data
	access_token = r.json()["access_token"]

	return keys["CLIENT_ID"], access_token
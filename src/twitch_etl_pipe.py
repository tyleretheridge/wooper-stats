# File to pull data from twitch API
import requests
import os
from dotenv import dotenv_values



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



def api_requests(client_id, access_token, endpoint, params=None):
	URL = "https://api.twitch.tv/helix/" + endpoint
	headers = {
    'Client-Id': client_id,
    'Authorization': f"Bearer {access_token}"
	}

	r = requests.get(url=URL, headers=headers, params=params)

	return r.json()




if __name__ == "__main__":
	endpoint = "streams"
	client_id, access_token = get_auth()
	data = api_requests(client_id, access_token, endpoint)
	print(data)
	print(data["data"][0])
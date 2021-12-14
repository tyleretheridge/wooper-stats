# File to pull data from twitch API
import requests
import os
from dotenv import dotenv_values



keys = dotenv_values(".env")

CLIENT_ID = keys["CLIENT_ID"]
CLIENT_SECRET = keys["CLIENT_SECRET"]
GRANT_TYPE = "client_credentials"

URL = "https://id.twitch.tv/oauth2/token"
PARAMS = {
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "grant_type": GRANT_TYPE
}





r1 = requests.post(url = URL, params = PARAMS)
token = r1.json()['access_token']


URL2 = 'https://api.twitch.tv/helix/users?login=xqcow'
headers = {
    'Client-Id': CLIENT_ID,
    'Authorization': f"Bearer {token}"
}



if __name__ == "__main__":
    r2 = requests.get(url=URL2, headers=headers)
    print(r2.json())
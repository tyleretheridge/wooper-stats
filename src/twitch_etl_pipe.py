# File to pull data from twitch API
import requests
from dotenv import load_dotenv
from auth_config import load_twitch_creds, load_warehouse_creds


def fetch_token(twitch_credentials):
    URL = "https://id.twitch.tv/oauth2/token"
    r = requests.post(url=URL, params=twitch_credentials)

    access_token = r.json()["access_token"]

    return twitch_credentials["client_id"], access_token


def api_requests(client_id, access_token, endpoint, params=None):
    URL = "https://api.twitch.tv/helix/" + endpoint
    headers = {"Client-Id": client_id, "Authorization": f"Bearer {access_token}"}

    r = requests.get(url=URL, headers=headers, params=params)

    return r.json().get("data", [])


def extract():
    # Load secrets into env
    load_dotenv()
    # create key value pairs for secrets
    twitch_credentials = load_twitch_creds()
    # Post request for access token
    client_id, access_token = fetch_token(twitch_credentials)
    # Get request data
    endpoint = "streams"
    data = api_requests(client_id, access_token, endpoint)

    return data


def insertion_query():
    return """
	INSERT INTO twitch.streams (
		user_id,
		user_login,
		game_name,
		viewer_count,
		language,
		is_mature
	)
	VALUES (
		%(user_id)s,
		%(user_login)s,
		%(game_name)s,
		%(viewer_count)s,
		%(language)s,
		%(is_mature)s
	);
	"""


if __name__ == "__main__":
    print(extract())

# File to pull data from twitch API
import requests
from dotenv import load_dotenv
from auth_config import load_twitch_creds, load_warehouse_creds
from models import Streams
from database import SessionLocal


def fetch_token(twitch_credentials):
    """
    Uses twitch credentials loaded from .env to interact with OAuth2
    to receive a token for making API calls
    """
    URL = "https://id.twitch.tv/oauth2/token"
    r = requests.post(url=URL, params=twitch_credentials)

    access_token = r.json()["access_token"]

    return twitch_credentials["client_id"], access_token


def api_requests(client_id, access_token, endpoint, params=None):
    """
    Makes api calls to a given endpoint using
    passed in client_id and access_token as credentials

    Returns:
        [List]: A list of a list of dict-like key-value pairs
    """
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
    endpoint = "streams?first=100"
    data = api_requests(client_id, access_token, endpoint)

    return data


def transform(data):
    """
    Transforms requested data into model class objects
    to be added to database via sqlalchemy
    """
    streams = list()
    for entry in data:
        obj = Streams(
            user_id=entry["user_id"],
            user_login=entry["user_login"],
            game_name=entry["game_name"],
            viewer_count=entry["viewer_count"],
            language=entry["is_mature"],
        )
        streams.append(obj)

    return streams


def load(streams, session):
    """Add data to database"""
    session.add_all(streams)
    session.commit()
    return "Stream data added to database"


def execute_load(streams):
    """Interface function for data loading that abstracts the life
    of the database connection away from individual function calls.
    """
    with SessionLocal() as session:
        load(streams, session)


def main():
    data = extract()
    streams = transform(data)
    execute_load(streams)


if __name__ == "__main__":
    main()

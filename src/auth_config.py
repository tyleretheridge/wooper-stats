import os
import requests


def load_warehouse_creds():
    return {
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "db": os.getenv("POSTGRES_DB"),
        "host": os.getenv("POSTGRES_HOST"),
    }


def load_twitch_creds():
    return {
        "client_id": os.getenv("TWITCH_CLIENT_ID"),
        "client_secret": os.getenv("TWITCH_CLIENT_SECRET"),
        "grant_type": "client_credentials",
    }

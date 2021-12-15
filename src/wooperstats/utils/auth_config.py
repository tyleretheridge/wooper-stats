import os
import requests


def load_warehouse_creds():
    return {
        'user': os.getenv('WAREHOUSE_USER'),
        'password': os.getenv('WAREHOUSE_PASSWORD'),
        'db': os.getenv('WAREHOUSE_DB'),
        'host': os.getenv('WAREHOUSE_HOST'),
        'port': int(os.getenv('WAREHOUSE_PORT', 5432)),
    }


def load_twitch_creds():
    return {
        "client_id" : os.getenv("TWITCH_CLIENT_ID"),
        "client_secret" : os.getenv("TWITCH_CLIENT_SECRET"),
        "grant_type" : "client_credentials"
    }
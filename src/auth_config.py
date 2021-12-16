# src/auth_config
import os


def load_warehouse_creds():
    """
    Loads secrets from .env and returns them as a dict.
    Returns:
        dict: a dictionary of key-values for loading secrets from .env
    """
    return {
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "db": os.getenv("POSTGRES_DB"),
        "host": os.getenv("POSTGRES_HOST"),
    }


def load_twitch_creds():
    """
    Loads secrets from .env and returns them as a dict.
    Returns:
        dict: a dictionary of key-values for loading secrets from .env
    """
    return {
        "client_id": os.getenv("TWITCH_CLIENT_ID"),
        "client_secret": os.getenv("TWITCH_CLIENT_SECRET"),
        "grant_type": "client_credentials",
    }

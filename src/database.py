# src/database.py
from dataclasses import dataclass
from auth_config import load_warehouse_creds
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Class to manage return of env secrets loading
@dataclass
class Connection:
    user: str
    password: str
    db: str
    host: str


def generate_db_url():
    """
    Constructor for URL that is abstracted away from .env loading
    """
    # Get creds from env
    load_dotenv()
    conn = Connection(**load_warehouse_creds())
    return f"postgresql://{conn.user}:{conn.password}@{conn.host}/{conn.db}"


# Function that manages Session when passed as arg
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Load database URL
SQLALCHEMY_DATABASE_URL = generate_db_url()

# Create session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

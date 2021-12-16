from dataclasses import dataclass
from .auth_config import load_warehouse_creds
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
    Returns SQAlchemy URL
    """
    # Get creds from env
    load_dotenv()
    conn = Connection(**load_warehouse_creds())
    return f"postgresql://{conn.user}:{conn.password}@{conn.host}/{conn.db}"


# Load database URL

SQLALCHEMY_DATABASE_URL = generate_db_url()

# make engine with URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

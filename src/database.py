import psycopg2
from dataclasses import dataclass
from contextlib import contextmanager
from auth_config import load_warehouse_creds
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Class to manage return of env secrets loading
@dataclass
class Connection:
    user: str
    password: str
    db: str
    host: str


# # Class to construct connection URI and manage psycopg2 cursor
# class DatastoreConnection:
#     def __init__(self, conn: Connection):
#         self.connection_url = (
#             f"postgresql://{conn.user}:{conn.password}@" f"{conn.host}/{conn.db}"
#         )

#     # Deploying cursor with context manager to maintain resources
#     @contextmanager
#     def managed_cursor(self, cursor_factory=None):
#         self.conn = psycopg2.connect(self.connection_url)
#         self.conn.autocommit = True
#         self.curr = self.conn.cursor(cursor_factory=cursor_factory)
#         try:
#             yield self.curr
#         finally:
#             self.curr.close()
#             self.conn.close()

load_dotenv()
# Load database URL
conn = Connection(**load_warehouse_creds())
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{conn.user}:{conn.password}@{conn.host}/{conn.db}"
)
# make engine with URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# if __name__ == "__main__":
#     load_dotenv()
#     conn = Connection(**load_warehouse_creds())
#     SQLALCHEMY_DATABASE_URL = (
#         f"postgresql://{conn.user}:{conn.password}@{conn.host}/{conn.db}"
#     )
#     print(SQLALCHEMY_DATABASE_URL)

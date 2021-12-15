import psycopg2
from dataclasses import dataclass
from contextlib import contextmanager

# Class to manage return of env secrets loading
@dataclass
class Connection:
    user: str
    password: str
    db: str
    host: str
    port: int = 5432


# Class to construct connection URI and manage psycopg2 cursor
class DatastoreConnection:
    def __init__(self, conn:Connection):
        self.connection_url = (
            f'postgresql://{conn.user}:{conn.password}@'
            f'{conn.host}:{conn.port}/{conn.db}'
        )
    
    # Deploying cursor with context manager to maintain resources
    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.connection_url)
        self.conn.autocommit = True
        self.curr = self.conn.cursor(cursor_factory=cursor_factory)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.conn.close()
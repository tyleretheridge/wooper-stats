import datetime as dt
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.sql.schema import Column
from database import Base


class Streams(Base):
    __tablename__ = "streams"

    user_id = Column(String, primary_key=True)
    user_login = Column(String, nullable=False)
    game_name = Column(String, nullable=False)
    viewer_count = Column(Integer, nullable=False)
    language = Column(String, nullable=False)
    is_mature = Column(Boolean, nullable=False)
    date = Column(DateTime, default=dt.datetime.utcnow)

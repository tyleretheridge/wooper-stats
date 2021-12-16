import datetime as dt
from pydantic import BaseModel


class StreamRequest(BaseModel):
    user_id: str
    user_login: str
    game_name: str
    viewer_count: int
    language: str
    stream_date: dt.datetime

    class Config:
        orm_mode = True

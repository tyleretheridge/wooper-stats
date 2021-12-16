import datetime as dt
from pydantic import BaseModel


class StreamRequest(BaseModel):
    user_id: str
    user_login: str
    game_name: str
    viewer_count: int
    language: str
    is_mature: bool
    datetime: dt.datetime

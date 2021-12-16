from .schema import StreamRequest
from .database import get_db
from sqlalchemy.orm import Session
from .models import Streams
from fastapi import FastAPI, Depends

app = FastAPI()


@app.post("/")
def create(details: StreamRequest, db: Session = Depends(get_db)):
    to_create = StreamRequest(
        user_id=details.user_id,
        user_login=details.user_login,
        game_name=details.game_name,
        viewer_count=details.viewer_count,
        language=details.language,
        is_mature=details.is_mature,
        datetime=details.datetime,
    )
    db.add(to_create)
    db.commit()
    return {"success": True, "created_id": to_create.user_id}


@app.get("/")
def ret():
    return "Hello World"

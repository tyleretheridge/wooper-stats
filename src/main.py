# src/main.py
import schema
import database
import services
from sqlalchemy.orm import Session
from models import Streams
from fastapi import FastAPI, Depends, HTTPException
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from sqlalchemy.orm import Session

# Create app
app = FastAPI()


# Define routes
@app.post("/api/streams/", response_model=schema.StreamRequest)
async def add_stream(
    stream_details: schema.StreamRequest, db: Session = Depends(database.get_db)
):

    return await services.add_stream(stream_details=stream_details, db=db)


@app.get("/api/streams/", response_model=List[schema.StreamRequest])
async def get_all_streams(db: Session = Depends(database.get_db)):
    return await services.get_all_streams(db)


@app.get("/api/streams/{user_id}/", response_model=schema.StreamRequest)
async def get_stream(user_id: str, db: Session = Depends(database.get_db)):
    stream = await services.get_stream(user_id=user_id, db=db)
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")

    return await services.get_stream(user_id=user_id, db=db)


@app.delete("/api/streams/{user_id}/")
async def delete_stream(user_id: str, db: Session = Depends(database.get_db)):
    stream = await services.get_stream(user_id=user_id, db=db)
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")

    await services.delete_stream(stream, db=db)

    return "Successfully removed stream records"

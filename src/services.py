# src/services.py
import models
import schema
from typing import TYPE_CHECKING, List
import database

# Useful for enforcing types across async functions
if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def add_tables():
    """
    Generates tables in postgres database according to SQLAlchemy
    model when this script is invoked directly via terminal.
    """
    return database.Base.metadata.create_all(bind=database.engine)


# Async functions that correspond to routes in main.py
async def add_stream(
    stream_details: schema.StreamRequest, db: "Session"
) -> schema.StreamRequest:
    stream_details = models.Streams(**stream_details.dict())
    db.add(stream_details)
    db.commit()
    db.refresh(stream_details)
    return schema.StreamRequest.from_orm(stream_details)


async def get_all_streams(db: "Session") -> List[schema.StreamRequest]:
    streams = db.query(models.Streams).all()
    return list(map(schema.StreamRequest.from_orm, streams))


async def get_stream(user_id: str, db: "Session"):
    stream = db.query(models.Streams).filter(models.Streams.user_id == user_id).first()
    return stream


async def delete_stream(stream: models.Streams, db: "Session"):
    db.delete(stream)
    db.commit()


if __name__ == "__main__":
    add_tables()

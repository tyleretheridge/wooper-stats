from typing import TYPE_CHECKING, List

import database
import models
import schema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def add_tables():
    return database.Base.metadata.create_all(bind=database.engine)


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

import database
import models
from dotenv import load_dotenv


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)


if __name__ == "__main__":
    load_dotenv()
    create_database()

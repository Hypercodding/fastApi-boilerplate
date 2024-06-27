from .database import SessionLocal, engine, Base

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


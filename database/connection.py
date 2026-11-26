from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql+psycopg://fraudstream:fraudstream@localhost:5433/fraudstream"

engine = create_engine(DATABASE_URL)

session_local = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
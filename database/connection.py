from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://fraudstream:fraudstream@localhost:5433/fraudstream"

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    print("Database connected!")
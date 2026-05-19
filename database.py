# This file handles the connection to the database. In this case, it's a SQLite DB.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DBModelBase

DATABASE_URL = "sqlite:///smartinventory.db"

engine = create_engine(DATABASE_URL)
DBModelBase.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


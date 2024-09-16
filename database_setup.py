from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection string (use SQLite for simplicity)
DATABASE_URL = "sqlite:///concerts.db"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured session class
Session = sessionmaker(bind=engine)
session = Session()

# Base class for declarative models
Base = declarative_base()

def init_db():
    Base.metadata.create_all(engine)

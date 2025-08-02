from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://postgres:test1234@localhost:5432/kpa_backend"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ This is the missing function
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from app.database import Base, engine
from app.models import PersonalInfo

# Table create
Base.metadata.create_all(bind=engine)

app = FastAPI()

from app.routers import user, personal_info  # import routers after DB setup


app = FastAPI()

app.include_router(user.router)
app.include_router(personal_info.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI is working fine!"}

# Create DB tables
Base.metadata.create_all(bind=engine)

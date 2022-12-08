from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Username as SchemaUsername
from dotenv import load_dotenv
import os

from models import Username
from fastapi_sqlalchemy import DBSessionMiddleware, db

load_dotenv(".env")

app = FastAPI()

origins = [
    "http://localhost",
    "http://http://192.168.56.5:8085"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.post("/add-username",response_model=SchemaUsername)
def add_student(Username:SchemaUsername):
    db_username = Username(name=Username.name)
    db.session.add(db_username)
    db.session.commit()
    return db_username

@app.get("/username/")
def get_username():
    username = db.session.query(Username).all()
    return username


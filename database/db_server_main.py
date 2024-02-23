from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated
from sqlalchemy.orm import Session
import models as models
from database import engine
from models import User
from db_connection import get_db
from requestsPyda_db import RequestRegister, RequestLog

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

user_logged = {}

@app.get("/")
async def root():
    return {"message": "DB is up and running!"}


@app.post("/login_query/")
async def login(user: RequestLog, db: Annotated[Session, Depends(get_db)]):
    global user_logged
    db_user = models.User(**user.dict())
    db_user.email = db_user.email.lower()
    user_courser = db.query(User).filter(User.email == db_user.email, User.password == db_user.password).first()
    if user_courser is not None:
        user_logged = user_courser
        return {"user" : user_logged}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
@app.post("/register_query/")
async def register(user : RequestRegister, db: Annotated[Session, Depends(get_db)]):
    db_user = models.User(**user.dict())
    db_user.email = db_user.email.lower()
    try:
        db.add(db_user)
        db.commit()
        return {"message" : f"user {db_user.username} created successfully"}
    except:
        return {"message" : "Email is already in use"}
    
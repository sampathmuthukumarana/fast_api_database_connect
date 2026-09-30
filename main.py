from fastapi import FastAPI
from sqlalchemy import select

import models
from schemas import UserCreate, UserResponse
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db

app = FastAPI()


# @app.get("/")
# async def get_users(db:Session = Depends(get_db)):
#     # return {"message": "Hello World"}
#       return db.query(User).all()

@app.get("/")
async def get_root():
    return {"message": "Hello World"}

@app.post("/user", response_model=UserResponse)
async def create_user(payload: UserCreate, database: Session = Depends(get_db)):
  new_user = models.User(**payload.model_dump())
  database.add(new_user)
  database.commit()

  return new_user

@app.get("/users", response_model=list[UserResponse])
async def get_all_users(database: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return  database.scalars(select(models.User).offset(skip).limit(limit)).all()


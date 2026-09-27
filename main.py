from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import get_db

app = FastAPI()


# @app.get("/")
# async def get_users(db:Session = Depends(get_db)):
#     # return {"message": "Hello World"}
#       return db.query(User).all()
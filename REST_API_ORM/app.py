from database import *
from fastapi import FastAPI
from models import*
app = FastAPI()
from sqlalchemy.orm import*


app = FastAPI(title="CRUD Application")

@app.get("/")
def root():
    return {"message": "Your app is running"}

def get_db():
    db=SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Error:",e)
    finally:
        db.close()


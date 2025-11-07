#Connect to database user sqlalchemy(ORM)
from sqlalchemy import *
from fastapi import *
app = FastAPI()

import os
from dotenv import load_dotenv

load_dotenv()

DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_NAME=os.getenv("DB_NAME")

app=FastAPI(title="CRUD APPILICATION")


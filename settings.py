import sqlite3
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()


engine = create_engine('postgresql://docker:postgresql@localhost:5432/translator')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


ALGORITHMS = "HS256"
JWT_SECRET = "5a43b01a6e1e22d7b945cd5b4158dbf5e9e4e7fa68f87a8dafe26f73d291d7f"

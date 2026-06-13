from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

from database import get_db

app = FastAPI()

@app.get('/')
def home():
    return {'data':{"message": 'Hello World'}} 

@app.get('/user')
def getUser ():
    return {'data': {'name': 'Masham'}}

@app.post('/product')
def addproduct():
    return {'data': {'Name': 'Table'}}

@app.get("/connection")
def db_connection(db: Session = Depends(get_db)):
    return {"message": "MySQL Connected Successfully"}
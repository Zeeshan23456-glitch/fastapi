from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data':{"message": 'Hello World'}} 

@app.get('/user')
def getUser ():
    return {'data': {'name': 'Masham'}}
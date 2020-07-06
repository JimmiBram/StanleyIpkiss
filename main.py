#Start this app using "uvicorn main:app --reload"
#Tutorial on fastapi here: https://fastapi.tiangolo.com/tutorial/first-steps/

from sibase.SiApi import SIApi as api
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
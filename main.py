#Start this app using "uvicorn main:app --reload"
#Tutorial on fastapi here: https://fastapi.tiangolo.com/tutorial/first-steps/

from sibase import si_api as api
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
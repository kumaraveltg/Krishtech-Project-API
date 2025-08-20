
from fastapi import FastAPI 
from app import db,models
app = FastAPI()

@app.get("/")
async def index():
    return{"message:" "Hi Kumar"} 

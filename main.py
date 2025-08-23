from fastapi import FastAPI
from app import models, db, api
from sqlmodel import SQLModel
from app.db_sqlmodel import engine,get_session
from app.users import router as users_router



app = FastAPI()

# Create tables at startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# include routers
app.include_router(api.router)
app.include_router(users_router)

# Sample root endpoint
# @app.get("/")
# async def index():
#     return {"message": "Hi Kumar"}

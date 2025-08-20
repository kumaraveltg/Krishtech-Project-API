from fastapi import FastAPI
from app import models, db, api

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=db.engine)

# include routes
app.include_router(api.router)

# @app.get("/")
# async def index():
#     return{"message:" "Hi Kumar"} 

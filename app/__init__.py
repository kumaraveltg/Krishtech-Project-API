# __init__.py
from .db import engine, Base
from .models import User, Role
Base.metadata.create_all(bind=engine)
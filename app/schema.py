# from pydantic import BaseModel
# from . import db

# class UserCreate(BaseModel):
#     username: str
#     password: str
#     firstname: str
#     userrolesid: int
#     active: bool

from pydantic import BaseModel
from . import models, db
from . import schema

# ----------------------------
# Role schemas
# ----------------------------
class RoleBase(BaseModel):
    rolename: str
    active: bool

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    #userrolesid: int

    class Config:
        from_attributes = True


# ----------------------------
# User schemas
# ----------------------------
class UserBase(BaseModel):
    username: str
    firstname: str | None = None
    active: bool

class UserCreate(UserBase):
    password: str
    userrolesid: list[int]  # since in your model it's ARRAY(Integer)

class User(UserBase):
    usersid: int
    userrolesid: list[int]

    class Config:
        from_attributes = True


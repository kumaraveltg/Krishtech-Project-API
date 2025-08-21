from pydantic import BaseModel
from . import models, db
from . import schema
from typing import Optional

# ----------------------------
# Role schemas
# ----------------------------
class RoleBase(BaseModel):
    rolename: str
    active: bool

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    userrolesid: int
    rolename: str
    active: bool
    createdby: str
    modifiedby: str

class UpdateRole(RoleBase):
    rolename: str
    active: bool
    modifiedby: str
    cancel: Optional[str] = None

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


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select,SQLModel,Field,Column,JSON
from .db_sqlmodel import engine, get_session
from sqlalchemy.dialects.postgresql import ARRAY, INTEGER,JSONB
from pydantic import EmailStr,validator
from typing import List, Optional,Dict, Any
from datetime import datetime
from pydantic import BaseModel

class Puser(BaseModel):
    createdby: str = Field(nullable=False)
    modifiedby: str = Field(nullable=False)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)
    firstname: Optional[str] = None
    emailid: Optional[EmailStr] = None
    userroleids: Optional[List[int]] = None
    active: bool = True 
    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda v: v.strftime("%d/%m/%Y %H:%M:%S") if v else None
        }
    }


    @validator("createdby", "modifiedby","username" )
    def must_not_be_empty(cls, v):
     if not v or not v.strip():
        raise ValueError("This field is required")
     return v
    @validator("userroleids")
    def roles_must_not_be_empty(cls, v):
        if v is None or not v:
            raise ValueError("userroleids must not be empty")
        return v
   
router = APIRouter()

 

class Kusers(SQLModel, table=True):
    __table_args__ = {"extend_existing": True} 
    id: int | None = Field(default=None, primary_key=True)
    cancel: str ="F"
    createdby: str = Field(nullable=False)
    #createdon: datetime = Field(default_factory=datetime.now) 
    createdon: str = Field(default_factory=lambda: datetime.now().strftime("%d/%m/%y %H:%M:%S"))
    modifiedby: str= Field(nullable=False)
    modifiedon: str = Field(default_factory=lambda: datetime.now().strftime("%d/%m/%y %H:%M:%S"))
    username: str = Field(index=True,nullable=False)
    password: str
    firstname: Optional[str]=None
    emailid: Optional[EmailStr]= None
    userroleids: Optional[List[int]] = Field(
        sa_column=Column(ARRAY(INTEGER))
    )
    active: bool = True  # default value
    
  

# ✅ Create user
@router.post("/users/", response_model=Puser)
def create_user(user: Puser):
    with Session(engine) as session:
        db_user = Kusers(**user.dict())  # convert Puser → Kusers
        existing_user = session.exec(
            select(Kusers).where(Kusers.username == user.username)
        ).first()

        if existing_user:
         raise HTTPException(status_code=400,detail="Username already Exist")
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return Puser.from_orm(db_user)

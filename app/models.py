from sqlalchemy import Column,Integer,String,ARRAY,Boolean,DateTime,func,text
from .db import Base

class UserRole(Base) :
  __tablename__ = "userroles"

  userrolesid = Column(Integer, primary_key=True,index=True)
  cancel = Column(String,default ="F")
  createdby=  Column(String,nullable=True)
  createdon= Column(DateTime,default=func.now() ,nullable=True) 
  modifiedby=Column(String,nullable=True)
  modifieon=Column(DateTime,default=func.now(),onupdate=func.now(),nullable=True) 
  rolename = Column(String,nullable=True)
  active = Column(Boolean,default=False,nullable=False)
 



class User(Base) :
    __tablename__ = "users"

    usersid = Column(Integer, primary_key=True, index=True)
    cancel = Column(String,default ="F")
    createdby=  Column(String,nullable=True)
    createdon= Column(DateTime,default=func.now(),nullable=True) 
    modifiedby=Column(String,nullable=True)
    modifieon=Column(DateTime,default=func.now(),onupdate=func.now(),nullable=True) 
    username = Column(String, index=True)
    firstname = Column(String, nullable=True)
    userrolesid = Column(ARRAY(Integer))
    active = Column(Boolean,default=False,nullable=False)
    password = Column(String(128))
    
    #Base.metadata.create_all(bind=engine)
    
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from . import  schema, db,models
from . models import UserRole
from typing import List

router = APIRouter()

@router.post("/userroles/", response_model=schema.Role)
def create_role(role: schema.RoleCreate, session: Session = Depends(db.get_db)):

    db_role = session.query(models.UserRole).filter(models.UserRole.rolename == role.rolename).first()
    if db_role:
        raise HTTPException(status_code=400,detail="Role Name Already Exists")
    new_role = models.UserRole(
        rolename=role.rolename,
        active=role.active
    )
    session.add(new_role)
    session.commit()
    session.refresh(new_role)
    return new_role

@router.get("/userrole/{userrolesid}")
def read_userroles(userrolesid :int,db: Session=Depends(db.get_db)):
    db_userroles = db.query(UserRole).filter(UserRole.userrolesid == userrolesid).first()
    if db_userroles is None:
        raise HTTPException(status_code=404, detail="User Role not found")
    return db_userroles
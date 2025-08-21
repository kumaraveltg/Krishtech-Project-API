from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from . import  schema, db,models,global_dict_parameters
from . models import UserRole
from typing import List

router = APIRouter()

@router.post("/userroles/", response_model=schema.Role)
def create_role(role: schema.RoleCreate, session: Session = Depends(db.get_db),
                globals: dict = Depends(global_dict_parameters.global_only_user)):

    db_role = session.query(models.UserRole).filter(models.UserRole.rolename == role.rolename).first()
    if db_role:
        raise HTTPException(status_code=400,detail="Role Name Already Exists")
    new_role = models.UserRole(
        rolename=role.rolename,
        active=role.active,
        createdby=globals["createdby"],
        modifiedby=globals["modifiedby"]
    )
    session.add(new_role)
    session.commit()
    session.refresh(new_role)
    return new_role
#User Role specific Records
@router.get("/userrole/{userrolesid}")
def read_userroles(userrolesid :int,db: Session=Depends(db.get_db)):
    db_userroles = db.query(UserRole).filter(UserRole.userrolesid == userrolesid).first()
    if db_userroles is None:
        raise HTTPException(status_code=404, detail="User Role not found")
    return db_userroles
# User Role All records
@router.get("/userrole/", response_model=List[schema.Role])
def read_all_userroles(db: Session = Depends(db.get_db)):
    db_userroles_all = db.query(UserRole).all()
    return db_userroles_all
@router.delete("/userrole/{userrolesid}",response_model=List[schema.Role])
def delete_userroles(userrolesid: int, db: Session= Depends(db.get_db)):
    db_delete_userrole = db.query(models.UserRole).filter(models.UserRole.userrolesid == userrolesid).first()
    if not db_delete_userrole:
        raise HTTPException(status_code=404, detail="User Role Not Available")
   
    Default_roles = "default"

    if db_delete_userrole.rolename.lower() in Default_roles:
          raise HTTPException(status_code=404, detail="You can't Delete this Userrole")
    
    db.delete(db_delete_userrole)
    db.commit()
    return {"message":f"User Role Successfully Deleted"}

@router.put("/userrole/{userroleid}",response_model=schema.UpdateRole)
def update_userrole(userroleid: int,update_role:schema.UpdateRole,db: Session=Depends(db.get_db)):
    db_update_userrole= db.query(models.UserRole).filter(models.UserRole.userrolesid == userroleid).first()
    if not db_update_userrole:
        raise HTTPException(status_code=404, detail="User Role not found")
    db_update_userrole.rolename= update_role.rolename
    db_update_userrole.active = update_role.active
    db_update_userrole.modifiedby = update_role.modifiedby
    db.add(db_update_userrole)
    db.commit()
    db.refresh(db_update_userrole)
    return db_update_userrole
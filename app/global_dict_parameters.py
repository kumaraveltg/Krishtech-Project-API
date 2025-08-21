from fastapi import Depends, Header

def get_global_params(
    username: str = Header(...),
    userrole: str = Header(...),
):
    return {
        "username": username,
        "userrole": userrole,
        "createdby": username,
        "modifiedby": username,
    }

def global_only_user(username: str = Header(...)):
    return{
        "username": username,
        "createdby": username,
        "modifiedby": username
    }
from fastapi import FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from utils.hashVerify import hash
from database.models import create_user, chech_if_username_exist, check_if_email_exist
# from ..utils.oauth2 import get_current_user, verify_access_token
from typing import Dict



def create_a_user(db: Session, username:str=None, email:str=None, password:str=None, role:str=None, iban:str=None):
    username_check = chech_if_username_exist(db=db, username=username)
    email_check = check_if_email_exist(db=db, email=email)
    
    hashed_password = hash(password)
    password = hashed_password
    
    if username_check is not None:
       raise HTTPException(status_code=400, detail= "Username already exist!")
    elif email_check is not None:
        raise HTTPException(status_code=404, detail= "Email already exist!")
    else:
        data = create_user(db=db, username=username, email=email, password=password, role=role, iban=iban)
    
        return {
            "status":True,
            "message": "Success",
            "data": data
        }
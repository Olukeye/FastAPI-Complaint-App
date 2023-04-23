from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from module.users import create_a_user, get_users_or_by_email, asign_a_role_to_user
from utils.oauth2 import get_current_user, is_complainer, if_user_is_admin
from schemas.users import CreateUserModel, UserOut, AsignRoleModel
from schemas.response_models import ResponseModel, UserResponseModel
from database.db import  get_db
from models.enums import RoleType, Enum


router = APIRouter(tags = ['Users'])



@router.get('/search',  status_code=200,response_model=ResponseModel)
async def search_user(db:Session=Depends(get_db), user:int=Depends(if_user_is_admin)):
    return get_users_or_by_email(db=db)

@router.post("/register", status_code=201,response_model=ResponseModel)
async def register(field:CreateUserModel, db:Session = Depends(get_db)):
    return create_a_user(db=db, username=field.username, email=field.email, password=field.password, role=field.role, iban=field.iban)

@router.put('/asignRole/{id}', status_code=200,response_model=ResponseModel)
async def asign_role(role:AsignRoleModel, id:int, db:Session = Depends(get_db), user:int=Depends(if_user_is_admin)):
    return asign_a_role_to_user(db=db, id=id, role=role, values=dict(role))



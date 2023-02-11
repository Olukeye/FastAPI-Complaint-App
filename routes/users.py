from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from module.users import create_a_user
from schemas.users import CreateUserModel
from schemas.response_models import ResponseModel
from database.db import  get_db

router = APIRouter(tags = ['Users'])



@router.post("/register", status_code=201,response_model=ResponseModel)
async def register(field:CreateUserModel, db:Session = Depends(get_db)):
    return create_a_user(db=db, username=field.username, email=field.email, password=field.password, role=field.role, iban=field.iban)

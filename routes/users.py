from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from module.users import create_a_user
from schemas.users import CreateUserModel
from Pydantic_schemas.response_models import ResponseModel
from database.db import  get_db

router = APIRouter(tags = ['Users'])



@router.post("/user", response_model=ResponseModel)
async def create_new_user(user:CreateUserModel, db:Session = Depends(get_db)):
    return create_a_user(db=db, username=user.username, email=user.email, password=user.password, role=user.role, iban=user.iban)

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from utils.oauth2 import get_current_user
from module.complaints import create_a_complaint
from schemas.complaints import CreateComplaintModel
from schemas.response_models import ResponseModel
from database.db import  get_db

router = APIRouter(tags = ['Compaints'])


@router.post('/complainer', status_code=201,response_model=ResponseModel)
async def create_new_complainer(field:CreateComplaintModel,  db:Session = Depends(get_db), user: int = Depends(get_current_user)):
    return create_a_complaint(db=db, title=field.title, user=user, description=field.description, image=field.image, amount=field.amount, status=field.status)

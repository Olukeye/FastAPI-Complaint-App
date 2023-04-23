from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from utils.oauth2 import get_current_user, is_complainer, if_user_is_admin
from module.complaints import create_a_complaint, user_complaint_status, get_complaints, delete_a_complaint, approve_complint
from schemas.complaints import CreateComplaintModel, ApproveModel
from schemas.response_models import ResponseModel
from database.db import  get_db

router = APIRouter(tags = ['Compaints'])


@router.get('/allcomplaints', status_code=200, response_model=ResponseModel)
async def all_complaints(db:Session = Depends(get_db), user= Depends(if_user_is_admin)):
    return get_complaints(db=db)


@router.post('/createComplain', status_code=201,response_model=ResponseModel)
async def create_new_complainer(field:CreateComplaintModel,  db:Session = Depends(get_db), user = Depends(get_current_user), me=Depends(is_complainer)):
    return create_a_complaint(db=db, title=field.title, user=user, description=field.description, image=field.image, amount=field.amount, status=field.status)

@router.get('/personalComplaint', status_code=200, response_model=ResponseModel)
async def user_complaint( db:Session = Depends(get_db), user:int=Depends(get_current_user)):
    return user_complaint_status(db=db, user=user)

@router.put('/complaint/{id}',status_code=200, response_model=ResponseModel)
async def approve_or_reject_complaint(field:ApproveModel, id:int, db: Session=Depends(get_db), user:int=Depends(if_user_is_admin)):
    return approve_complint(db=db, id=id, status=status, values=dict(field))

@router.delete('/deleteComplaint/{id}', status_code=200, response_model=ResponseModel)
async def delet_complaint(id:int, db: Session=Depends(get_db), user:int=Depends(if_user_is_admin)):
    return delete_a_complaint(db=db, user=user, id=id)
from fastapi import FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from database.models import create_complainer, complaints_status, get_all_complaints, delete_complaint
from models.enums import State
from typing import Dict


def get_complaints(db: Session):
    info = get_all_complaints(db=db)
    return {
        "status":True,
        "message": "Success",
        "data":info
    }


def user_complaint_status(db: Session, user:int):
    info = complaints_status(db=db,user=user)
    return {
        "status":True,
        "message": "Success",
        "data":info
    }
    
def create_a_complaint(db:Session, title:str=None, user:int=0, customer_id:int=None, description:str=None, image:str=None, amount:int=0, status:str=None):
    info = create_complainer(db=db, title=title,user=user, description=description, image=image, amount=amount, status=status)
    
    return {
        "status":True,
        "message": "Success",
        "data":info
    }
    
def delete_a_complaint(db:Session, user:int, id:int):
   info = delete_complaint(id=id, user=user, db=db)
   
   return {
        "status":True,
        "message": "User Deleted Successfully",
        "data":info
    }
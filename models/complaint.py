from sqlalchemy import Column, BigInteger, Integer,  String, Float, ForeignKey
from sqlalchemy.orm import Session, relationship
from database.db import get_db, Base, create_customised_datetime
from typing import Dict
from models.enums import State, Enum


class Complaint(Base):
    __tablename__ = 'complaints'
    id = Column(BigInteger, primary_key=True, nullable=False)
    customer_id = Column(ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(State), default=State.pending.name)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
    user = relationship("User")
    
    
def get_all_complaints(db:Session):
    all_complaints = db.query(Complaint).all()
    return all_complaints
    
def create_complainer(db:Session, title:str=None, description:str=None, image:str=None, amount:int=0, status:str=None, user:int=0):
    new_complainer = Complaint(title=title, description=description, image=image, amount=amount, status=status, created_at=create_customised_datetime(), user=user,updated_at=create_customised_datetime())
    
    db.add(new_complainer)
    db.commit()
    db.refresh(new_complainer)
    
    return new_complainer

def complaints_status(db:Session, user:int):
    get_complaints_status = db.query(Complaint).filter(Complaint.customer_id == user.id).all()
    
    return get_complaints_status

def delete_complaint(id:int, user:int,  db:Session):
    del_complaint = db.query(Complaint).filter(Complaint.id == id)
    
    destroy = del_complaint.first()
    del_complaint.delete()
    db.commit()
    
    return  destroy

def approve_a_complaint(id:int, db:Session, status:str=Enum(State),values:Dict={}):
    approver = db.query(Complaint).filter(Complaint.id == id).values()
    
    db.commit()
    
    return approver
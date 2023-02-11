from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import Session
from database.db import Base, create_customised_datetime
from typing import Dict
from models.enums import RoleType, Enum



class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)
    role = Column(Enum(RoleType), default=RoleType.complainer, nullable=False)
    iban = Column(String, nullable=True)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
    
    
def check_if_email_exist(db:Session, email:str=None):
    check_email = db.query(User).filter(User.email == email).first()
    
    return check_email
    
def chech_if_username_exist(db:Session, username:str=None):
    check_username = db.query(User).filter(User.username == username).first()
    
    return check_username
    
def create_user(db: Session, username:str=None, email:str=None, password:str=None, role:str=None, iban:str=None):
    new_user = User(username=username, email=email, password=password, role=role, iban=iban, created_at=create_customised_datetime(),updated_at=create_customised_datetime())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    

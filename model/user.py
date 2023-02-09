from sqlalchemy import Column, BigInteger, Integer, Boolean, String, SmallInteger
from sqlalchemy.orm import Session
from database.db import get_db, Base, get_session, create_customised_datetime
from typing import Dict
from enums import RoleType



class User(Base):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, nullable=False)
    username = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)
    role = Column(Enum(RoleType), server_default=RoleType.complainer.name, nullable=True)
    iban = Column(String)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
    
    

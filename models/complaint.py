from sqlalchemy import Column, BigInteger, Integer,  String, Float, ForeignKey
from sqlalchemy.orm import Session
from database.db import get_db, Base, create_customised_datetime
from typing import Dict
from enums import State


class Complaint(Base):
    __tablename__ : 'complaints'
    id = Column(BigInteger, primary_key=True, nullable=False)
    customer_id = Column(ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(Enum(State), server_default=State.pending.name)
    created_at = Column(String, nullable=True)
    updated_at = Column(String, nullable=True)
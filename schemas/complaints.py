from pydantic import BaseModel,EmailStr, constr
from database.db import create_customised_datetime
from pydantic.types import conint
from decimal import Decimal
from typing import Optional
from models.enums import  State


class Complaint(BaseModel):
    title: Optional[str]=None
    description: Optional[str] = None
    image: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[State] = None
    
    
class CreateComplaintModel(Complaint):
     pass
 
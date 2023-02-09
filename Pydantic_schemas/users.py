from pydantic import BaseModel,EmailStr, constr
from database.db import create_customised_datetime
from pydantic.types import conint
from decimal import Decimal
from typing import Optional



class User(BaseModel):
    username: str
    email: str
    password:str
    role: Optional[str]
    iban: Optional[str]=None
    
class CreateUserModel(User):
     pass
 
 
# class UserOption(BaseModel):
#     id:int
#     username: str
#     email: str
#     pin: str
#     user_type: str
#     status: int
    
#     class Config:
#         orm_mode = True
  
  
  
# class UpdateUserModel(BaseModel):
#     username: Optional[str] = None
#     email: Optional[str] = None
#     password: Optional[str] = None
#     pin: Optional[str] = None
#     user_type: Optional[str] = None
#     status: Optional[int] = None
#     created_at: Optional[str] = None
#     updated_at: Optional[str] = None
    
#     class Config:
#         orm_mode = True
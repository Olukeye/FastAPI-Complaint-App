from pydantic import BaseModel,EmailStr, constr
from database.db import create_customised_datetime
from pydantic.types import conint
from decimal import Decimal
from typing import Optional
from models.enums import  RoleType

class User(BaseModel):
    username: Optional[str]=None
    email: str
    password: str
    role: Optional[RoleType] 
    iban: Optional[str]=None
class CreateUserModel(User):
     pass
 
class UserOut(BaseModel):
    id:int
    username: str
    email: str
    role: RoleType
    iban: str
    class Config:
        orm_mode = True
  
class UpdateUserModel(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    updated_at: Optional[str] = None
    class Config:
        orm_mode = True
        
class AsignRoleModel(BaseModel):
    role:RoleType
    class Config:
        orm_mode = True
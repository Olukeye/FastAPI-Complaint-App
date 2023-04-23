from typing import Dict, Optional, Any
from pydantic import BaseModel
from schemas.users import UserOut


class ResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[Any] = None
    
class UserResponseModel(UserOut):
    status: bool
    message: str
    data: Optional[str] = None
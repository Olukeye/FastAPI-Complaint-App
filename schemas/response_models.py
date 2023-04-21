from typing import Dict, Optional, Any
from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[Any] = None
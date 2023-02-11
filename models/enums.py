import enum
from sqlalchemy import Enum
# from enum import Enum


class RoleType(str, enum.Enum):
    approver = "approver"
    complainer = "complainer"
    admin = "admin"
    
    
class State(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
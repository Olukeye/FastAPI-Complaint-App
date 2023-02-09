from enum import Enum, unique

@unique
class RoleType(Enum):
    approver = "approver"
    complainer = "complainer"
    admin = "admin"
    
    
class State(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
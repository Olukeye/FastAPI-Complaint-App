from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from schemas.token import TokenData
from sqlalchemy.orm import Session
from models.users import User
from database.db import get_db
from settings.config import load_env_config
from models.enums import RoleType, State


env_var = load_env_config()



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = env_var['secret_key']
ALGORITHM = env_var['algorithm']
ACCESS_TOKEN_EXPIRE_MINUTE = env_var['access_token_expire_minute']

# Login access for registered user
def access_token(data: dict):
    to_encode = data.copy()

    expireIn = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTE))
    to_encode.update({"exp": expireIn})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt

def verify_access_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id = payload.get("users_id")

        if not id:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data

# Verify a user if logged in before they can perform any action
def get_current_user(token = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Time Out!.Re-Login Please", headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)

    user = db.query(User).filter(User.id == token.id).first()

    return user

# What is the status of a user
def get_user_status(current_user: User = Depends(get_current_user)):
    if not current_user.role:
            raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def is_complainer(current_user: User = Depends(get_user_status)):
    if not current_user.role == RoleType.complainer:
            raise HTTPException(status_code=400, detail="Only a complainer is allowed to create a ticket")
    return current_user

def is_approver(current_user: User = Depends(get_user_status)):
    if not current_user.role == RoleType.approver:
            raise HTTPException(status_code=400, detail="Only a approver is allowed to create a ticket")
    return current_user


def if_user_is_admin(current_user: User = Depends(get_user_status)):
    if not current_user.role == RoleType.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You have no permission")
    
    return current_user
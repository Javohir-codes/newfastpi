from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models
from app.database import get_db

SECRET_KEY = "super_puper_secret_key"
ALGORITHM = "HS256"

ACCSESS_TOKEN_EXPIRE_MINS = 30

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login") 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCSESS_TOKEN_EXPIRE_MINS)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise credentials_exception
        
        return user_id
    except JWTError:
        raise credentials_exception
    
def get_current_user(
        token: str = Depends(oauth2_schema),
        db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW_Authenticate": "Bearer"}
    )

    user_id = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user is None:
        raise credentials_exception
    
    return user
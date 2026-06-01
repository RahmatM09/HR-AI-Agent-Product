from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User

bearer_scheme = HTTPBearer()

credintials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credintials",
    headers={"WWW-Authenticate": "Bearer"}
)

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), 
        db: Session = Depends(get_db)
    ) -> User:
    token = credentials.credentials

    payload = decode_access_token(token)

    email = payload.get("sub")

    if email is None:
        raise credintials_exception
    
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise credintials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDEN,
            detial="This account is inactive."
        )
    
    return user

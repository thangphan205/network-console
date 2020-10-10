import jwt
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jwt import PyJWTError
from starlette.status import HTTP_403_FORBIDDEN

from crud.crud_users import get_user, get_user_by_id
from schemas.users import User
from schemas.token import TokenPayload
from settings import settings
from db.database import get_db
from models import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/account")


def get_current_user(
    db: Session = Depends(get_db), token: str = Security(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
    user = get_user(db, username=token_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def get_current_active_user(current_user: models.Users = Security(get_current_user)):
    # if not crud.user.is_active(current_user):
    #     raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_user_admin(
    db: Session = Depends(get_db), token: str = Security(oauth2_scheme)
):

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

    user = get_user_by_id(db, id=token_data.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.user_role < 100:
        raise HTTPException(
            status_code=404, detail="The user doesn't have enough privileges"
        )
    return user

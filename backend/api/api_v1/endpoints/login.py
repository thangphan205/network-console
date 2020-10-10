from datetime import datetime, timedelta
from sqlalchemy.orm import Session

import jwt
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from schemas.users import User
from schemas.token import Token, TokenData
from api.utils import security
from crud import crud_users
from settings import settings
from db.database import get_db
from loguru import logger

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/account")


def authenticate_user(db_session: Session, username: str, password: str):
    user = crud_users.get_user(db_session, username)
    if not user:
        return False
    if not crud_users.verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=600)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


@router.post("/login/account", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Incorrect username or password",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )

        logger.warning("user {} log in FAIL.".format(form_data.username))
        return {
            "status": False,
            "access_token": "",
            "token_type": "bearer",
        }

    currentAuthority = "user"
    if user.user_role == 100:
        currentAuthority = "admin"
    elif user.user_role == 50:
        currentAuthority = "operator"
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "username": user.username,
            "id": user.id,
            "user_id": user.id,
            "user_role": user.user_role,
            "is_active": user.is_active,
            "department": user.department,
            "ipaddress": user.ipaddress,
            "status": "ok",
            "type": "account",
            "currentAuthority": currentAuthority,
        },
        expires_delta=access_token_expires,
    )
    logger.info("user {} log in SUCCESS.".format(form_data.username))
    return {"access_token": access_token, "token_type": "bearer", "status": True}

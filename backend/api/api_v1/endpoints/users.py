from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.encoders import jsonable_encoder

from crud import crud_users
from schemas.users import (
    User,
    UserCreate,
    UserCurrent,
    Users,
    UserUpdate,
    UserUpdatePassword,
)
from db.database import SessionLocal, engine, get_db
from api.utils.security import (
    get_current_user,
    get_current_active_user,
    get_current_user_admin,
)
from models import models
from loguru import logger

router = APIRouter()


@router.post("/", response_model=User)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user_admin),
):
    db_user = crud_users.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    result = crud_users.create_user(db=db, user=user)
    if result:
        logger.info(
            "{} create user {} - role {} SUCCESS.".format(
                current_user.username, result.username, result.user_role
            )
        )
        return {
            "success": True,
            "data": result,
            "message": "{} create user {} - role {} SUCCESS.".format(
                current_user.username, result.username, result.user_role
            ),
        }
    logger.error(
        "{} create user {} - role {} FAIL.".format(
            current_user.username, result.username, result.user_role
        )
    )
    return {
        "success": False,
        "data": result,
        "message": "{} create user {} - role {} FAIL.".format(
            current_user.username, result.username, result.user_role
        ),
    }


@router.get("/", response_model=Users)
def read_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    users = crud_users.get_users(db, skip=skip, limit=limit)

    return {
        "success": True,
        "data": users,
        "message": "list users successfully.",
    }


@router.get("/currentUser")
def read_user_me(
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_active_user),
):
    """
    Get current user.
    """

    current_user_response = {
        "username": current_user.username,
        "user_id": current_user.id,
        "status": "ok",
        "type": "account",
        "currentAuthority": current_user.user_role,
        "user_role": current_user.user_role,
    }
    return current_user_response


@router.get("/{id}", response_model=User)
def read_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    db_user = crud_users.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{id}")
def update_user(
    id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user_admin),
):
    current_user_data = jsonable_encoder(current_user)

    db_user = crud_users.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="user is not exist.")
    user_update = crud_users.update_user(
        db=db,
        db_user=db_user,
        user_update=user_update,
        current_user=current_user_data,
    )
    return {
        "success": True,
        "data": user_update,
        "message": "user update successfully.",
    }


@router.delete("/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user_admin),
):
    db_user = crud_users.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user {} not found.".format(id))
    result = crud_users.delete_user_by_id(
        db=db,
        id=id,
    )

    if result:
        logger.info(
            "User {} delete user {} SUCCESS.".format(
                current_user.username, result.username
            )
        )
        return {
            "success": True,
            "data": result,
            "message": "User {} delete user {} SUCCESS.".format(
                current_user.username, result.username
            ),
        }
    logger.error(
        "User {} delete user {} FAIL.".format(current_user.username, result.username)
    )
    return {
        "success": False,
        "data": result,
        "message": "User  {} delete user {} FAIL.".format(
            current_user.username, result.username
        ),
    }


@router.put("/{id}/password/")
def update_user_password(
    id: int,
    user_update: UserUpdatePassword,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    current_user_data = jsonable_encoder(current_user)

    db_user = crud_users.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="user is not exist.")
    user_update = crud_users.update_user_password(
        db=db,
        db_user=db_user,
        user_update=user_update,
        current_user=current_user_data,
    )
    return {
        "success": True,
        "data": user_update,
        "message": "user update successfully.",
    }

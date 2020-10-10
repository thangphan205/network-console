from sqlalchemy.orm import Session
from fastapi import FastAPI
from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from models import models
from schemas.users import User, UserCreate, UserUpdate, UserUpdatePassword
import requests
import json
from settings import settings
import ipaddress
from loguru import logger

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_id(db: Session, id: int):
    return db.query(models.Users).filter(models.Users.id == id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Users).offset(skip).limit(limit).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Users).all()


def create_user(db: Session, user: models.Users):
    pass


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user_by_id(db: Session, id: int):
    return db.query(models.Users).filter(models.Users.id == id).first()


def get_user(db: Session, username: str):
    return db.query(models.Users).filter(models.Users.username == username).first()


def update_user(
    db: Session,
    db_user: models.Users,
    user_update: UserUpdate,
    current_user: User,
):
    obj_data = jsonable_encoder(db_user)
    update_data = user_update.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_user, field, update_data[field])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user_password(
    db: Session,
    db_user: models.Users,
    user_update: UserUpdatePassword,
    current_user: User,
):
    obj_data = jsonable_encoder(db_user)
    update_data = user_update.dict(exclude_unset=True)
    # db_user.ovpn_password = update_data["password"]
    db_user.hashed_password = get_password_hash(update_data["password"])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # update openvpn password


def delete_user_by_id(db: Session, id: int):
    pass
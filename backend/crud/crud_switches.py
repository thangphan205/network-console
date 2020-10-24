from sqlalchemy.orm import Session
from fastapi import FastAPI
from passlib.context import CryptContext
from datetime import datetime
from fastapi.encoders import jsonable_encoder

from models import models
from schemas.switches import Switches, SwitchesCreate
from schemas.users import User
from utils.nornir import NornirModel


def get_switches(
    db: Session,
    skip: int = 0,
    limit: int = 100,
):

    # return db.query(models.Switches).order_by(models.Switches.id).all()
    switches = NornirModel.get_devices()
    return switches


def get_switches_by_id(db: Session, id: int):
    return db.query(models.Switches).filter(models.Switches.id == id).first()


def create_switches(db: Session, switches: models.Switches, current_user: User):

    obj_in_data = jsonable_encoder(switches)
    db_obj = models.Switches(**obj_in_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_switches(
    db: Session,
    db_switches: models.Switches,
    switches_update: SwitchesCreate,
    current_user: User,
):
    obj_data = jsonable_encoder(db_switches)
    update_data = switches_update.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_switches, field, update_data[field])
    db.add(db_switches)
    db.commit()
    db.refresh(db_switches)
    return db_switches


def delete_switches_by_id(db: Session, id: int):
    db_switches_obj = db.query(models.Switches).filter(models.Switches.id == id).first()
    db.delete(db_switches_obj)
    db.commit()
    return db_switches_obj

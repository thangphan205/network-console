from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from fastapi.encoders import jsonable_encoder

from crud import crud_switches
from schemas.users import User, UserCreate
from schemas.switches import (
    Switches,
    SwitchesCreate,
    SwitchesUpdate,
)

# from schemas import items
from db.database import SessionLocal, engine, get_db
from api.utils.security import get_current_user
from models import models


router = APIRouter()


@router.post("/")
def create_switches(
    switches: SwitchesCreate,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    current_user_data = jsonable_encoder(current_user)

    switches_create = crud_switches.create_switches(
        db=db, switches=switches, current_user=current_user_data
    )
    return {
        "success": True,
        "data": switches_create,
        "message": "switches create successfully.",
    }


@router.get("/")
def read_switches(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    switches = crud_switches.get_switches(
        db,
        skip=skip,
        limit=limit,
    )
    return {
        "success": True,
        "data": switches,
        "message": "List switches successfully.",
    }


@router.get("/{id}")
def read_switches_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    db_switches = crud_switches.get_switches_by_id(db, id=id)
    if db_switches is None:
        raise HTTPException(status_code=404, detail="switches {} not found.".format(id))
    return {
        "success": True,
        "data": db_switches,
        "message": "List switches {}.".format(id),
    }


@router.get("/ticket/{idticket}")
def read_switches_by_idticket(
    idticket: int,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    db_switches = crud_switches.get_switches_by_idticket(db, idticket=idticket)
    if db_switches is None:
        raise HTTPException(
            status_code=404, detail="switches ticket {} not found.".format(idticket)
        )
    return {
        "success": True,
        "data": db_switches,
        "message": "List switches {}.".format(idticket),
    }


@router.put("/{id}")
def update_switches(
    id: int,
    switches_update: SwitchesUpdate,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    current_user_data = jsonable_encoder(current_user)

    db_switches = crud_switches.get_switches_by_id(db, id=id)
    if db_switches is None:
        raise HTTPException(status_code=400, detail="switches is not exist.")
    switches_update = crud_switches.update_switches(
        db=db,
        db_switches=db_switches,
        switches_update=switches_update,
        current_user=current_user_data,
    )
    return {
        "success": True,
        "data": switches_update,
        "message": "switches update successfully.",
    }


@router.delete("/{id}")
def delete_switches(
    id: int,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    db_switches = crud_switches.get_switches_by_id(db, id=id)
    if db_switches is None:
        raise HTTPException(status_code=404, detail="switches {} not found.".format(id))
    db_switches = crud_switches.delete_switches_by_id(db=db, id=id)
    return {
        "success": True,
        "data": db_switches,
        "message": "User {} delete switches {}.".format(current_user.username, id),
    }

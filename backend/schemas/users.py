from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):

    username: str = ""
    email: str = ""
    full_username: str = ""
    user_role: int = 0
    is_active: bool = False
    last_login: Optional[datetime] = None
    created_date: Optional[datetime] = None
    login_fail: int = 0
    department: str = ""
    description: str = ""


class UserCreate(UserBase):
    password: str = ""


class UserUpdate(UserBase):
    pass


class UserUpdatePassword(BaseModel):
    password: str = ""


class User(UserBase):
    id: int = 0

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Users(BaseModel):
    data: List[User]
    success: bool = True
    message: str = ""


class UserCurrent(UserBase):
    pass
    # is_active: bool
    # user_role: str
    # created_date: str
    # department: str
    # last_login: str
    # login_fail: str

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
    Text,
    JSON,
)
from sqlalchemy.orm import relationship

from db.database import Base, engine


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    email = Column(String)
    full_username = Column(String)
    user_role = Column(Integer)
    is_active = Column(Boolean)
    last_login = Column(DateTime)
    created_date = Column(DateTime)
    login_fail = Column(Integer)
    department = Column(String)
    description = Column(String)


class Switches(Base):
    __tablename__ = "switches"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String)
    ip_address = Column(String)
    type_os = Column(String)
    group = Column(String)
    status = Column(String)
    description = Column(String)
    fast_cli = Column(Boolean)
    last_check = Column(DateTime)
    location = Column(String)
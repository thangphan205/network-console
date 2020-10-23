from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class SwitchesBase(BaseModel):

    hostname: str = ""
    ip_address: str = ""
    type_os: str = ""
    group: str = ""
    status: str = ""
    fast_cli: bool = False
    description: str = ""
    location: str = ""
    last_check: Optional[datetime] = None


class SwitchesCreate(SwitchesBase):
    pass


class SwitchesUpdate(SwitchesBase):
    pass


class Switches(SwitchesBase):
    id: int = 0

    class Config:
        orm_mode = True

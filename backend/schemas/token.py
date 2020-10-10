from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    status: bool


class TokenData(BaseModel):
    username: str = None


class TokenPayload(BaseModel):
    id: int = None
    user_id: int = None
    username: str = None

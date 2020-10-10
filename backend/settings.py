from pydantic import BaseSettings
import secrets


class DevSettings(BaseSettings):
    API_V1_STR: str = "/api"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600

    # Database
    DB_HOST: str = "127.0.0.1"
    DB_USER: str = "username"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "database_name"
    SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
    )

    LOGGING_FILE = "logs/console.log"


class Settings(BaseSettings):
    API_V1_STR: str = "/api"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600

    # Database
    DB_HOST: str = "127.0.0.1"
    DB_USER: str = "username"
    DB_PASSWORD: str = "password"
    DB_NAME: str = "database_name"
    SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
    )

    LOGGING_FILE = "logs/console.log"


settings = DevSettings()

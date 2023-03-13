from enum import Enum

from pydantic import BaseSettings, validator
from pytz import all_timezones


class EnvEnum(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


def assemble_db_url(_, values):
    return "{}://{}:{}@{}:{}/{}".format(
        values["DB_DRIVER"],
        values["DB_USER"],
        values["DB_PASSWORD"],
        values["DB_HOST"],
        values["DB_PORT"],
        values["DB_NAME"],
    )


def check_timezone(value):
    if value not in all_timezones:
        raise ValueError("Invalid timezone")
    return value


class Env(BaseSettings):
    API_ENV: EnvEnum

    DB_DRIVER: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    DB_URL: str | None = None
    __DB_URL = validator("DB_URL")(assemble_db_url)

    TIME_ZONE: str
    __TIME_ZONE = validator("TIME_ZONE")(check_timezone)


env = Env()

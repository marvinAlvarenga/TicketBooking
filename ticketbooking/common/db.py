from sqlalchemy.orm import Session

from ticketbooking.config.db import DbSession


def get_db() -> Session:
    try:
        session = DbSession()
        yield session
    finally:
        session.close()

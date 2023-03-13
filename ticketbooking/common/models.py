from sqlalchemy.orm import declarative_base

from ticketbooking.config.db import engine

Base = declarative_base(bind=engine)

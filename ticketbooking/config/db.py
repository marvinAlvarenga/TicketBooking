from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ticketbooking.common.env import env

engine = create_engine(url=env.DB_URL, echo=True)
DbSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

from sqlalchemy import CheckConstraint, Column, Integer, String, Text

from ticketbooking.common.models import AuditModel, IdentityModel
from ticketbooking.config.db import Base


class EventModel(Base, IdentityModel, AuditModel):
    __tablename__ = "events"
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    total_tickets = Column(Integer, CheckConstraint("total_tickets >= 0"))

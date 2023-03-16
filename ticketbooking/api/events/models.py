from sqlalchemy import CheckConstraint, Column, DateTime, Integer, String, Text

from ticketbooking.common.models import AuditModel, IdentityModel
from ticketbooking.config.db import Base


class EventModel(Base, IdentityModel, AuditModel):
    __tablename__ = "events"

    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String(255), nullable=True)
    total_tickets = Column(Integer, CheckConstraint("total_tickets >= 0"))
    starts_at = Column(DateTime(timezone=True), nullable=True)
    ends_at = Column(DateTime(timezone=True), nullable=True)

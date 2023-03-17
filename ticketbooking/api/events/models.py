from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

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

    event_type_id = Column(
        Integer,
        ForeignKey("events_type.id"),
        nullable=True,
    )
    event_type = relationship("EventTypeModel")


class EventTypeModel(Base, IdentityModel, AuditModel):
    __tablename__ = "events_type"
    name = Column(String(127), nullable=False)

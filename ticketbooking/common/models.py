from sqlalchemy import Column, DateTime, Identity, Integer

from ticketbooking.common.utils import now


class IdentityModel:
    id = Column(Integer, Identity(), primary_key=True)


class AuditModel:
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=now,
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        default=now,
        onupdate=now,
    )

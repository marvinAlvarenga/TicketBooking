from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ticketbooking.api.events.models import EventTypeModel
from ticketbooking.api.events.schemas.event_type import (
    CreateUpdateEventTypeSchema,
)


def list_events_type(db: Session) -> list[EventTypeModel]:
    return db.query(EventTypeModel).all()


def get_type_event_by_id(db: Session, event_type_id: int) -> EventTypeModel:
    event_type = (
        db.query(EventTypeModel)
        .filter(EventTypeModel.id == event_type_id)
        .first()
    )
    if not event_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )
    return event_type


def create_event_type(
    db: Session, dto: CreateUpdateEventTypeSchema
) -> EventTypeModel:
    event_type = EventTypeModel(**dto.dict())
    db.add(event_type)
    db.commit()
    db.refresh(event_type)
    return event_type


def update_event_type(
    db: Session, event_type_id: int, dto: CreateUpdateEventTypeSchema
) -> EventTypeModel:
    event_type_filter = db.query(EventTypeModel).filter(
        EventTypeModel.id == event_type_id
    )

    if not db.query(event_type_filter.exists()).scalar():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )

    event_type_filter.update(dto.dict(exclude_unset=True))
    db.commit()
    return event_type_filter.first()


def delete_event_type(db: Session, event_type_id: int) -> None:
    event_type_filter = db.query(EventTypeModel).filter(
        EventTypeModel.id == event_type_id
    )

    if not db.query(event_type_filter.exists()).scalar():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found"
        )

    event_type_filter.delete()
    db.commit()

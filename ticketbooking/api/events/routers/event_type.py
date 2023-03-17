from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ticketbooking.api.events.schemas import event_type as schemas
from ticketbooking.api.events.services import event_type as services
from ticketbooking.common.db import get_db
from ticketbooking.common.tags import Tags

router = APIRouter(prefix="/events_type", tags=[Tags.EVENTS])


@router.get("")
def list_events_type(
    db: Session = Depends(get_db),
) -> list[schemas.EventTypeSchema]:
    return services.list_events_type(db)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_event_type(
    dto: schemas.CreateUpdateEventTypeSchema, db: Session = Depends(get_db)
) -> schemas.EventTypeSchema:
    return services.create_event_type(db, dto)


@router.get("/{event_type_id}")
def get_event_type(
    event_type_id: int, db: Session = Depends(get_db)
) -> schemas.EventTypeSchema:
    return services.get_type_event_by_id(db, event_type_id)


@router.put("/{event_type_id}")
def update_event_type(
    event_type_id: int,
    dto: schemas.CreateUpdateEventTypeSchema,
    db: Session = Depends(get_db),
) -> schemas.EventTypeSchema:
    return services.update_event_type(db, event_type_id, dto)


@router.delete("/{event_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event_type(
    event_type_id: int, db: Session = Depends(get_db)
) -> None:
    services.delete_event_type(db, event_type_id)

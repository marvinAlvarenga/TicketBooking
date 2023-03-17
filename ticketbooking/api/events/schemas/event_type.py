from pydantic import BaseModel

from ticketbooking.common.schemas import IdentitySchema


class BaseEventTypeSchema(BaseModel):
    name: str


class CreateUpdateEventTypeSchema(BaseEventTypeSchema):
    pass


class EventTypeSchema(BaseEventTypeSchema, IdentitySchema):
    class Config:
        orm_mode = True

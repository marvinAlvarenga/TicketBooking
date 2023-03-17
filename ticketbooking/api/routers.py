from fastapi import APIRouter

from ticketbooking.api.events.routers.event_type import (
    router as event_type_router,
)

api_router_v1 = APIRouter(prefix="/api/v1")
api_router_v1.include_router(event_type_router)

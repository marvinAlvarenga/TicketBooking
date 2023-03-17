from fastapi import FastAPI

from ticketbooking.api.routers import api_router_v1

app = FastAPI(
    title="RoomBookingApi",
    version="0.1.0",
)

app.include_router(api_router_v1)


@app.get("/")
def health_check() -> str:
    return "Ok!"

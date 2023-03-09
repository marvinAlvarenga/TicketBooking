from fastapi import FastAPI

app = FastAPI(
    title='RoomBookingApi',
    version='0.1.0',
)


@app.get('/')
def health_check() -> str:
    return 'Ok!'

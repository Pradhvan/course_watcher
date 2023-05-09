from fastapi import FastAPI

from config.db_config import initiate_database
from routes.student import router as courserouter

app = FastAPI()


@app.on_event("startup")
async def start_database():
    await initiate_database()


app.include_router(courserouter)

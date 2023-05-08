from fastapi import FastAPI

from routes.urls import router

app = FastAPI()

app.include_router(router)

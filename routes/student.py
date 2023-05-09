from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.course import Course

router = APIRouter()


@router.get("/")
async def ping():
    json_compatible_item_data = jsonable_encoder({"ping": "pong!"})
    return JSONResponse(content=json_compatible_item_data)

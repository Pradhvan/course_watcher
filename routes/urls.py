from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from models.course import Course

router = APIRouter()


@router.get("/")
async def ping():
    data = {"status": "200OK"}
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)

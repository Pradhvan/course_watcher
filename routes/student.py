from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from handlers.course import course_list
from models.course import Course

router = APIRouter()


@router.get("/")
async def ping():
    json_compatible_item_data = jsonable_encoder({"ping": "pong!"})
    return JSONResponse(content=json_compatible_item_data)


@router.get("/courses")
async def get_courses(sort_by: str = "", domain: str = "str"):
    courses = await course_list()
    json_compatible_courses_data = jsonable_encoder(courses)
    return JSONResponse(content=json_compatible_courses_data)


@router.get("/course/{course_id}/overview")
async def get_course_overview(course_id):
    ...


@router.get("/course/{course_id}/chapter/{chapter_id}")
async def get_chapter(course_id, chapter_id):
    ...


@router.get("/course/{course_id}/raiting")
async def get_course_raiting(course_id):
    ...

from models.course import Course

course_collection = Course


async def course_list():
    courses = await course_collection.all().to_list()
    return courses


async def get_course(course_id):
    course = await course_collection.get("f_{course_id}")
    if course:
        return course

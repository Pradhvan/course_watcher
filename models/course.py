from beanie import Document
from pydantic import BaseModel, Field


class Chapter(Document):
    name: str = Field(...)
    text: str = Field(...)


class Course(Document):
    name: str = Field(...)
    date: int = Field(...)
    description: str = Field(...)
    domain: list = [str]
    chapters: list = [Chapter]
    course_id: str = Field(..., alias="_id")
    rating: float = Field(0.0, ge=0.0, le=5.0)

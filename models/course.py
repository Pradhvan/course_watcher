from beanie import Document
from pydantic import BaseModel, Field


class Chapter(BaseModel):
    name: str = Field(...)
    text: str = Field(...)


class Course(Document):
    name: str = Field(...)
    date: int = Field(...)
    description: str = Field(...)
    domain: list = [str]
    chapter: list = [Chapter]

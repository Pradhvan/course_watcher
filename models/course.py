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

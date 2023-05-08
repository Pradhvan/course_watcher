from pydantic import BaseModel


class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: list
    chapter: list

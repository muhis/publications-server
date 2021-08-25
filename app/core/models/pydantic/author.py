from pydantic import BaseModel
from pydantic.types import PositiveInt
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from app.core.models.tortoise.author import Author

AuthorOut = pydantic_model_creator(Author)

class AuthorIn(BaseModel):
    name: str
    id: int

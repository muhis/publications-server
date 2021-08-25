from app.core.models.tortoise.author import Author
from typing import List
from pydantic import BaseModel, PositiveInt, fields, constr
from tortoise.contrib.pydantic.creator import pydantic_model_creator, pydantic_queryset_creator
from app.core.models.pydantic.author import AuthorOut
from app.core.models.tortoise.publication import Publication


PublicationPydantic = pydantic_model_creator(Publication)
PublicationPydanticList = pydantic_queryset_creator(Publication)


class PublicationIn(BaseModel):
    title: str = fields.Field(max_length=1024)
    publish_year: int
    authors: List[int]


class PublicationOut(PublicationIn):
    id: int
    authors: List[AuthorOut]

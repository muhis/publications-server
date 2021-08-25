"""
Pydantic models.
"""
from tortoise.contrib.pydantic.creator import pydantic_queryset_creator
from .author import AuthorOut, AuthorIn
from app.core.models.tortoise.publication import Publication
from .publication import PublicationPydantic, PublicationPydanticList, PublicationOut

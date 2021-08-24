import typing

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel


class TypedAPIRouter(BaseModel):
    """ Typed APIRouter. Needed for initalizer """

    router: APIRouter
    prefix: str = str()
    tags: typing.List[str] = []

    class Config:
        arbitrary_types_allowed = True

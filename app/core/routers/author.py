from fastapi.routing import APIRouter
from app.core.models.pydantic import AuthorIn, AuthorOut
from app.core.models.tortoise import Author
from starlette.status import HTTP_201_CREATED

authors_router = APIRouter()


@authors_router.post('/authors', response_model=AuthorOut, status_code=HTTP_201_CREATED)
async def author_create(author: AuthorIn):
    author_object = await Author.create(name=author.name)
    return await AuthorOut.from_tortoise_orm(author_object)

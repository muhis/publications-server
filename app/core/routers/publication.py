
from app.core import exceptions
from app.core.models.pydantic.author import AuthorOut
from app.core.models.tortoise import author
from app.core.models.tortoise.author import Author
from app.core.models.pydantic.publication import PublicationIn
from fastapi import APIRouter
from starlette.exceptions import HTTPException
from pydantic.error_wrappers import ValidationError
from tortoise.contrib.pydantic.creator import pydantic_queryset_creator
from app.core.models.tortoise import Publication, publication
from app.core.models.pydantic import PublicationPydantic, PublicationPydanticList, PublicationOut
from starlette.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST
from pydantic import ValidationError
from typing import List, Optional
from loguru import logger
publications_router = APIRouter()


async def list_publications(publicationYear:int=None) -> Optional[PublicationPydanticList]:
    if publicationYear:
        publications = Publication.filter(publish_year=publicationYear)
    else:
        publications = Publication.all()

    pydantic_publications = await PublicationPydanticList.from_queryset(publications)
    return pydantic_publications



@publications_router.get('/publications', response_model=Optional[PublicationPydanticList], status_code=HTTP_200_OK)
async def list_all(publicationYear:int=None):
    response = await list_publications(publicationYear=publicationYear)
    return response

@publications_router.post('/publications', response_model=PublicationOut, status_code=HTTP_201_CREATED)
async def create_publication(publication: PublicationIn):
    authors = publication.authors
    existing_authors_objects = await get_existing_authors(authors)
    publication = await create_publication_object(publication, existing_authors_objects)
    return publication

async def create_publication_object(publication: PublicationIn, existing_authors_objects) -> PublicationPydantic:
    # Tortoise orm does not allow setting m2m fields -authors- from init.
    publication_dict = publication.dict()
    publication_dict.pop('authors')

    publication_object = await Publication.create(**publication_dict)
    
    # Add authors
    await publication_object.authors.add(*existing_authors_objects)
    await publication_object.save()
    
    # Create output pydantic model
    publication_pydantic = await PublicationPydantic.from_tortoise_orm(publication_object)
    authors = [await AuthorOut.from_tortoise_orm(obj) for obj in existing_authors_objects]
    publication_pydantic = PublicationOut(authors=authors, **publication_pydantic.dict())
    return publication_pydantic

async def get_existing_authors(authors) -> List[Author]:
    """
    Get a list of existing authors from DB
    Raises HTTPException when one or more of the authors are not found.
    """
    if not authors:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail='At least one author is required')
    existing_authors_objects = await Author.filter(id__in=authors)
    existing_authors = [author.id for author in existing_authors_objects]
    if not existing_authors == authors:
        invalid_authors = set(authors) - set(existing_authors)
        error_detail = f'Author {invalid_authors} does not exist.'
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=error_detail)
    return existing_authors_objects


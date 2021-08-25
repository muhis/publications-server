import pytest
from fastapi import APIRouter

from app.utils.api.router import TypedAPIRouter


@pytest.fixture
def router():
    my_router = APIRouter()

    @my_router.get("/get")
    async def get():
        return {}

    return my_router


def test_typed_api_router(router: APIRouter):
    typed_router = TypedAPIRouter(router=router)
    assert typed_router.router is router
    assert typed_router.prefix == ""
    assert len(typed_router.tags) < 1

    # test working with default values
    another_router = TypedAPIRouter(router=router)
    another_router.tags.append("elem")

    assert len(another_router.tags) == 1
    assert len(typed_router.tags) < 1

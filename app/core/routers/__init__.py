from app.core.routers.generic import router as server_health
from app.core.routers.publication import publications_router
from app.core.routers.author import authors_router
from app.utils.api.router import TypedAPIRouter

generic_router = TypedAPIRouter(router=server_health, tags=["Server health"])
publications_router = TypedAPIRouter(router=publications_router, tags=["Publications"])
author_router = TypedAPIRouter(router=authors_router, tags=["Authors"])

from app.core.routers.generic import router as server_health
from app.utils.api.router import TypedAPIRouter

generic_router = TypedAPIRouter(router=server_health, tags=["server health"])

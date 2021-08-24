from pydantic import BaseModel


class ServerHealth(BaseModel):
    state:str
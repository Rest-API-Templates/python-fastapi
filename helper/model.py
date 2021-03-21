from pydantic import BaseModel

class TodoOut(BaseModel):
    id: int
    title: str
    status: str
    lastUpdate: str

class TodoIn(BaseModel):
    title: str
    status: str
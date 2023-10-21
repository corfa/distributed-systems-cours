from pydantic import BaseModel



class Item(BaseModel):
    id: int = None 
    url: str = None
    status: str = None

class Status(BaseModel):
    status: int = None
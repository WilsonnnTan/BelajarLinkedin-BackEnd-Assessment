from pydantic import BaseModel
import uuid

class AddClass(BaseModel):
    name: str
    detail: str | None
    
class EditClass(BaseModel):
    name: str
    detail: str | None

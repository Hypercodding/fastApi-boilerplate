from pydantic import BaseModel

class Role_class(BaseModel):
    id: int | None = None
    name: str
    
    class Config:
        from_attributes = True
        

from pydantic import BaseModel
from .role import Role_class


class User_class(BaseModel):
    id: int | None = None
    email: str
    roles: list["Role_class"] = []

    class Config:
         from_attributes = True

class UserCreate(User_class):
    email: str
    password: str


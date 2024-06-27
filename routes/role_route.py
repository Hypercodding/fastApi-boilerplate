from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from configurations import get_database
from services import create_user_role, get_roles
from models import Role_class

router = APIRouter()

@router.get("/", response_model=list[Role_class])
def get_roles(skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    roles = get_roles(database, skip=skip, limit=limit)
    return roles


@router.post("/{user_id}/", response_model=Role_class)
def create_role_of_user(user_id: int, role: Role_class, database: Session = Depends(get_database)):
    return create_user_role(database=database, user_id=user_id, role=role)
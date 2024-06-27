from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import (
    get_all_users, 
    get_user,
    get_user_by_email, 
    create_user
)
from configurations import get_database
from models import (
    User_class,
    UserCreate
)      


#roter initialization
router = APIRouter()

#routers
@router.get("/", response_model=list[User_class])
def get_users(skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    user = get_all_users(database, skip=skip, limit=limit)
    return user

@router.get("/{user_id}", response_model=User_class)
def get_user(user_id: int, database: Session = Depends(get_database)):
    database_user = get_user(database, user_id=user_id)
    if database_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return database_user


@router.post("/", response_model=User_class)
def create_user_route(user: UserCreate, database: Session = Depends(get_database)):
    database_user = get_user_by_email(database, email=user.email)
    if database_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(database=database, user=user)
import bcrypt
from sqlalchemy.orm import Session
from models import User, UserCreate

def database_function(obj, database: Session):
    database.add(obj)
    database.commit()
    database.refresh(obj)
    return obj

def get_all_users(database: Session, skip: int = 0, limit: int = 10):
    return database.query(User).offset(skip).limit(limit).all()

def get_user(database: Session, user_id: int):
    return database.query(User).filter(User.id == user_id).first()

def get_user_by_email(database: Session, email: str):
    return database.query(User).filter(User.email == email).first()

def create_user(database: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    database_user = User(email=user.email, hashed_password=hashed_password.decode('utf-8'))
    user = database_function(database_user, database)
    return user

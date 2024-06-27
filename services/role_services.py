from sqlalchemy.orm import Session
from models import Role_class,Role


def database_function(obj, database: Session):
    database.add(obj)
    database.commit()
    database.refresh(obj)
    return obj

def get_roles(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Role).offset(skip).limit(limit).all()


def create_user_role(database: Session, user_id: int, role: Role_class):
    db_role = Role(name=role.name, user_id=user_id)  # Adjust instantiation as per your needs
    return database_function(db_role, database)

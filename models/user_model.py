from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from configurations import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    roles = relationship("Role", back_populates="owner")

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from configurations import Base



class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="roles")

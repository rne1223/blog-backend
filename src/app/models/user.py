from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    firt_name = Column(String(256), nullable=False)
    surname = Column(String(256), nullable=False)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(String(256), nullable=False)
    recipes = relationship(
        "Recipe",
        cascade="all,delete-orphan",
        back_populates="submitter",
        userlist=True,
    )

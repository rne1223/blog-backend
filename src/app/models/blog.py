from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    body = Column(Text, index=True, nullable=False) 
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    submitter = relationship("User", back_populates="blogs")
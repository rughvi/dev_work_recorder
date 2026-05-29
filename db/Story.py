from sqlalchemy import Column, Integer, String
from db.db import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
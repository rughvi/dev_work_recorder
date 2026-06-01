from sqlalchemy import Column, Integer, String
from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Story(Base):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[int] = mapped_column(String, nullable=False)
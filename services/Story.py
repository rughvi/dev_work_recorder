from sqlalchemy import select
from db.Story import Story
from db.db import SessionLocal

async def exists(story: int):
    """Checks if story exists or not"""
    async with SessionLocal() as session:
        result = await session.execute(
            select(Story).where(Story.number == story)
        )
        return result.scalar_one_or_none()
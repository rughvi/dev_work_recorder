from langchain.tools import tool
from pydantic import BaseModel, Field
from sqlalchemy import select
import services.Story as StoryService

class StoryCheckInput(BaseModel):
    story: int = Field(description="Story number")

class StoryCheckOutput(BaseModel):
    story: int = Field(description="Story number")
    exists: bool = Field(description="Story exists")
    message: str = Field(description="Story exists or not")

class StoryInsertInput(BaseModel):
    story: int = Field(description="Story number")

@tool(args_schema=StoryCheckInput)
async def exists(story: int) -> StoryCheckOutput:
    """Checks if story exists or not"""
    storyExists = await StoryService.exists(story)
    if not storyExists:
        return StoryCheckOutput(
            story=story,
            exists=False,
            message="Story not exists")
    return StoryCheckOutput(
        story=story,
        exists=True,
        message="Story exists")

@tool(args_schema=StoryInsertInput)
def insert(story: int):
    """Inserts story"""
    return "Inserted"

story_tools = [
    exists,
    insert
]
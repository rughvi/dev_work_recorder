from langchain.tools import tool
from pydantic import BaseModel, Field

class StoryCheckInput(BaseModel):
    story: int = Field(description="Story number")

class StoryCheckOutput(BaseModel):
    story: int = Field(description="Story number")
    exists: bool = Field(description="Story exists")
    message: str = Field(description="Story exists or not")

class StoryInsertInput(BaseModel):
    story: int = Field(description="Story number")

@tool(args_schema=StoryCheckInput)
def exists(story: int) -> StoryCheckOutput:
    """Checks if story exists or not"""
    if story == 189:
        return StoryCheckOutput(
            story=story,
            exists=True,
            message="Story exists").model_dump()
    else:
        return StoryCheckOutput(
            story=story,
            exists=False,
            message="Story not exists").model_dump()

@tool(args_schema=StoryInsertInput)
def insert(story: int):
    """Inserts story"""
    return "Inserted"

story_tools = [
    exists,
    insert
]
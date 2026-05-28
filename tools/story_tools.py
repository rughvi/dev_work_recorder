from langchain.tools import tool
from pydantic import BaseModel, Field

class StoryCheckInput(BaseModel):
    story: int = Field(description="Story number")

class StoryInsertInput(BaseModel):
    story: int = Field(description="Story number")

@tool(args_schema=StoryCheckInput)
def exists(story: int):
    """Checks if story exists or not"""
    if story == 189:
        return "Exists"
    else:
        return "Not exists"

@tool(args_schema=StoryInsertInput)
def insert(story: int):
    """Inserts story"""
    return "Inserted"

story_tools = [
    exists,
    insert
]
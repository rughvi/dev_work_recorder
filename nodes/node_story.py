from llm import llm
from langchain_ollama import ChatOllama

from tools.story_tools import story_tools

llm_with_story_tools = llm.bind_tools(story_tools)

async def node_story(state):
    response = await llm_with_story_tools.ainvoke([
        {
            "role":"system",
            "content": """
                You are a database assistant.
                Rules:
                1. Always check if story as a number exists first
                2. Insert only if story does not exists
            """
        },
        *state["messages"]])
    return {"messages": [response]}
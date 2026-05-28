from llm import llm
from langchain_ollama import ChatOllama

from tools.story_tools import story_tools

llm_with_story_tools = llm.bind_tools(story_tools)

def node_story(state):
    response = llm_with_story_tools.invoke([
        {
            "role":"system",
            "content": """
                You are a database assistant.
                Rules:
                1. Always check if story exists first
                2. Insert only if story does not exists
            """
        },
        *state["messages"]])
    return {"messages": [response]}
from llm import llm
from langchain_ollama import ChatOllama

def node_story_task(state):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}
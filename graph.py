from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from nodes.node_story import node_story
from nodes.node_story_task import node_story_task
from langgraph.prebuilt import ToolNode, tools_condition
from tools.story_tools import story_tools


# Shared state
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Build graph
builder = StateGraph(State)

builder.add_node("story", node_story)
builder.add_node("story_tools", ToolNode(story_tools))
builder.add_node("story_task", node_story_task)

builder.add_edge(START, "story")
builder.add_conditional_edges(
    "story",
    tools_condition,
    {
        "tools": "story_tools",
        END: "story_task"
    }
)
builder.add_edge("story_tools", "story")
builder.add_edge("story_task", END)

app = builder.compile()

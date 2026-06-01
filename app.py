

from graph import app
import asyncio
from langchain_core.messages import HumanMessage

async def main():
    # Run graph
    result = await app.ainvoke({
        "messages": [
            HumanMessage(content="Dave is working on subtask 16773 under story 191")
        ]
    })

    print("\nAI Response:\n")
    print(result)

asyncio.run(main())
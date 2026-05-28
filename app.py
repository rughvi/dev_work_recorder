

from graph import app

# Run graph
result = app.invoke({
    "messages": ["Dave is working on subtask 16773 under story 191"]
})

print("\nAI Response:\n")
print(result)
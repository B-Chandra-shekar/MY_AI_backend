from transformers import pipeline
from typing import Dict, List

chatbot = pipeline("text-generation", model="distilgpt2")

# In-memory context store
session_memory: Dict[str, List[str]] = {}

def process_message(user_text: str, session_id: str = "default") -> str:
    if session_id not in session_memory:
        session_memory[session_id] = []

    # Build the context string
    context = "\n".join(session_memory[session_id][-5:])  # last 5 messages
    prompt = context + f"\nUser: {user_text}\nAI:"

    generated = chatbot(prompt, max_length=200, num_return_sequences=1)[0]["generated_text"]

    # Extract AI reply only (remove prompt part)
    reply = generated[len(prompt):].strip().split("\n")[0]

    # Save to memory
    session_memory[session_id].append(f"User: {user_text}")
    session_memory[session_id].append(f"AI: {reply}")

    return reply

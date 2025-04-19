
import requests

OPENROUTER_API_KEY = "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" 

def process_message(user_message, session_id="default"):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:4200", 
        "X-Title": "Futuristic Dev Assistant"
    }

    data = {
        "model": "openai/gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful, futuristic AI assistant for developers."},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)

    try:
        reply = response.json()['choices'][0]['message']['content']
    except Exception as e:
        reply = "Error: Something went wrong.\n" + str(response.text)
    
    return reply.strip()

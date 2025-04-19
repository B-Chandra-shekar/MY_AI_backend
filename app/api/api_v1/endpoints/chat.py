from fastapi import APIRouter, Request, HTTPException
import requests
import os
import json

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("text", "")
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-2.0-flash-thinking-exp:free",  # Use exact model name from OpenRouter docs
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        print("\n[ AI RESPONSE]:", json.dumps(result, indent=2))

        return {"response": result['choices'][0]['message']['content']}
    
    except requests.exceptions.RequestException as e:
        print("\n[ API ERROR]:", str(e))
        raise HTTPException(status_code=500, detail="OpenRouter API call failed.")
    
    except KeyError:
        print("\n[ RESPONSE PARSE ERROR]:", response.text)
        raise HTTPException(status_code=500, detail="Unexpected API response format.")

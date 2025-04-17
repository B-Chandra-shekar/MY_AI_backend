from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import process_message

router = APIRouter()

class ChatRequest(BaseModel):
    text: str
    session_id: str = "default"

@router.post("/chat")
def chat_endpoint(req: ChatRequest):
    response = process_message(req.text, req.session_id)
    return {"response": response}

from fastapi import APIRouter
from app.models.message import Message, ChatResponse
from app.services.chat_service import process_message

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(message: Message):
    response_text = process_message(message.text)
    return ChatResponse(response=response_text)

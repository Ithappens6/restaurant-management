"""
Simple Chat API Routes
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    """Simple chat request"""
    restaurant_id: str
    session_id: str
    message: str
    chat_history: Optional[List[Dict]] = None


class ChatResponse(BaseModel):
    """Simple chat response"""
    session_id: str
    restaurant_id: str
    user_message: str
    assistant_message: str
    success: bool


@router.post("", response_model=ChatResponse, summary="Chat with AI assistant")
async def chat(request: ChatRequest):
    """
    Send a message to the AI assistant
    
    - **restaurant_id**: Restaurant identifier (e.g., "kurdiescurry")
    - **session_id**: Session identifier for conversation tracking
    - **message**: User's message
    - **chat_history**: Optional previous messages in format [{"role": "user", "content": "..."}]
    
    Example:
    ```json
    {
        "restaurant_id": "kurdiescurry",
        "session_id": "session123",
        "message": "What are your vegetarian options?",
        "chat_history": []
    }
    ```
    """
    try:
        from app.services.simple_chat_service import SimpleChatService
        
        # Create chat service
        chat_service = SimpleChatService()
        
        # Get response from OpenAI
        assistant_message = chat_service.chat(
            restaurant_id=request.restaurant_id,
            session_id=request.session_id,
            message=request.message,
            chat_history=request.chat_history or []
        )
        
        return ChatResponse(
            session_id=request.session_id,
            restaurant_id=request.restaurant_id,
            user_message=request.message,
            assistant_message=assistant_message,
            success=True
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")


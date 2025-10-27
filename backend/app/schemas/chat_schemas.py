"""
Chat Schemas
Pydantic schemas for chat-related data validation and serialization
"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ChatMessageRequest(BaseModel):
    """Schema for incoming chat message"""
    session_id: str = Field(..., description="Unique session identifier")
    restaurant_id: str = Field(..., description="Restaurant identifier")
    message: str = Field(..., min_length=1, max_length=2000, description="User message")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "session_id": "user123_session456",
                "restaurant_id": "kurdiescurry",
                "message": "What are your vegetarian options?"
            }
        }
    }


class ChatMessage(BaseModel):
    """Schema for chat message"""
    id: str
    session_id: str
    restaurant_id: str
    role: str  # 'user' or 'assistant'
    content: str
    created_at: datetime


class ChatSession(BaseModel):
    """Schema for chat session"""
    session_id: str
    restaurant_id: str
    created_at: datetime
    last_activity: datetime


class ChatResponse(BaseModel):
    """Schema for chat API response"""
    success: bool
    message: str
    session_id: str
    assistant_message: str
    message_id: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "success": True,
                "message": "Message processed successfully",
                "session_id": "user123_session456",
                "assistant_message": "We have many delicious vegetarian options including samosas, pakoras, and chana masala...",
                "message_id": "msg_abc123"
            }
        }
    }


class ChatHistoryResponse(BaseModel):
    """Schema for chat history response"""
    session_id: str
    restaurant_id: str
    messages: List[ChatMessage]
    total_messages: int
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "session_id": "user123_session456",
                "restaurant_id": "kurdiescurry",
                "total_messages": 4,
                "messages": [
                    {
                        "id": "msg_001",
                        "session_id": "user123_session456",
                        "restaurant_id": "kurdiescurry",
                        "role": "user",
                        "content": "What are your vegetarian options?",
                        "created_at": "2025-10-27T16:30:00Z"
                    },
                    {
                        "id": "msg_002",
                        "session_id": "user123_session456",
                        "restaurant_id": "kurdiescurry",
                        "role": "assistant",
                        "content": "We have many delicious vegetarian options...",
                        "created_at": "2025-10-27T16:30:05Z"
                    }
                ]
            }
        }
    }

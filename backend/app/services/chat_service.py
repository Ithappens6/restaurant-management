"""
Chat Service
Business logic for chat operations with OpenAI integration
"""
from typing import List, Optional
from app.repositories.sqlalchemy_chat_repository import SQLAlchemyChatRepository
from app.schemas.chat_schemas import ChatMessageRequest, ChatResponse, ChatHistoryResponse, ChatMessage
from app.services.restaurant_service import RestaurantService
from openai import OpenAI
import os
import uuid
from datetime import datetime


class ChatService:
    """
    Service for handling chat operations with OpenAI integration
    """
    
    def __init__(self, chat_repository: SQLAlchemyChatRepository, restaurant_service: RestaurantService):
        self.chat_repository = chat_repository
        self.restaurant_service = restaurant_service
        
        # Initialize OpenAI client
        from app.core.config import settings
        api_key = settings.openai_api_key or os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "":
            raise ValueError("OPENAI_API_KEY is not configured in settings or environment")
        
        self.openai_client = OpenAI(api_key=api_key)
    
    def process_message(self, request: ChatMessageRequest) -> ChatResponse:
        """
        Process a chat message and return AI response
        """
        session_id = request.session_id
        restaurant_id = request.restaurant_id
        user_message = request.message
        
        # Get or create session
        session = self.chat_repository.get_session(session_id)
        if not session:
            session = self.chat_repository.create_session(session_id, restaurant_id)
        
        # Update session activity
        self.chat_repository.update_session_activity(session_id)
        
        # Store user message
        user_msg = self.chat_repository.create_message(
            session_id=session_id,
            restaurant_id=restaurant_id,
            role="user",
            content=user_message
        )
        
        # Get chat history for context (empty if none found)
        try:
            chat_history = self.chat_repository.get_session_messages(session_id, limit=20)
        except:
            chat_history = []
        
        # Get restaurant context
        try:
            restaurant_info = self.restaurant_service.get_restaurant(restaurant_id)
            restaurant_context = self._build_restaurant_context(restaurant_info)
        except:
            restaurant_context = "You are a helpful assistant for a restaurant."
        
        # Build conversation context for OpenAI
        messages = self._build_openai_messages(restaurant_context, chat_history)
        
        try:
            # Call OpenAI API
            response = self.openai_client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                max_tokens=500,
                temperature=0.7,
                stream=False
            )
            
            assistant_message = response.choices[0].message.content
            
            # Store assistant response
            assistant_msg = self.chat_repository.create_message(
                session_id=session_id,
                restaurant_id=restaurant_id,
                role="assistant",
                content=assistant_message
            )
            
            return ChatResponse(
                success=True,
                message="Message processed successfully",
                session_id=session_id,
                assistant_message=assistant_message,
                message_id=assistant_msg.id
            )
            
        except Exception as e:
            # Handle OpenAI API errors
            error_message = f"I apologize, but I'm having trouble processing your request right now. Please try again later."
            
            # Store error response
            error_msg = self.chat_repository.create_message(
                session_id=session_id,
                restaurant_id=restaurant_id,
                role="assistant",
                content=error_message
            )
            
            return ChatResponse(
                success=False,
                message=f"Error processing message: {str(e)}",
                session_id=session_id,
                assistant_message=error_message,
                message_id=error_msg.id
            )
    
    def get_chat_history(self, session_id: str, restaurant_id: str) -> ChatHistoryResponse:
        """
        Get chat history for a session
        """
        # Verify session exists and belongs to restaurant
        session = self.chat_repository.get_session(session_id)
        if not session or session.restaurant_id != restaurant_id:
            raise ValueError("Session not found or doesn't belong to this restaurant")
        
        messages = self.chat_repository.get_session_messages(session_id)
        total_messages = self.chat_repository.get_session_messages_count(session_id)
        
        return ChatHistoryResponse(
            session_id=session_id,
            restaurant_id=restaurant_id,
            messages=messages,
            total_messages=total_messages
        )
    
    def _build_restaurant_context(self, restaurant_info) -> str:
        """
        Build restaurant context for OpenAI
        """
        if not restaurant_info:
            return "You are a helpful assistant for a restaurant."
        
        context = f"""You are a helpful assistant for {restaurant_info.name}, a restaurant.
        
Restaurant Information:
- Name: {restaurant_info.name}
- Address: {restaurant_info.address}
- Phone: {restaurant_info.phone}
- Email: {restaurant_info.email}
- Cuisine Type: {restaurant_info.cuisine_type}
- Tagline: {restaurant_info.tagline}
- Story: {restaurant_info.story}

Please help customers with:
1. Menu recommendations
2. Restaurant information
3. Reservation inquiries
4. General questions about the restaurant

Be friendly, helpful, and accurate. If you don't know something specific about the restaurant, 
suggest they call the restaurant directly at {restaurant_info.phone}."""
        
        return context
    
    def _build_openai_messages(self, restaurant_context: str, chat_history: List[ChatMessage]) -> List[dict]:
        """
        Build messages array for OpenAI API
        """
        messages = [
            {
                "role": "system",
                "content": restaurant_context
            }
        ]
        
        # Add chat history (last 10 messages to avoid token limits)
        recent_history = chat_history[-10:] if len(chat_history) > 10 else chat_history
        
        for msg in recent_history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        return messages
    
    def generate_session_id(self, restaurant_id: str) -> str:
        """
        Generate a unique session ID
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        random_id = str(uuid.uuid4())[:8]
        return f"{restaurant_id}_{timestamp}_{random_id}"

"""
Simple Chat Service - Direct OpenAI Integration
"""
from openai import OpenAI
from typing import List, Dict


class SimpleChatService:
    """
    Simple chat service with direct OpenAI integration
    """
    
    def __init__(self):
        # Hardcoded API key as requested
        self.api_key = "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"
        import os
        os.environ["OPENAI_API_KEY"] = self.api_key
        self.client = OpenAI()
        self.model = "gpt-4o-mini"  # Using GPT-4o-mini
    
    def chat(self, restaurant_id: str, session_id: str, message: str, chat_history: List[Dict] = None) -> str:
        """
        Send a message to OpenAI and get response
        
        Args:
            restaurant_id: Restaurant identifier
            session_id: Session identifier
            message: User's message
            chat_history: Optional chat history [(role, content), ...]
        
        Returns:
            OpenAI's response text
        """
        # Build messages for OpenAI
        messages = [
            {
                "role": "system",
                "content": f"You are a helpful assistant for restaurant '{restaurant_id}'. Help customers with their questions about the restaurant, menu, reservations, and general inquiries."
            }
        ]
        
        # Add chat history if provided
        if chat_history:
            for msg in chat_history:
                messages.append({
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                })
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": message
        })
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error: {str(e)}"


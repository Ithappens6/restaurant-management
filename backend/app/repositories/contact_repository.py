"""
Contact Message Repository Implementation
Handles data access for contact form submissions
"""
from typing import List, Optional
from app.models import ContactMessage
import uuid


class IContactRepository:
    """Interface for contact repository"""
    
    def get_all(self) -> List[ContactMessage]:
        """Get all contact messages"""
        raise NotImplementedError
    
    def get_by_id(self, message_id: str) -> Optional[ContactMessage]:
        """Get contact message by ID"""
        raise NotImplementedError
    
    def create(self, message: ContactMessage) -> ContactMessage:
        """Create a new contact message"""
        raise NotImplementedError


class InMemoryContactRepository(IContactRepository):
    """
    In-memory implementation of contact repository
    Stores contact messages in memory
    """
    
    def __init__(self):
        self._messages: List[ContactMessage] = []
    
    def get_all(self) -> List[ContactMessage]:
        """Get all contact messages"""
        return self._messages.copy()
    
    def get_by_id(self, message_id: str) -> Optional[ContactMessage]:
        """Get contact message by ID"""
        for message in self._messages:
            if message.id == message_id:
                return message
        return None
    
    def create(self, message: ContactMessage) -> ContactMessage:
        """Create a new contact message"""
        # Generate unique ID if not provided
        if not message.id:
            message.id = str(uuid.uuid4())[:8]
        
        self._messages.append(message)
        return message
    
    def delete(self, message_id: str) -> bool:
        """Delete a contact message"""
        initial_length = len(self._messages)
        self._messages = [m for m in self._messages if m.id != message_id]
        return len(self._messages) < initial_length


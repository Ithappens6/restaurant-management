"""
SQLAlchemy Chat Repository
Database implementation of chat session and message storage
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.database.models import ChatSessionModel, ChatMessageModel
from app.schemas.chat_schemas import ChatMessage, ChatSession
import uuid
from datetime import datetime


class SQLAlchemyChatRepository:
    """
    SQLAlchemy implementation of chat repository
    Stores chat sessions and messages in database with full persistence
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def create_session(self, session_id: str, restaurant_id: str) -> ChatSession:
        """Create a new chat session"""
        db_session = ChatSessionModel(
            session_id=session_id,
            restaurant_id=restaurant_id,
            created_at=datetime.now(),
            last_activity=datetime.now()
        )
        
        self.db.add(db_session)
        self.db.commit()
        self.db.refresh(db_session)
        
        return self._to_session_domain(db_session)
    
    def get_session(self, session_id: str) -> Optional[ChatSession]:
        """Get chat session by ID"""
        db_session = self.db.query(ChatSessionModel).filter(
            ChatSessionModel.session_id == session_id
        ).first()
        
        if not db_session:
            return None
        
        return self._to_session_domain(db_session)
    
    def update_session_activity(self, session_id: str) -> bool:
        """Update last activity timestamp for session"""
        db_session = self.db.query(ChatSessionModel).filter(
            ChatSessionModel.session_id == session_id
        ).first()
        
        if not db_session:
            return False
        
        db_session.last_activity = datetime.now()
        self.db.commit()
        
        return True
    
    def create_message(self, session_id: str, restaurant_id: str, role: str, content: str) -> ChatMessage:
        """Create a new chat message"""
        message_id = str(uuid.uuid4())[:8]
        
        db_message = ChatMessageModel(
            id=message_id,
            session_id=session_id,
            restaurant_id=restaurant_id,
            role=role,
            content=content,
            created_at=datetime.now()
        )
        
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        
        return self._to_message_domain(db_message)
    
    def get_session_messages(self, session_id: str, limit: int = 50) -> List[ChatMessage]:
        """Get all messages for a session, ordered by creation time"""
        db_messages = self.db.query(ChatMessageModel).filter(
            ChatMessageModel.session_id == session_id
        ).order_by(ChatMessageModel.created_at.asc()).limit(limit).all()
        
        return [self._to_message_domain(msg) for msg in db_messages]
    
    def get_session_messages_count(self, session_id: str) -> int:
        """Get count of messages in a session"""
        return self.db.query(ChatMessageModel).filter(
            ChatMessageModel.session_id == session_id
        ).count()
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a chat session and all its messages"""
        # Delete all messages first
        self.db.query(ChatMessageModel).filter(
            ChatMessageModel.session_id == session_id
        ).delete()
        
        # Delete the session
        deleted = self.db.query(ChatSessionModel).filter(
            ChatSessionModel.session_id == session_id
        ).delete()
        
        self.db.commit()
        
        return deleted > 0
    
    def _to_session_domain(self, db_session: ChatSessionModel) -> ChatSession:
        """Convert database model to domain entity"""
        return ChatSession(
            session_id=db_session.session_id,
            restaurant_id=db_session.restaurant_id,
            created_at=db_session.created_at,
            last_activity=db_session.last_activity
        )
    
    def _to_message_domain(self, db_message: ChatMessageModel) -> ChatMessage:
        """Convert database model to domain entity"""
        return ChatMessage(
            id=db_message.id,
            session_id=db_message.session_id,
            restaurant_id=db_message.restaurant_id,
            role=db_message.role,
            content=db_message.content,
            created_at=db_message.created_at
        )

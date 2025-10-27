"""
SQLAlchemy Contact Repository
Database implementation of contact message storage
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import ContactMessage
from app.database.models import ContactMessageModel
import uuid


class SQLAlchemyContactRepository:
    """
    SQLAlchemy implementation of contact repository
    Stores contact messages in database with full persistence
    """
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> List[ContactMessage]:
        """Get all contact messages from database"""
        db_messages = self.db.query(ContactMessageModel).all()
        
        return [
            self._to_domain(db_msg)
            for db_msg in db_messages
        ]
    
    def get_by_id(self, message_id: str) -> Optional[ContactMessage]:
        """Get contact message by ID from database"""
        db_message = self.db.query(ContactMessageModel).filter(
            ContactMessageModel.id == message_id
        ).first()
        
        if not db_message:
            return None
        
        return self._to_domain(db_message)
    
    def create(self, message: ContactMessage) -> ContactMessage:
        """Create a new contact message in database"""
        # Generate ID if not provided
        if not message.id:
            message.id = str(uuid.uuid4())[:8]
        
        # Convert domain entity to database model
        db_message = ContactMessageModel(
            id=message.id,
            restaurant_id=message.restaurant_id,
            name=message.name,
            email=message.email,
            subject=message.subject,
            message=message.message,
            created_at=message.created_at
        )
        
        # Add to database
        self.db.add(db_message)
        self.db.commit()
        self.db.refresh(db_message)
        
        return self._to_domain(db_message)
    
    def delete(self, message_id: str) -> bool:
        """Delete a contact message from database"""
        db_message = self.db.query(ContactMessageModel).filter(
            ContactMessageModel.id == message_id
        ).first()
        
        if not db_message:
            return False
        
        self.db.delete(db_message)
        self.db.commit()
        
        return True
    
    def get_by_restaurant(self, restaurant_id: str) -> List[ContactMessage]:
        """Get all contact messages for a specific restaurant"""
        db_messages = self.db.query(ContactMessageModel).filter(
            ContactMessageModel.restaurant_id == restaurant_id
        ).all()
        
        return [
            self._to_domain(db_msg)
            for db_msg in db_messages
        ]
    
    def _to_domain(self, db_message: ContactMessageModel) -> ContactMessage:
        """Convert database model to domain entity"""
        return ContactMessage(
            id=db_message.id,
            restaurant_id=db_message.restaurant_id,
            name=db_message.name,
            email=db_message.email,
            subject=db_message.subject,
            message=db_message.message,
            created_at=db_message.created_at
        )


"""
SQLAlchemy Database Models
Defines the database schema for persistent storage
"""
from sqlalchemy import Column, String, Integer, Text, DateTime, Index
from datetime import datetime
from .base import Base


class ReservationModel(Base):
    """
    Database model for restaurant reservations
    """
    __tablename__ = "reservations"
    
    # Primary Key
    id = Column(String(50), primary_key=True, index=True)
    
    # Restaurant Association
    restaurant_id = Column(String(100), nullable=False, index=True)
    
    # Customer Information
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20))
    
    # Reservation Details
    date = Column(String(20), nullable=False)  # YYYY-MM-DD format
    time = Column(String(10), nullable=False)  # HH:MM format
    party_size = Column(Integer, nullable=False)
    special_requests = Column(Text, nullable=True)
    
    # Status and Metadata
    status = Column(String(20), default="confirmed")
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    
    # Composite indexes for common queries
    __table_args__ = (
        Index('ix_restaurant_date', 'restaurant_id', 'date'),
        Index('ix_restaurant_status', 'restaurant_id', 'status'),
    )
    
    def __repr__(self):
        return f"<Reservation(id={self.id}, name={self.name}, restaurant={self.restaurant_id})>"


class ContactMessageModel(Base):
    """
    Database model for contact form messages
    """
    __tablename__ = "contact_messages"
    
    # Primary Key
    id = Column(String(50), primary_key=True, index=True)
    
    # Restaurant Association
    restaurant_id = Column(String(100), nullable=False, index=True)
    
    # Sender Information
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    subject = Column(String(200), nullable=True)
    
    # Message Content
    message = Column(Text, nullable=False)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    
    # Index for filtering by restaurant
    __table_args__ = (
        Index('ix_restaurant_created', 'restaurant_id', 'created_at'),
    )
    
    def __repr__(self):
        return f"<ContactMessage(id={self.id}, from={self.name}, restaurant={self.restaurant_id})>"


class ChatSessionModel(Base):
    """
    Database model for chat sessions
    """
    __tablename__ = "chat_sessions"
    
    # Primary Key
    session_id = Column(String(100), primary_key=True, index=True)
    
    # Restaurant Association
    restaurant_id = Column(String(100), nullable=False, index=True)
    
    # Session Metadata
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    last_activity = Column(DateTime, default=datetime.now, nullable=False)
    
    # Index for filtering by restaurant
    __table_args__ = (
        Index('ix_restaurant_session', 'restaurant_id', 'session_id'),
    )
    
    def __repr__(self):
        return f"<ChatSession(session_id={self.session_id}, restaurant={self.restaurant_id})>"


class ChatMessageModel(Base):
    """
    Database model for chat messages
    """
    __tablename__ = "chat_messages"
    
    # Primary Key
    id = Column(String(50), primary_key=True, index=True)
    
    # Session Association
    session_id = Column(String(100), nullable=False, index=True)
    restaurant_id = Column(String(100), nullable=False, index=True)
    
    # Message Content
    role = Column(String(20), nullable=False)  # 'user' or 'assistant'
    content = Column(Text, nullable=False)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    
    # Indexes for efficient queries
    __table_args__ = (
        Index('ix_session_created', 'session_id', 'created_at'),
        Index('ix_restaurant_session', 'restaurant_id', 'session_id'),
    )
    
    def __repr__(self):
        return f"<ChatMessage(id={self.id}, session={self.session_id}, role={self.role})>"
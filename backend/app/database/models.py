"""
SQLAlchemy Database Models
Defines the database schema for persistent storage
"""
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, Boolean, JSON, Index
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


class RestaurantModel(Base):
    """
    Database model for restaurant information
    """
    __tablename__ = "restaurants"
    
    # Primary Key
    id = Column(String(100), primary_key=True, index=True)
    
    # Basic Information
    name = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, nullable=False, index=True)
    tagline = Column(String(300))
    
    # Contact Information
    address = Column(String(300))
    phone = Column(String(20))
    email = Column(String(100))
    
    # Media URLs
    logo_url = Column(Text)
    hero_image_url = Column(Text)
    about_image_url = Column(Text)
    owner_image_url = Column(Text)
    
    # About Section
    story = Column(Text)
    cuisine_type = Column(String(100))
    owner_name = Column(String(100))
    owner_bio = Column(Text)
    
    # Business Hours (JSON format)
    # Example: {"0": null, "1": [11, 21], "2": [11, 21], ...}
    business_hours = Column(JSON)
    
    # Settings
    is_active = Column(Boolean, default=True)
    accepts_reservations = Column(Boolean, default=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    
    def __repr__(self):
        return f"<Restaurant(id={self.id}, name={self.name})>"


class MenuItemModel(Base):
    """
    Database model for menu items
    """
    __tablename__ = "menu_items"
    
    # Primary Key
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Restaurant Association
    restaurant_id = Column(String(100), nullable=False, index=True)
    
    # Item Information
    name = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    
    # Category and Tags
    category = Column(String(50), nullable=False)  # e.g., "appetizers", "signature_dishes"
    tags = Column(JSON)  # List of dietary tags: ["vegetarian", "gluten_free"]
    
    # Media
    image = Column(Text)
    
    # Display Settings
    is_available = Column(Boolean, default=True)
    display_order = Column(Integer, default=0)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    
    # Indexes
    __table_args__ = (
        Index('ix_restaurant_category', 'restaurant_id', 'category'),
        Index('ix_restaurant_available', 'restaurant_id', 'is_available'),
    )
    
    def __repr__(self):
        return f"<MenuItem(id={self.id}, name={self.name}, restaurant={self.restaurant_id})>"


class SystemPromptCacheModel(Base):
    """
    Database model for cached system prompts
    Stores pre-built prompts for each restaurant to improve performance
    """
    __tablename__ = "system_prompt_cache"
    
    # Primary Key
    restaurant_id = Column(String(100), primary_key=True, index=True)
    
    # Cached Prompt (can be very large - SQLite TEXT supports up to 1GB)
    prompt_text = Column(Text, nullable=False)
    
    # Versioning
    version = Column(Integer, default=1, nullable=False)
    
    # Metadata flags
    includes_menu = Column(Boolean, default=True)
    includes_hours = Column(Boolean, default=True)
    includes_about = Column(Boolean, default=True)
    
    # Token count estimate (for monitoring)
    estimated_tokens = Column(Integer, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    
    def __repr__(self):
        return f"<SystemPromptCache(restaurant_id={self.restaurant_id}, version={self.version})>"
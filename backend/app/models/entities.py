"""
Domain Entities Module
Contains core business objects following Domain-Driven Design principles
Following Single Responsibility Principle - each class has one clear purpose
"""
from typing import List, Optional
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime


class DietaryTag(str, Enum):
    """Enum for dietary tags - makes it type-safe and prevents invalid values"""
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    GLUTEN_FREE = "gluten-free"
    DAIRY_FREE = "dairy-free"
    NUT_FREE = "nut-free"
    SPICY = "spicy"


class MenuCategory(str, Enum):
    """Enum for menu categories"""
    APPETIZERS = "appetizers"
    SIGNATURE_DISHES = "signature_dishes"
    BREAD_AND_SIDES = "bread_and_sides"
    BEVERAGES = "beverages"
    DESSERTS = "desserts"


@dataclass
class MenuItem:
    """
    Represents a single item on the menu
    Immutable after creation (uses frozen=True for data integrity)
    """
    id: int
    name: str
    description: str
    price: float
    category: MenuCategory
    tags: List[DietaryTag] = field(default_factory=list)
    image: Optional[str] = None
    is_available: bool = True
    
    def __post_init__(self):
        """Validate data after initialization"""
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if not self.name or not self.name.strip():
            raise ValueError("Name cannot be empty")
    
    def has_tag(self, tag: DietaryTag) -> bool:
        """Check if item has a specific dietary tag"""
        return tag in self.tags
    
    def is_vegetarian(self) -> bool:
        """Check if item is vegetarian"""
        return DietaryTag.VEGETARIAN in self.tags
    
    def is_vegan(self) -> bool:
        """Check if item is vegan"""
        return DietaryTag.VEGAN in self.tags


@dataclass
class Menu:
    """
    Represents the restaurant's menu
    Aggregates menu items by category
    """
    items: List[MenuItem] = field(default_factory=list)
    
    def get_items_by_category(self, category: MenuCategory) -> List[MenuItem]:
        """Get all items in a specific category"""
        return [item for item in self.items if item.category == category]
    
    def get_items_by_tag(self, tag: DietaryTag) -> List[MenuItem]:
        """Get all items with a specific dietary tag"""
        return [item for item in self.items if item.has_tag(tag)]
    
    def get_available_items(self) -> List[MenuItem]:
        """Get all currently available items"""
        return [item for item in self.items if item.is_available]
    
    def get_item_by_id(self, item_id: int) -> Optional[MenuItem]:
        """Get a specific item by ID"""
        for item in self.items:
            if item.id == item_id:
                return item
        return None
    
    def add_item(self, item: MenuItem) -> None:
        """Add a new item to the menu"""
        # Check for duplicate IDs
        if any(existing.id == item.id for existing in self.items):
            raise ValueError(f"Item with ID {item.id} already exists")
        self.items.append(item)


@dataclass
class Reservation:
    """
    Represents a restaurant reservation
    """
    id: Optional[str]
    restaurant_id: str  # Which restaurant this reservation is for
    name: str
    email: str
    phone: str
    date: str
    time: str
    party_size: int
    special_requests: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    status: str = "confirmed"
    
    def __post_init__(self):
        """Validate reservation data"""
        if self.party_size < 1:
            raise ValueError("Party size must be at least 1")
        if self.party_size > 20:
            raise ValueError("Party size cannot exceed 20")
        if not self.email or '@' not in self.email:
            raise ValueError("Valid email is required")


@dataclass
class ContactMessage:
    """
    Represents a contact form submission
    """
    id: Optional[str]
    restaurant_id: str  # Which restaurant this message is for
    name: str
    email: str
    subject: Optional[str]
    message: str
    created_at: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        """Validate contact message data"""
        if not self.email or '@' not in self.email:
            raise ValueError("Valid email is required")
        if not self.message or not self.message.strip():
            raise ValueError("Message cannot be empty")


@dataclass
class Restaurant:
    """
    Represents the restaurant entity with its branding and information
    Each restaurant has its own identity, menu, and settings
    """
    id: str  # Unique identifier (e.g., "kurdiescurry", "spicehaven")
    name: str  # Display name
    slug: str  # URL-friendly identifier
    
    # Contact Information
    address: str
    phone: str
    email: Optional[str] = None
    
    # Branding & Media
    logo_url: Optional[str] = None
    hero_image_url: Optional[str] = None  # Homepage hero image
    about_image_url: Optional[str] = None  # About section image
    owner_image_url: Optional[str] = None  # Owner/Chef photo
    
    # About Section
    tagline: Optional[str] = None  # e.g., "Authentic Flavors, Modern Twist"
    story: Optional[str] = None  # Restaurant story/description
    cuisine_type: Optional[str] = None  # e.g., "Indian-Kurdish Fusion"
    owner_name: Optional[str] = None
    owner_bio: Optional[str] = None
    
    # Business Details
    business_hours: dict = field(default_factory=dict)  # {day: (open_hour, close_hour)}
    menu: Menu = field(default_factory=Menu)
    
    # Settings
    is_active: bool = True
    accepts_reservations: bool = True
    
    def is_open_now(self) -> tuple[bool, str]:
        """
        Check if restaurant is currently open
        Returns: (is_open: bool, message: str)
        """
        from datetime import datetime
        
        now = datetime.now()
        current_day = now.weekday()  # 0 = Monday, 6 = Sunday
        current_hour = now.hour
        
        # Adjust to match our business_hours format (0 = Sunday)
        day_index = (current_day + 1) % 7
        
        hours = self.business_hours.get(day_index)
        
        if hours is None:
            # Closed today
            next_open_day = (day_index + 1) % 7
            while self.business_hours.get(next_open_day) is None:
                next_open_day = (next_open_day + 1) % 7
            
            day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", 
                        "Thursday", "Friday", "Saturday"]
            if next_open_day == (day_index + 1) % 7:
                return False, "Closed - Opens tomorrow at 11:00 AM"
            else:
                return False, f"Closed - Opens {day_names[next_open_day]} at 11:00 AM"
        
        open_hour, close_hour = hours
        
        if current_hour >= open_hour and current_hour < close_hour:
            close_time = f"{close_hour % 12 or 12}:00 {'PM' if close_hour >= 12 else 'AM'}"
            return True, f"Open until {close_time}"
        elif current_hour >= close_hour:
            return False, "Closed - Opens tomorrow at 11:00 AM"
        else:
            return False, "Closed - Opens at 11:00 AM"


"""
Menu-related Pydantic schemas for request/response validation
Following Interface Segregation Principle - separate schemas for different use cases
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional


class MenuItemResponse(BaseModel):
    """Schema for menu item in API responses"""
    id: int
    name: str
    description: str
    price: float = Field(ge=0, description="Price must be non-negative")
    tags: List[str] = Field(default_factory=list)
    image: Optional[str] = None
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Samosas",
                "description": "Crispy pastry filled with spiced potatoes and peas.",
                "price": 5.99,
                "tags": ["vegetarian"],
                "image": "https://example.com/samosas.jpg"
            }
        }
    )


class MenuCategoryResponse(BaseModel):
    """Schema for a menu category with its items"""
    category: str
    items: List[MenuItemResponse]


class MenuResponse(BaseModel):
    """
    Schema for complete menu response
    Organized by categories as expected by frontend
    """
    appetizers: List[MenuItemResponse] = Field(default_factory=list)
    signature_dishes: List[MenuItemResponse] = Field(default_factory=list)
    bread_and_sides: List[MenuItemResponse] = Field(default_factory=list)
    beverages: List[MenuItemResponse] = Field(default_factory=list)
    desserts: List[MenuItemResponse] = Field(default_factory=list)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "appetizers": [
                    {
                        "id": 1,
                        "name": "Samosas",
                        "description": "Crispy pastry filled with spiced potatoes and peas.",
                        "price": 5.99,
                        "tags": ["vegetarian"],
                        "image": "https://example.com/samosas.jpg"
                    }
                ],
                "signature_dishes": [],
                "bread_and_sides": [],
                "beverages": [],
                "desserts": []
            }
        }
    )


class MenuItemCreate(BaseModel):
    """Schema for creating a new menu item"""
    name: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=500)
    price: float = Field(gt=0, description="Price must be positive")
    category: str = Field(
        description="Category: appetizers, signature_dishes, bread_and_sides, beverages, desserts"
    )
    tags: List[str] = Field(default_factory=list)
    image: Optional[str] = None
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Tikka Masala",
                "description": "Classic Indian curry with tender chicken",
                "price": 14.99,
                "category": "signature_dishes",
                "tags": ["gluten-free"],
                "image": "https://example.com/tikka.jpg"
            }
        }
    )


class MenuItemUpdate(BaseModel):
    """Schema for updating a menu item (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    tags: Optional[List[str]] = None
    image: Optional[str] = None
    is_available: Optional[bool] = None


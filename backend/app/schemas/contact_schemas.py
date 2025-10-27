"""
Contact form related Pydantic schemas
"""
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class ContactFormSubmit(BaseModel):
    """Schema for contact form submission"""
    restaurant_id: str = Field(description="Restaurant ID")
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    subject: Optional[str] = Field(None, max_length=200)
    message: str = Field(min_length=1, max_length=1000)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "restaurant_id": "kurdiescurry",
                "name": "Jane Smith",
                "email": "jane@example.com",
                "subject": "Catering inquiry",
                "message": "I'd like to know about your catering services for 50 people."
            }
        }
    )


class ContactFormResponse(BaseModel):
    """Schema for contact form response"""
    success: bool
    message: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Message sent! We will get back to you."
            }
        }
    )


class ContactMessageDetail(BaseModel):
    """Schema for detailed contact message (admin view)"""
    id: str
    restaurant_id: str
    name: str
    email: str
    subject: Optional[str]
    message: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


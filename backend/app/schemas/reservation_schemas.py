"""
Reservation-related Pydantic schemas
"""
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime


class ReservationCreate(BaseModel):
    """Schema for creating a new reservation"""
    restaurant_id: str = Field(description="Restaurant ID")
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    phone: str = Field(min_length=10, max_length=20)
    date: str = Field(description="Date in YYYY-MM-DD format")
    time: str = Field(description="Time in HH:MM format")
    party_size: int = Field(ge=1, le=20, description="Number of guests (1-20)")
    special_requests: Optional[str] = Field(None, max_length=500)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "restaurant_id": "kurdiescurry",
                "name": "John Doe",
                "email": "john@example.com",
                "phone": "(555) 123-4567",
                "date": "2024-12-25",
                "time": "19:00",
                "party_size": 4,
                "special_requests": "Window seat preferred"
            }
        }
    )


class ReservationResponse(BaseModel):
    """Schema for reservation in API response"""
    id: str
    restaurant_id: str
    name: str
    email: str
    phone: str
    date: str
    time: str
    party_size: int
    special_requests: Optional[str] = None
    status: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ReservationConfirmation(BaseModel):
    """Schema for reservation confirmation response"""
    success: bool
    message: str
    reservation_id: str
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Reservation confirmed! See you soon.",
                "reservation_id": "abc123xyz"
            }
        }
    )


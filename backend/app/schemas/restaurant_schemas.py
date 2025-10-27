"""
Restaurant-related Pydantic schemas
"""
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import Optional


class RestaurantStatusResponse(BaseModel):
    """Schema for restaurant open/closed status"""
    isOpen: bool = Field(alias="isOpen")
    message: str
    
    model_config = ConfigDict(
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "isOpen": True,
                "message": "Open until 9:00 PM"
            }
        }
    )


class RestaurantBrandingResponse(BaseModel):
    """Schema for restaurant branding assets"""
    logo_url: Optional[str] = None
    hero_image_url: Optional[str] = None
    about_image_url: Optional[str] = None
    owner_image_url: Optional[str] = None


class RestaurantAboutResponse(BaseModel):
    """Schema for restaurant about information"""
    story: Optional[str] = None
    cuisine_type: Optional[str] = None
    owner_name: Optional[str] = None
    owner_bio: Optional[str] = None


class RestaurantResponse(BaseModel):
    """Schema for complete restaurant information"""
    id: str
    name: str
    slug: str
    tagline: Optional[str] = None
    
    # Contact
    address: str
    phone: str
    email: Optional[str] = None
    
    # Branding
    logo_url: Optional[str] = None
    hero_image_url: Optional[str] = None
    about_image_url: Optional[str] = None
    owner_image_url: Optional[str] = None
    
    # About
    story: Optional[str] = None
    cuisine_type: Optional[str] = None
    owner_name: Optional[str] = None
    owner_bio: Optional[str] = None
    
    # Status
    is_active: bool = True
    accepts_reservations: bool = True
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "kurdiescurry",
                "name": "Kurdie's Curry",
                "slug": "kurdiescurry",
                "tagline": "Authentic Flavors, Modern Twist",
                "address": "1337 N Spice Rd, Prescott Valley, AZ 86314",
                "phone": "(928) 555-1337",
                "email": "info@kurdiescurry.com",
                "hero_image_url": "https://example.com/hero.jpg",
                "story": "Our story began with a dream...",
                "is_active": True
            }
        }
    )


class RestaurantListResponse(BaseModel):
    """Schema for restaurant list item"""
    id: str
    name: str
    slug: str
    tagline: Optional[str] = None
    cuisine_type: Optional[str] = None
    logo_url: Optional[str] = None
    is_active: bool = True


class RestaurantInfoResponse(BaseModel):
    """Schema for basic restaurant information"""
    name: str
    address: str
    phone: str
    email: Optional[str] = None
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Kurdie's Curry",
                "address": "1337 N Spice Rd, Prescott Valley, AZ 86314",
                "phone": "(928) 555-1337",
                "email": "info@kurdiescurry.com"
            }
        }
    )


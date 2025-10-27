"""
Restaurant Service - Business Logic Layer
Handles restaurant information and status
"""
from typing import List, Optional
from app.models import Restaurant
from app.repositories import IRestaurantRepository
from app.schemas import (
    RestaurantStatusResponse, 
    RestaurantInfoResponse,
    RestaurantResponse,
    RestaurantListResponse
)


class RestaurantService:
    """
    Service for restaurant operations
    Handles restaurant status, information, and management
    """
    
    def __init__(self, restaurant_repository: IRestaurantRepository):
        self._repository = restaurant_repository
    
    def get_all_restaurants(self) -> List[RestaurantListResponse]:
        """Get all active restaurants"""
        restaurants = self._repository.get_all()
        
        return [
            RestaurantListResponse(
                id=r.id,
                name=r.name,
                slug=r.slug,
                tagline=r.tagline,
                cuisine_type=r.cuisine_type,
                logo_url=r.logo_url,
                is_active=r.is_active
            )
            for r in restaurants
        ]
    
    def get_restaurant(self, restaurant_id: str) -> Optional[RestaurantResponse]:
        """Get complete restaurant details"""
        restaurant = self._repository.get_by_id(restaurant_id)
        
        if not restaurant:
            return None
        
        return RestaurantResponse(
            id=restaurant.id,
            name=restaurant.name,
            slug=restaurant.slug,
            tagline=restaurant.tagline,
            address=restaurant.address,
            phone=restaurant.phone,
            email=restaurant.email,
            logo_url=restaurant.logo_url,
            hero_image_url=restaurant.hero_image_url,
            about_image_url=restaurant.about_image_url,
            owner_image_url=restaurant.owner_image_url,
            story=restaurant.story,
            cuisine_type=restaurant.cuisine_type,
            owner_name=restaurant.owner_name,
            owner_bio=restaurant.owner_bio,
            is_active=restaurant.is_active,
            accepts_reservations=restaurant.accepts_reservations
        )
    
    def get_status(self, restaurant_id: str) -> Optional[RestaurantStatusResponse]:
        """Get current restaurant status (open/closed)"""
        restaurant = self._repository.get_by_id(restaurant_id)
        
        if not restaurant:
            return None
        
        is_open, message = restaurant.is_open_now()
        
        return RestaurantStatusResponse(
            isOpen=is_open,
            message=message
        )
    
    def get_info(self, restaurant_id: str) -> Optional[RestaurantInfoResponse]:
        """Get restaurant basic information"""
        restaurant = self._repository.get_by_id(restaurant_id)
        
        if not restaurant:
            return None
        
        return RestaurantInfoResponse(
            name=restaurant.name,
            address=restaurant.address,
            phone=restaurant.phone,
            email=restaurant.email
        )
    
    def get_business_hours(self, restaurant_id: str) -> Optional[dict]:
        """Get business hours"""
        restaurant = self._repository.get_by_id(restaurant_id)
        
        if not restaurant:
            return None
        
        day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", 
                    "Thursday", "Friday", "Saturday"]
        
        formatted_hours = {}
        for day_index, hours in restaurant.business_hours.items():
            day_name = day_names[day_index]
            if hours is None:
                formatted_hours[day_name] = "CLOSED"
            else:
                open_hour, close_hour = hours
                open_time = f"{open_hour % 12 or 12}:00 {'PM' if open_hour >= 12 else 'AM'}"
                close_time = f"{close_hour % 12 or 12}:00 {'PM' if close_hour >= 12 else 'AM'}"
                formatted_hours[day_name] = f"{open_time} - {close_time}"
        
        return formatted_hours


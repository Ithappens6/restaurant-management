"""
Restaurant Repository Implementation
Handles data access for restaurants
"""
from typing import List, Optional
from app.models import Restaurant


class IRestaurantRepository:
    """Interface for restaurant repository"""
    
    def get_all(self) -> List[Restaurant]:
        """Get all active restaurants"""
        raise NotImplementedError
    
    def get_by_id(self, restaurant_id: str) -> Optional[Restaurant]:
        """Get restaurant by ID"""
        raise NotImplementedError
    
    def get_by_slug(self, slug: str) -> Optional[Restaurant]:
        """Get restaurant by URL slug"""
        raise NotImplementedError
    
    def create(self, restaurant: Restaurant) -> Restaurant:
        """Create a new restaurant"""
        raise NotImplementedError


class InMemoryRestaurantRepository(IRestaurantRepository):
    """
    In-memory implementation of restaurant repository
    Stores restaurants in memory
    """
    
    def __init__(self, restaurants: List[Restaurant] = None):
        self._restaurants: List[Restaurant] = restaurants or []
    
    def get_all(self) -> List[Restaurant]:
        """Get all active restaurants"""
        return [r for r in self._restaurants if r.is_active]
    
    def get_by_id(self, restaurant_id: str) -> Optional[Restaurant]:
        """Get restaurant by ID"""
        for restaurant in self._restaurants:
            if restaurant.id == restaurant_id:
                return restaurant
        return None
    
    def get_by_slug(self, slug: str) -> Optional[Restaurant]:
        """Get restaurant by URL slug"""
        for restaurant in self._restaurants:
            if restaurant.slug == slug:
                return restaurant
        return None
    
    def create(self, restaurant: Restaurant) -> Restaurant:
        """Create a new restaurant"""
        # Check for duplicate IDs or slugs
        if any(r.id == restaurant.id for r in self._restaurants):
            raise ValueError(f"Restaurant with ID {restaurant.id} already exists")
        if any(r.slug == restaurant.slug for r in self._restaurants):
            raise ValueError(f"Restaurant with slug {restaurant.slug} already exists")
        
        self._restaurants.append(restaurant)
        return restaurant
    
    def update(self, restaurant_id: str, updated_data: dict) -> Optional[Restaurant]:
        """Update a restaurant"""
        restaurant = self.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        # In a real implementation, update the restaurant fields
        return restaurant
    
    def delete(self, restaurant_id: str) -> bool:
        """Delete (deactivate) a restaurant"""
        restaurant = self.get_by_id(restaurant_id)
        if not restaurant:
            return False
        
        restaurant.is_active = False
        return True


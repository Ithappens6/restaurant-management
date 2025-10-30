"""
Menu Service - Business Logic Layer
Handles menu-related business operations
Following Single Responsibility and Dependency Inversion principles
"""
from typing import Dict, List, Optional
from app.models import MenuItem, MenuCategory
from app.repositories import IMenuRepository, IRestaurantRepository
from app.schemas import MenuItemResponse


class MenuService:
    """
    Service for menu operations
    Depends on abstraction (IMenuRepository) not concrete implementation
    """
    
    def __init__(self, restaurant_repository: IRestaurantRepository):
        self._restaurant_repo = restaurant_repository
    
    def get_menu_grouped_by_category(self, restaurant_id: str, category_filter: Optional[str] = None) -> Optional[Dict[str, List[MenuItemResponse]]]:
        """
        Get menu organized by categories for a specific restaurant
        Returns data in the format expected by frontend
        
        Args:
            restaurant_id: The restaurant identifier
            category_filter: Optional category to filter by (e.g., 'signature_dishes')
        """
        restaurant = self._restaurant_repo.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        menu = restaurant.menu
        
        # Group items by category
        grouped_menu = {
            "appetizers": [],
            "signature_dishes": [],
            "bread_and_sides": [],
            "beverages": [],
            "desserts": [],
        }
        
        for item in menu.get_available_items():
            # Convert domain entity to response schema
            item_response = MenuItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                price=item.price,
                tags=[tag.value for tag in item.tags],
                image=item.image
            )
            
            # Add to appropriate category
            category_key = item.category.value
            if category_key in grouped_menu:
                grouped_menu[category_key].append(item_response)
        
        # If category filter is provided, return only that category
        if category_filter:
            if category_filter in grouped_menu:
                return {category_filter: grouped_menu[category_filter]}
            else:
                # Return empty dict if category doesn't exist
                return {}
        
        return grouped_menu
    
    def get_item_by_id(self, restaurant_id: str, item_id: int) -> Optional[MenuItemResponse]:
        """Get a specific menu item by ID"""
        restaurant = self._restaurant_repo.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        item = restaurant.menu.get_item_by_id(item_id)
        
        if not item:
            return None
        
        return MenuItemResponse(
            id=item.id,
            name=item.name,
            description=item.description,
            price=item.price,
            tags=[tag.value for tag in item.tags],
            image=item.image
        )
    
    def get_items_by_category(self, restaurant_id: str, category: str) -> Optional[List[MenuItemResponse]]:
        """Get all items in a specific category"""
        restaurant = self._restaurant_repo.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        try:
            menu_category = MenuCategory(category)
        except ValueError:
            return []
        
        items = restaurant.menu.get_items_by_category(menu_category)
        
        return [
            MenuItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                price=item.price,
                tags=[tag.value for tag in item.tags],
                image=item.image
            )
            for item in items if item.is_available
        ]
    
    def search_items(self, restaurant_id: str, query: str) -> Optional[List[MenuItemResponse]]:
        """Search menu items by name or description"""
        restaurant = self._restaurant_repo.get_by_id(restaurant_id)
        if not restaurant:
            return None
        
        menu = restaurant.menu
        query_lower = query.lower()
        
        matching_items = [
            item for item in menu.get_available_items()
            if query_lower in item.name.lower() or query_lower in item.description.lower()
        ]
        
        return [
            MenuItemResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                price=item.price,
                tags=[tag.value for tag in item.tags],
                image=item.image
            )
            for item in matching_items
        ]


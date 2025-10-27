"""
Menu Repository Implementation
Handles data access for menu items
Following Repository Pattern and Single Responsibility Principle
"""
from typing import List, Optional
from app.models import MenuItem, Menu, MenuCategory, DietaryTag


class IMenuRepository:
    """Interface for menu repository"""
    
    def get_menu(self) -> Menu:
        """Get the complete menu"""
        raise NotImplementedError
    
    def get_item_by_id(self, item_id: int) -> Optional[MenuItem]:
        """Get a specific menu item"""
        raise NotImplementedError
    
    def get_items_by_category(self, category: MenuCategory) -> List[MenuItem]:
        """Get items by category"""
        raise NotImplementedError
    
    def get_items_by_tag(self, tag: DietaryTag) -> List[MenuItem]:
        """Get items by dietary tag"""
        raise NotImplementedError


class InMemoryMenuRepository(IMenuRepository):
    """
    In-memory implementation of menu repository
    In a real application, this would be replaced with a database implementation
    """
    
    def __init__(self, menu: Menu):
        self._menu = menu
    
    def get_menu(self) -> Menu:
        """Get the complete menu"""
        return self._menu
    
    def get_item_by_id(self, item_id: int) -> Optional[MenuItem]:
        """Get a specific menu item"""
        return self._menu.get_item_by_id(item_id)
    
    def get_items_by_category(self, category: MenuCategory) -> List[MenuItem]:
        """Get items by category"""
        return self._menu.get_items_by_category(category)
    
    def get_items_by_tag(self, tag: DietaryTag) -> List[MenuItem]:
        """Get items by dietary tag"""
        return self._menu.get_items_by_tag(tag)
    
    def add_item(self, item: MenuItem) -> MenuItem:
        """Add a new menu item"""
        self._menu.add_item(item)
        return item
    
    def update_item(self, item_id: int, updated_data: dict) -> Optional[MenuItem]:
        """Update a menu item"""
        item = self.get_item_by_id(item_id)
        if not item:
            return None
        
        # In a real implementation, we'd update the item
        # For now, this is a simplified version
        return item
    
    def delete_item(self, item_id: int) -> bool:
        """Delete a menu item"""
        item = self.get_item_by_id(item_id)
        if not item:
            return False
        
        self._menu.items = [i for i in self._menu.items if i.id != item_id]
        return True


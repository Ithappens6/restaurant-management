"""
Base Repository Interface
Following Interface Segregation and Dependency Inversion principles
This allows us to swap implementations (e.g., from in-memory to database)
"""
from abc import ABC, abstractmethod
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


class IRepository(ABC, Generic[T]):
    """
    Generic repository interface
    Defines contract that all repositories must follow
    """
    
    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all items"""
        pass
    
    @abstractmethod
    def get_by_id(self, item_id: str) -> Optional[T]:
        """Get item by ID"""
        pass
    
    @abstractmethod
    def create(self, item: T) -> T:
        """Create a new item"""
        pass
    
    @abstractmethod
    def update(self, item_id: str, item: T) -> Optional[T]:
        """Update an existing item"""
        pass
    
    @abstractmethod
    def delete(self, item_id: str) -> bool:
        """Delete an item"""
        pass


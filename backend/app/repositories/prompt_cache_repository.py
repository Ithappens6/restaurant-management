"""
Prompt Cache Repository
Handles database operations for cached system prompts
"""
from sqlalchemy.orm import Session
from app.database.models import SystemPromptCacheModel
from datetime import datetime
from typing import Optional


class PromptCacheRepository:
    """Repository for managing cached system prompts"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_prompt(self, restaurant_id: str) -> Optional[str]:
        """
        Get cached prompt for a restaurant
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            Cached prompt text or None if not found
        """
        cache = self.db.query(SystemPromptCacheModel).filter(
            SystemPromptCacheModel.restaurant_id == restaurant_id
        ).first()
        
        return cache.prompt_text if cache else None
    
    def get_cache_metadata(self, restaurant_id: str) -> Optional[SystemPromptCacheModel]:
        """
        Get full cache record with metadata
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            SystemPromptCacheModel or None
        """
        return self.db.query(SystemPromptCacheModel).filter(
            SystemPromptCacheModel.restaurant_id == restaurant_id
        ).first()
    
    def set_prompt(
        self, 
        restaurant_id: str, 
        prompt_text: str,
        includes_menu: bool = True,
        includes_hours: bool = True,
        includes_about: bool = True,
        estimated_tokens: Optional[int] = None
    ) -> SystemPromptCacheModel:
        """
        Set or update cached prompt for a restaurant
        
        Args:
            restaurant_id: Restaurant identifier
            prompt_text: The complete system prompt text
            includes_menu: Whether menu data is included
            includes_hours: Whether business hours are included
            includes_about: Whether about/story is included
            estimated_tokens: Estimated token count
            
        Returns:
            Updated SystemPromptCacheModel
        """
        cache = self.db.query(SystemPromptCacheModel).filter(
            SystemPromptCacheModel.restaurant_id == restaurant_id
        ).first()
        
        if cache:
            # Update existing cache
            cache.prompt_text = prompt_text
            cache.version += 1
            cache.includes_menu = includes_menu
            cache.includes_hours = includes_hours
            cache.includes_about = includes_about
            cache.estimated_tokens = estimated_tokens
            cache.updated_at = datetime.now()
        else:
            # Create new cache
            cache = SystemPromptCacheModel(
                restaurant_id=restaurant_id,
                prompt_text=prompt_text,
                version=1,
                includes_menu=includes_menu,
                includes_hours=includes_hours,
                includes_about=includes_about,
                estimated_tokens=estimated_tokens,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            self.db.add(cache)
        
        self.db.commit()
        self.db.refresh(cache)
        return cache
    
    def invalidate(self, restaurant_id: str) -> bool:
        """
        Delete cached prompt (forces rebuild on next request)
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            True if cache was deleted, False if it didn't exist
        """
        result = self.db.query(SystemPromptCacheModel).filter(
            SystemPromptCacheModel.restaurant_id == restaurant_id
        ).delete()
        
        self.db.commit()
        return result > 0
    
    def get_all_caches(self):
        """Get all cached prompts (for admin/monitoring)"""
        return self.db.query(SystemPromptCacheModel).all()
    
    def get_cache_stats(self, restaurant_id: str) -> dict:
        """
        Get statistics about a cached prompt
        
        Args:
            restaurant_id: Restaurant identifier
            
        Returns:
            Dictionary with cache statistics
        """
        cache = self.get_cache_metadata(restaurant_id)
        
        if not cache:
            return {"exists": False}
        
        return {
            "exists": True,
            "version": cache.version,
            "size_bytes": len(cache.prompt_text),
            "size_kb": len(cache.prompt_text) / 1024,
            "estimated_tokens": cache.estimated_tokens,
            "includes_menu": cache.includes_menu,
            "includes_hours": cache.includes_hours,
            "includes_about": cache.includes_about,
            "created_at": cache.created_at.isoformat(),
            "updated_at": cache.updated_at.isoformat(),
            "age_seconds": (datetime.now() - cache.updated_at).total_seconds()
        }


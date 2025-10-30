"""
Menu API Routes
Defines HTTP endpoints for menu operations
Following REST principles
"""
from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List
from app.schemas import MenuResponse, MenuItemResponse
from app.services import MenuService

router = APIRouter(prefix="/restaurants/{restaurant_id}/menu", tags=["Menu"])


def get_menu_service() -> MenuService:
    """Dependency injection for MenuService"""
    from app.core.dependencies import get_menu_service as _get_service
    return _get_service()


@router.get("", response_model=MenuResponse, summary="Get complete menu")
async def get_menu(
    restaurant_id: str,
    category: str = Query(None, description="Optional category filter (e.g., 'signature_dishes')"),
    service: MenuService = Depends(get_menu_service)
):
    """
    Get the complete restaurant menu organized by categories
    
    Returns menu items grouped by:
    - appetizers
    - signature_dishes
    - bread_and_sides
    - beverages
    - desserts
    
    - **restaurant_id**: Unique restaurant identifier
    - **category**: Optional - filter to return only one category
    """
    menu_data = service.get_menu_grouped_by_category(restaurant_id, category_filter=category)
    if menu_data is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return MenuResponse(**menu_data)


@router.get("/items/{item_id}", response_model=MenuItemResponse, summary="Get specific menu item")
async def get_menu_item(
    restaurant_id: str,
    item_id: int,
    service: MenuService = Depends(get_menu_service)
):
    """
    Get a specific menu item by its ID
    
    - **restaurant_id**: Unique restaurant identifier
    - **item_id**: The ID of the menu item
    """
    item = service.get_item_by_id(restaurant_id, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


@router.get("/category/{category}", response_model=List[MenuItemResponse], summary="Get items by category")
async def get_items_by_category(
    restaurant_id: str,
    category: str,
    service: MenuService = Depends(get_menu_service)
):
    """
    Get all menu items in a specific category
    
    - **restaurant_id**: Unique restaurant identifier
    - **category**: One of: appetizers, signature_dishes, bread_and_sides, beverages, desserts
    """
    items = service.get_items_by_category(restaurant_id, category)
    if items is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    if not items:
        raise HTTPException(status_code=404, detail=f"No items found in category: {category}")
    return items


@router.get("/search", response_model=List[MenuItemResponse], summary="Search menu items")
async def search_menu(
    restaurant_id: str,
    query: str = Query(..., min_length=1, description="Search query"),
    service: MenuService = Depends(get_menu_service)
):
    """
    Search menu items by name or description
    
    - **restaurant_id**: Unique restaurant identifier
    - **query**: Search term to look for in item names and descriptions
    """
    items = service.search_items(restaurant_id, query)
    if items is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return items

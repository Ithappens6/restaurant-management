"""
Restaurant API Routes
Defines HTTP endpoints for restaurant information and status
"""
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.schemas import (
    RestaurantStatusResponse, 
    RestaurantInfoResponse,
    RestaurantResponse,
    RestaurantListResponse
)
from app.services import RestaurantService

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


def get_restaurant_service() -> RestaurantService:
    """Dependency injection for RestaurantService"""
    from app.core.dependencies import get_restaurant_service as _get_service
    return _get_service()


@router.get("", response_model=List[RestaurantListResponse], summary="Get all restaurants")
async def list_restaurants(service: RestaurantService = Depends(get_restaurant_service)):
    """
    Get all active restaurants
    
    Returns a list of restaurants with basic information
    """
    return service.get_all_restaurants()


@router.get("/{restaurant_id}", response_model=RestaurantResponse, summary="Get restaurant details")
async def get_restaurant(
    restaurant_id: str,
    service: RestaurantService = Depends(get_restaurant_service)
):
    """
    Get complete restaurant details including branding and about information
    
    - **restaurant_id**: Unique restaurant identifier (e.g., "kurdiescurry")
    """
    restaurant = service.get_restaurant(restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant


@router.get("/{restaurant_id}/status", response_model=RestaurantStatusResponse, summary="Get restaurant status")
async def get_status(
    restaurant_id: str,
    service: RestaurantService = Depends(get_restaurant_service)
):
    """
    Get current restaurant status (open/closed)
    
    Returns whether the restaurant is currently open based on business hours
    and a message with additional information
    
    - **restaurant_id**: Unique restaurant identifier
    """
    status = service.get_status(restaurant_id)
    if not status:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return status


@router.get("/{restaurant_id}/info", response_model=RestaurantInfoResponse, summary="Get restaurant information")
async def get_info(
    restaurant_id: str,
    service: RestaurantService = Depends(get_restaurant_service)
):
    """
    Get restaurant contact information
    
    Returns restaurant name, address, phone number, and email
    
    - **restaurant_id**: Unique restaurant identifier
    """
    info = service.get_info(restaurant_id)
    if not info:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return info


@router.get("/{restaurant_id}/hours", summary="Get business hours")
async def get_hours(
    restaurant_id: str,
    service: RestaurantService = Depends(get_restaurant_service)
):
    """
    Get restaurant business hours
    
    Returns operating hours for each day of the week
    
    - **restaurant_id**: Unique restaurant identifier
    """
    hours = service.get_business_hours(restaurant_id)
    if not hours:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return hours

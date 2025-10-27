"""
Dependency Injection Container
Provides singleton instances of services and repositories
Following Dependency Inversion Principle
"""
from sqlalchemy.orm import Session
from app.repositories import (
    InMemoryRestaurantRepository,
    SQLAlchemyReservationRepository,
    SQLAlchemyContactRepository,
)
from app.services import (
    MenuService,
    ReservationService,
    ContactService,
    RestaurantService,
)
from app.data import create_sample_restaurants
from app.database import get_db


# Create sample restaurants
_restaurants = create_sample_restaurants()

# Create restaurant repository with sample data (restaurants stay in memory)
_restaurant_repository = InMemoryRestaurantRepository(_restaurants)

# Create service instances (without database dependencies)
_menu_service = MenuService(_restaurant_repository)
_restaurant_service = RestaurantService(_restaurant_repository)


# Dependency provider functions

def get_restaurant_repository():
    """Get restaurant repository instance (in-memory)"""
    return _restaurant_repository


def get_menu_service() -> MenuService:
    """Get menu service instance"""
    return _menu_service


def get_restaurant_service() -> RestaurantService:
    """Get restaurant service instance"""
    return _restaurant_service


def get_reservation_service(db: Session = None) -> ReservationService:
    """
    Get reservation service instance with database session
    
    Note: db parameter will be injected by FastAPI's Depends(get_db)
    """
    if db is None:
        # Fallback for testing or non-request contexts
        from app.database import SessionLocal
        db = SessionLocal()
    
    reservation_repository = SQLAlchemyReservationRepository(db)
    return ReservationService(reservation_repository)


def get_contact_service(db: Session = None) -> ContactService:
    """
    Get contact service instance with database session
    
    Note: db parameter will be injected by FastAPI's Depends(get_db)
    """
    if db is None:
        # Fallback for testing or non-request contexts
        from app.database import SessionLocal
        db = SessionLocal()
    
    contact_repository = SQLAlchemyContactRepository(db)
    return ContactService(contact_repository)

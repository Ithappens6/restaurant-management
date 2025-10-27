"""Repositories module - Data access layer"""
from .menu_repository import IMenuRepository, InMemoryMenuRepository
from .reservation_repository import IReservationRepository, InMemoryReservationRepository
from .contact_repository import IContactRepository, InMemoryContactRepository
from .restaurant_repository import IRestaurantRepository, InMemoryRestaurantRepository
from .sqlalchemy_reservation_repository import SQLAlchemyReservationRepository
from .sqlalchemy_contact_repository import SQLAlchemyContactRepository

__all__ = [
    "IMenuRepository",
    "InMemoryMenuRepository",
    "IReservationRepository",
    "InMemoryReservationRepository",
    "IContactRepository",
    "InMemoryContactRepository",
    "IRestaurantRepository",
    "InMemoryRestaurantRepository",
    "SQLAlchemyReservationRepository",
    "SQLAlchemyContactRepository",
]


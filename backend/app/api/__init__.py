"""API module - HTTP endpoints"""
from .menu_routes import router as menu_router
from .reservation_routes import router as reservation_router
from .contact_routes import router as contact_router
from .restaurant_routes import router as restaurant_router
from .simple_chat_routes import router as chat_router

__all__ = [
    "menu_router",
    "reservation_router",
    "contact_router",
    "restaurant_router",
    "chat_router",
]


"""
Main FastAPI Application
Entry point for the restaurant backend API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import (
    menu_router,
    reservation_router,
    contact_router,
    restaurant_router,
    chat_router,
)

# Create FastAPI application
app = FastAPI(
    title="Multi-Restaurant Management API",
    description="""
    ## 🍽️ Restaurant Management System
    
    A comprehensive backend API for managing multiple restaurants with complete branding, 
    menus, reservations, and customer communications.
    
    ### Key Features
    
    * **Multi-Restaurant Support** - Manage unlimited restaurants
    * **Complete Branding** - Hero images, logos, owner photos, and stories
    * **Menu Management** - Organize items by categories with dietary tags
    * **Reservations** - Accept and manage table reservations
    * **Contact Forms** - Handle customer inquiries
    * **Business Hours** - Automatic open/closed status
    
    ### Architecture
    
    Built following **SOLID principles** with clean architecture:
    - Domain-driven design
    - Repository pattern for data access
    - Service layer for business logic
    - RESTful API design
    
    ### Getting Started
    
    1. **List Restaurants**: `GET /api/restaurants`
    2. **Get Restaurant Details**: `GET /api/restaurants/{restaurant_id}`
    3. **Browse Menu**: `GET /api/restaurants/{restaurant_id}/menu`
    4. **Make Reservation**: `POST /api/restaurants/{restaurant_id}/reservations`
    
    ### Sample Restaurant
    
    Use `kurdiescurry` as the restaurant_id to test endpoints.
    """,
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "API Support",
        "email": "api@restaurant.com",
    },
    license_info={
        "name": "MIT",
    },
    openapi_tags=[
        {
            "name": "Restaurants",
            "description": "Operations related to restaurant information, branding, and status",
        },
        {
            "name": "Menu",
            "description": "Browse and search restaurant menus with dietary filtering",
        },
        {
            "name": "Reservations",
            "description": "Create and manage table reservations",
        },
        {
            "name": "Contact",
            "description": "Submit customer inquiries and feedback",
        },
        {
            "name": "Chat",
            "description": "AI-powered chat assistant for customer support",
        },
        {
            "name": "Health",
            "description": "System health checks and status",
        },
    ],
)

# Configure CORS - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (development only)
    allow_credentials=False,  # Must be False when allow_origins is "*"
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"],  # All methods
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"],  # Expose all headers
    max_age=3600,  # Cache preflight requests for 1 hour
)

# Production CORS configuration (commented out for development)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.cors_origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["Content-Type", "Accept", "Authorization", "X-Requested-With"],
#     expose_headers=["*"],
# )


# Health check endpoint
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - API health check"""
    return {
        "status": "ok",
        "message": "Welcome to Kurdie's Curry Restaurant API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Register routers with /api prefix
API_PREFIX = "/api"

app.include_router(menu_router, prefix=API_PREFIX)
app.include_router(reservation_router, prefix=API_PREFIX)
app.include_router(contact_router, prefix=API_PREFIX)
app.include_router(restaurant_router, prefix=API_PREFIX)
app.include_router(chat_router, prefix=API_PREFIX)


# Startup event
@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    from app.database.base import init_db
    
    print("=" * 60)
    print("🍛 Multi-Restaurant Management API Starting...")
    print("=" * 60)
    
    # Initialize database
    print("🗄️  Initializing database...")
    init_db()
    
    print(f"📍 Sample Restaurant: {settings.restaurant_name}")
    print(f"📫 Address: {settings.restaurant_address}")
    print(f"📞 Phone: {settings.restaurant_phone}")
    print(f"🌐 CORS Origins: {', '.join(settings.cors_origins)}")
    print(f"📚 API Documentation: http://{settings.host}:{settings.port}/docs")
    print(f"💾 Database: SQLite (restaurant.db)")
    print("=" * 60)


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("\n" + "=" * 60)
    print("🛑 Multi-Restaurant Management API Shutting Down...")
    print("💾 Database saved successfully")
    print("=" * 60)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info" if settings.debug else "warning",
    )


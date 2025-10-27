# Backend Architecture Documentation

## Overview

This document describes the architecture and design decisions for the Kurdie's Curry Restaurant Backend API.

## Design Principles

### 1. Clean Architecture

The application follows Clean Architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                     API Layer                           │
│            (FastAPI Routes/Controllers)                 │
│                  app/api/*.py                          │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                  Service Layer                          │
│               (Business Logic)                          │
│                app/services/*.py                        │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│               Repository Layer                          │
│              (Data Access Logic)                        │
│              app/repositories/*.py                      │
└────────────────────┬────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────┐
│                Domain Models                            │
│           (Business Entities/Rules)                     │
│               app/models/*.py                           │
└─────────────────────────────────────────────────────────┘
```

### 2. SOLID Principles

#### Single Responsibility Principle (SRP)
Each class has one reason to change:
- **MenuItem**: Represents menu item data only
- **MenuRepository**: Handles menu data access only
- **MenuService**: Contains menu business logic only
- **MenuRouter**: Handles HTTP requests/responses only

#### Open/Closed Principle (OCP)
Classes are open for extension but closed for modification:
- New dietary tags can be added without modifying existing code
- New payment methods can be added via strategy pattern
- New notification channels can be added via observer pattern

#### Liskov Substitution Principle (LSP)
Interfaces can be substituted with any implementation:
- Any `IMenuRepository` implementation works with `MenuService`
- `InMemoryMenuRepository` can be replaced with `DatabaseMenuRepository`
- No service code needs to change when swapping implementations

#### Interface Segregation Principle (ISP)
Clients don't depend on interfaces they don't use:
- Separate schemas for different operations (Create, Update, Response)
- Focused repository interfaces (IMenuRepository, IReservationRepository)
- Each service only depends on repositories it needs

#### Dependency Inversion Principle (DIP)
High-level modules don't depend on low-level modules:
- Services depend on repository interfaces, not implementations
- Dependency injection through `core/dependencies.py`
- Easy to swap implementations for testing or production

## Layer Responsibilities

### Domain Layer (`app/models/`)

**Purpose**: Core business entities and rules

**Files**:
- `entities.py`: Domain objects (MenuItem, Menu, Reservation, etc.)

**Characteristics**:
- No dependencies on other layers
- Contains business rules (validation, calculations)
- Immutable where possible (using dataclasses)
- Framework-agnostic (pure Python)

**Example**:
```python
@dataclass
class MenuItem:
    id: int
    name: str
    price: float
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
```

### Repository Layer (`app/repositories/`)

**Purpose**: Data access abstraction

**Files**:
- `menu_repository.py`: Menu data access
- `reservation_repository.py`: Reservation data access
- `contact_repository.py`: Contact message data access

**Characteristics**:
- Defines interfaces (contracts)
- Provides in-memory implementations
- Easy to swap for database implementations
- Hides data source details from services

**Example**:
```python
class IMenuRepository(ABC):
    @abstractmethod
    def get_menu(self) -> Menu:
        pass

class InMemoryMenuRepository(IMenuRepository):
    def get_menu(self) -> Menu:
        return self._menu
```

### Service Layer (`app/services/`)

**Purpose**: Business logic and orchestration

**Files**:
- `menu_service.py`: Menu operations
- `reservation_service.py`: Reservation business logic
- `contact_service.py`: Contact form handling
- `restaurant_service.py`: Restaurant info and status

**Characteristics**:
- Depends on repository interfaces
- Contains business rules and workflows
- Coordinate multiple repositories if needed
- Transform domain objects to/from DTOs

**Example**:
```python
class MenuService:
    def __init__(self, repository: IMenuRepository):
        self._repository = repository
    
    def get_menu_grouped_by_category(self):
        menu = self._repository.get_menu()
        # Business logic to group and format
        return grouped_menu
```

### API Layer (`app/api/`)

**Purpose**: HTTP request/response handling

**Files**:
- `menu_routes.py`: Menu endpoints
- `reservation_routes.py`: Reservation endpoints
- `contact_routes.py`: Contact endpoints
- `restaurant_routes.py`: Restaurant info endpoints

**Characteristics**:
- FastAPI routers
- HTTP-specific concerns (status codes, headers)
- Input validation (via Pydantic schemas)
- Error handling and responses

**Example**:
```python
@router.get("/menu")
async def get_menu(service: MenuService = Depends()):
    return service.get_menu_grouped_by_category()
```

### Schema Layer (`app/schemas/`)

**Purpose**: Data Transfer Objects (DTOs) and validation

**Files**:
- `menu_schemas.py`: Menu request/response models
- `reservation_schemas.py`: Reservation models
- `contact_schemas.py`: Contact form models
- `restaurant_schemas.py`: Restaurant info models

**Characteristics**:
- Pydantic models for validation
- Separate schemas for different use cases
- API contract definitions
- Documentation via examples

**Example**:
```python
class MenuItemResponse(BaseModel):
    id: int
    name: str
    price: float = Field(ge=0)
    tags: List[str]
```

## Data Flow

### Request Flow (Menu Retrieval)

```
1. Client Request
   ↓
2. API Layer (menu_routes.py)
   - Receive HTTP GET /api/menu
   - Inject MenuService dependency
   ↓
3. Service Layer (menu_service.py)
   - Call repository.get_menu()
   - Group items by category
   - Convert to response schemas
   ↓
4. Repository Layer (menu_repository.py)
   - Retrieve menu from data source
   - Return domain entities
   ↓
5. Domain Layer (entities.py)
   - Menu and MenuItem objects
   ↓
← Response flows back up through layers
```

### Request Flow (Create Reservation)

```
1. Client Request (POST /api/reservations)
   ↓
2. API Layer
   - Validate ReservationCreate schema
   - Inject ReservationService
   ↓
3. Service Layer
   - Validate business rules (date not in past)
   - Create Reservation entity
   - Call repository.create()
   ↓
4. Repository Layer
   - Generate ID
   - Store reservation
   - Return saved entity
   ↓
5. Service Layer
   - Create confirmation response
   ↓
← Return ReservationConfirmation
```

## Dependency Injection

### Container (`app/core/dependencies.py`)

```python
# Initialize repositories
menu_repo = InMemoryMenuRepository(menu)
reservation_repo = InMemoryReservationRepository()

# Initialize services with dependencies
menu_service = MenuService(menu_repo)
reservation_service = ReservationService(reservation_repo)

# Provider functions
def get_menu_service() -> MenuService:
    return menu_service
```

### Usage in Routes

```python
@router.get("/menu")
async def get_menu(
    service: MenuService = Depends(get_menu_service)
):
    return service.get_menu_grouped_by_category()
```

## Error Handling

### Validation Errors
- Pydantic schemas validate input automatically
- Returns 422 Unprocessable Entity

### Business Logic Errors
- Services raise `ValueError` for business rule violations
- Routes catch and convert to HTTPException (400 Bad Request)

### Not Found Errors
- Return HTTPException(404) when resource not found

### Example
```python
try:
    confirmation = service.create_reservation(data)
    return confirmation
except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
```

## Testing Strategy

### Unit Testing

**Domain Layer**:
```python
def test_menu_item_validation():
    with pytest.raises(ValueError):
        MenuItem(id=1, name="Test", price=-5.0)
```

**Service Layer**:
```python
def test_menu_service():
    mock_repo = Mock(spec=IMenuRepository)
    service = MenuService(mock_repo)
    # Test business logic
```

**Repository Layer**:
```python
def test_in_memory_repository():
    repo = InMemoryMenuRepository(menu)
    item = repo.get_item_by_id(1)
    assert item.name == "Samosas"
```

### Integration Testing

```python
from fastapi.testclient import TestClient

def test_get_menu():
    client = TestClient(app)
    response = client.get("/api/menu")
    assert response.status_code == 200
    assert "appetizers" in response.json()
```

## Future Enhancements

### Database Integration

1. Create database repositories:
```python
class DatabaseMenuRepository(IMenuRepository):
    def __init__(self, db: Session):
        self.db = db
    
    def get_menu(self) -> Menu:
        # Query database
        items = self.db.query(MenuItemModel).all()
        # Convert to domain entities
        return Menu(items=[...])
```

2. Update dependencies:
```python
def get_menu_repository(db: Session = Depends(get_db)):
    return DatabaseMenuRepository(db)
```

3. Services remain unchanged! (Dependency Inversion)

### Caching Layer

```python
class CachedMenuService(MenuService):
    def get_menu_grouped_by_category(self):
        if not self._cache:
            self._cache = super().get_menu_grouped_by_category()
        return self._cache
```

### Authentication

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Validate token, return user
    pass

@router.post("/admin/menu")
async def create_menu_item(
    item: MenuItemCreate,
    user: User = Depends(get_current_user)
):
    # Only authenticated users can access
    pass
```

## Best Practices

1. **Keep layers independent**: Changes in one layer shouldn't affect others
2. **Depend on abstractions**: Use interfaces, not concrete implementations
3. **Single responsibility**: Each class has one clear purpose
4. **Immutability**: Use immutable objects where possible
5. **Validation**: Validate at boundaries (API layer, domain layer)
6. **Error handling**: Handle errors at appropriate layers
7. **Testing**: Test each layer independently

## Conclusion

This architecture provides:
- ✅ Maintainability through separation of concerns
- ✅ Testability through dependency injection
- ✅ Flexibility through abstraction
- ✅ Scalability through modularity
- ✅ Clarity through SOLID principles

The design allows the system to evolve without major rewrites, making it production-ready and future-proof.


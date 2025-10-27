# Kurdie's Curry Restaurant Backend API

A well-architected FastAPI backend for a restaurant application following SOLID principles and clean architecture.

## 🏗️ Architecture

This backend follows **Clean Architecture** and **SOLID Principles** for maintainability, testability, and scalability.

### Project Structure

```
backend/
├── app/
│   ├── models/          # Domain entities (business objects)
│   │   └── entities.py  # MenuItem, Menu, Reservation, etc.
│   ├── repositories/    # Data access layer (abstractions)
│   │   ├── menu_repository.py
│   │   ├── reservation_repository.py
│   │   └── contact_repository.py
│   ├── services/        # Business logic layer
│   │   ├── menu_service.py
│   │   ├── reservation_service.py
│   │   ├── contact_service.py
│   │   └── restaurant_service.py
│   ├── api/            # HTTP endpoints (controllers)
│   │   ├── menu_routes.py
│   │   ├── reservation_routes.py
│   │   ├── contact_routes.py
│   │   └── restaurant_routes.py
│   ├── schemas/        # Pydantic models for validation
│   │   ├── menu_schemas.py
│   │   ├── reservation_schemas.py
│   │   ├── contact_schemas.py
│   │   └── restaurant_schemas.py
│   ├── core/           # Configuration and dependencies
│   │   ├── config.py
│   │   └── dependencies.py
│   ├── data/           # Sample data
│   │   └── sample_data.py
│   └── main.py         # FastAPI application
├── requirements.txt
├── run.py
└── README.md
```

### SOLID Principles Implementation

#### 1. **Single Responsibility Principle (SRP)**
- Each class/module has one clear responsibility
- `MenuItem` entity only represents menu item data
- `MenuService` only handles menu business logic
- `MenuRepository` only handles data access

#### 2. **Open/Closed Principle (OCP)**
- System is open for extension through interfaces
- New dietary tags can be added to `DietaryTag` enum
- New menu categories can be added without changing existing code

#### 3. **Liskov Substitution Principle (LSP)**
- Repository interfaces can be swapped
- `InMemoryMenuRepository` can be replaced with `DatabaseMenuRepository`
- Services depend on interfaces, not implementations

#### 4. **Interface Segregation Principle (ISP)**
- Separate schemas for different use cases
- `MenuItemResponse` vs `MenuItemCreate` vs `MenuItemUpdate`
- Small, focused repository interfaces

#### 5. **Dependency Inversion Principle (DIP)**
- Services depend on repository abstractions (`IMenuRepository`)
- Not on concrete implementations (`InMemoryMenuRepository`)
- Dependencies injected through `core/dependencies.py`

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

**Option 1: Using the run script**
```bash
python run.py
```

**Option 2: Using uvicorn directly**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL:** http://localhost:8000
- **Interactive Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## 📚 API Endpoints

### Menu Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/menu` | Get complete menu organized by categories |
| GET | `/api/menu/items/{item_id}` | Get specific menu item |
| GET | `/api/menu/category/{category}` | Get items by category |
| GET | `/api/menu/search?query={term}` | Search menu items |

### Reservation Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/reservations` | Create a new reservation |
| GET | `/api/reservations/{id}` | Get reservation details |
| DELETE | `/api/reservations/{id}` | Cancel a reservation |

### Contact Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/contact` | Submit contact form |

### Restaurant Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/restaurant/status` | Get open/closed status |
| GET | `/api/restaurant/info` | Get restaurant information |
| GET | `/api/restaurant/hours` | Get business hours |

## 📋 Example API Calls

### Get Menu
```bash
curl http://localhost:8000/api/menu
```

### Create Reservation
```bash
curl -X POST http://localhost:8000/api/reservations \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "(555) 123-4567",
    "date": "2024-12-25",
    "time": "19:00",
    "party_size": 4,
    "special_requests": "Window seat preferred"
  }'
```

### Submit Contact Form
```bash
curl -X POST http://localhost:8000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "subject": "Catering inquiry",
    "message": "I would like to know about your catering services."
  }'
```

### Check Restaurant Status
```bash
curl http://localhost:8000/api/restaurant/status
```

## 🔧 Configuration

Configuration is managed through environment variables or the `.env` file.

Create a `.env` file in the backend directory:

```env
# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Restaurant Information
RESTAURANT_NAME=Kurdie's Curry
RESTAURANT_ADDRESS=1337 N Spice Rd, Prescott Valley, AZ 86314
RESTAURANT_PHONE=(928) 555-1337
```

## 🏪 Menu Structure

The menu is organized into categories:

1. **Appetizers** - Starters and small plates
2. **Signature Dishes** - Main courses and specialties
3. **Bread and Sides** - Naan, rice, and accompaniments
4. **Beverages** - Drinks and refreshments
5. **Desserts** - Sweet treats

Each menu item includes:
- Name and description
- Price
- Dietary tags (vegetarian, vegan, gluten-free, etc.)
- Image URL
- Availability status

## 🔄 Extending the Backend

### Adding a New Dietary Tag

1. Add to `DietaryTag` enum in `app/models/entities.py`:
```python
class DietaryTag(str, Enum):
    # ... existing tags
    SPICY = "spicy"
```

2. Use in menu items:
```python
MenuItem(
    # ... other fields
    tags=[DietaryTag.VEGETARIAN, DietaryTag.SPICY]
)
```

### Adding a New Menu Category

1. Add to `MenuCategory` enum in `app/models/entities.py`
2. Update `MenuResponse` schema in `app/schemas/menu_schemas.py`
3. Add category to `sample_data.py`

### Switching to a Database

1. Create a new repository implementation:
```python
class DatabaseMenuRepository(IMenuRepository):
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_menu(self) -> Menu:
        # Implement database query
        pass
```

2. Update `dependencies.py` to use the new repository
3. Services don't need to change! (Dependency Inversion)

## 🧪 Testing

The architecture makes testing easy:

```python
# Test services with mock repositories
def test_menu_service():
    mock_repo = MockMenuRepository()
    service = MenuService(mock_repo)
    menu = service.get_menu_grouped_by_category()
    assert "appetizers" in menu
```

## 📝 Business Hours

Default hours (configurable in `config.py`):
- **Monday-Thursday:** 11:00 AM - 9:00 PM
- **Friday-Saturday:** 11:00 AM - 10:00 PM
- **Sunday:** CLOSED

## 🔐 Future Enhancements

- [ ] Add authentication/authorization
- [ ] Integrate with a database (PostgreSQL, MongoDB)
- [ ] Add email notifications for reservations
- [ ] Implement admin panel endpoints
- [ ] Add payment processing
- [ ] Implement online ordering
- [ ] Add rate limiting
- [ ] Add caching layer
- [ ] Implement logging and monitoring
- [ ] Add unit and integration tests

## 🤝 Contributing

This backend follows clean architecture principles. When adding new features:

1. Create domain entities in `models/`
2. Define data access in `repositories/`
3. Implement business logic in `services/`
4. Add API endpoints in `api/`
5. Define schemas in `schemas/`

## 📄 License

This project is part of the Kurdie's Curry restaurant application.

## 🆘 Support

For issues or questions:
- Check API documentation at `/docs`
- Review this README
- Contact: kurdiescurry@example.com

---

**Built with ❤️ using FastAPI and SOLID Principles**


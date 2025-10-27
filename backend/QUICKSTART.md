# Backend Quick Start Guide

## 🚀 Quick Start (5 Minutes)

### 1. Setup Virtual Environment

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the Server

```bash
python3 run.py
```

The server will start at **http://localhost:8000**

### 4. Test the API

Open your browser and go to:
- **Interactive Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health

Or run the test script:
```bash
chmod +x test_api.sh
./test_api.sh
```

## 📡 Available Endpoints

### Menu API
- `GET /api/menu` - Get complete menu
- `GET /api/menu/items/{id}` - Get specific menu item
- `GET /api/menu/category/{category}` - Get items by category
- `GET /api/menu/search?query=...` - Search menu

### Reservation API
- `POST /api/reservations` - Create reservation
- `GET /api/reservations/{id}` - Get reservation details
- `DELETE /api/reservations/{id}` - Cancel reservation

### Contact API
- `POST /api/contact` - Submit contact form

### Restaurant Info API
- `GET /api/restaurant/status` - Get open/closed status
- `GET /api/restaurant/info` - Get restaurant info
- `GET /api/restaurant/hours` - Get business hours

## 🧪 Example API Calls

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
    "party_size": 4
  }'
```

### Check Restaurant Status
```bash
curl http://localhost:8000/api/restaurant/status
```

## 🔧 Configuration

Create a `.env` file in the backend directory:

```env
HOST=0.0.0.0
PORT=8000
DEBUG=True
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 🏗️ Architecture Highlights

This backend follows **SOLID principles** and **Clean Architecture**:

- **Domain Layer** (`models/`): Business entities and rules
- **Repository Layer** (`repositories/`): Data access abstractions
- **Service Layer** (`services/`): Business logic
- **API Layer** (`api/`): HTTP endpoints
- **Schema Layer** (`schemas/`): Request/response validation

### Key Features

✅ **Type Safety** - Full type hints and Pydantic validation  
✅ **SOLID Principles** - Clean, maintainable code architecture  
✅ **Dependency Injection** - Easy to test and swap implementations  
✅ **Auto Documentation** - Interactive API docs at `/docs`  
✅ **CORS Enabled** - Ready for frontend integration  
✅ **Validation** - Comprehensive input validation  
✅ **Error Handling** - Proper HTTP status codes and messages  

## 📊 Sample Data

The backend comes with pre-loaded sample menu data:
- 3 Appetizers (Samosas, Pakoras, Onion Bhaji)
- 4 Signature Dishes (Butter Chicken, Chana Masala, etc.)
- 4 Bread and Sides (Garlic Naan, Rice, etc.)
- 3 Beverages (Lassi, Chai Tea)
- 3 Desserts (Gulab Jamun, Kheer, Rasmalai)

## 🔄 Integration with Frontend

The API is designed to work seamlessly with the Vue.js frontend.

Update the frontend's `.env` or API configuration:
```env
VITE_API_URL=http://localhost:8000/api
```

The response formats match exactly what the frontend expects:
- Menu grouped by categories
- Reservation confirmations
- Restaurant status with `isOpen` boolean

## 📝 Next Steps

1. **Test the API** - Use the interactive docs at `/docs`
2. **Read the Architecture** - See `ARCHITECTURE.md` for detailed design
3. **Customize the Menu** - Edit `app/data/sample_data.py`
4. **Add Database** - Implement database repositories
5. **Add Authentication** - Protect admin endpoints

## 🆘 Troubleshooting

**Port already in use:**
```bash
# Change port in .env or run with:
PORT=8001 python3 run.py
```

**Import errors:**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
pip install -r requirements.txt
```

**CORS issues:**
```bash
# Add your frontend URL to CORS_ORIGINS in .env
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

## 📚 Additional Resources

- **Full README:** `README.md`
- **Architecture Guide:** `ARCHITECTURE.md`
- **API Documentation:** http://localhost:8000/docs (when running)

---

**Built with FastAPI and following SOLID principles** 🚀


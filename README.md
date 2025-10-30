# 🍛 Kurdie's Curry - Full Stack Restaurant Website

A modern, full-stack restaurant management system with AI-powered chat assistant, online reservations, menu management, and customer contact forms.

![Vue.js](https://img.shields.io/badge/Vue.js-3.4-4FC08D?logo=vue.js&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Backend Setup](#-backend-setup)
- [Frontend Setup](#-frontend-setup)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [AI Chat Assistant](#-ai-chat-assistant)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)
- [Configuration Quick Reference](#-configuration-quick-reference)

---

## ✨ Features

### Frontend
- 🎨 **Modern UI/UX** - Responsive design with light/dark mode
- 📱 **Mobile Optimized** - Works seamlessly on all devices
- 🍜 **Interactive Menu** - Browse dishes with filtering and search
- 📅 **Online Reservations** - Book tables with instant confirmation
- 💬 **AI Chat Assistant** - Get instant answers about menu, hours, reservations
- 📧 **Contact Forms** - Easy customer communication
- ⏰ **Real-time Status** - Shows if restaurant is currently open/closed
- 📍 **Google Maps Integration** - One-click directions
- ☎️ **Click-to-Call** - Mobile phone dialer integration

### Backend
- 🚀 **FastAPI** - High-performance async Python API
- 🤖 **OpenAI Integration** - GPT-4.1 powered chatbot with function calling
- 💾 **SQLite Database** - Lightweight, zero-configuration database
- 📨 **Email Notifications** - SendGrid integration for confirmations
- 🔐 **CORS Enabled** - Secure cross-origin requests
- 📚 **Auto-generated Docs** - Swagger UI and ReDoc
- 🏗️ **Clean Architecture** - Repository pattern, service layer, SOLID principles
- ✅ **Data Validation** - Pydantic schemas for type safety
- 🎯 **Function Calling** - AI can create reservations directly

---

## 🛠️ Tech Stack

### Frontend
- **Vue.js 3.4** - Progressive JavaScript framework
- **Vue Router 4** - Client-side routing
- **Vite 5** - Lightning-fast build tool
- **CSS3** - Custom styling with dark mode support
- **Material Symbols** - Google's icon library

### Backend
- **FastAPI 0.104** - Modern Python web framework
- **Python 3.11** - Latest Python features
- **SQLAlchemy 2.0** - SQL toolkit and ORM
- **Pydantic 2.0** - Data validation using Python type hints
- **OpenAI API** - GPT-4.1 for AI chat
- **SendGrid** - Email delivery service
- **Uvicorn** - ASGI server
- **SQLite** - Embedded database

---

## 📁 Project Structure

```
restaurant/
├── backend/                    # Python FastAPI backend
│   ├── app/
│   │   ├── api/               # API route handlers
│   │   │   ├── chat_routes.py
│   │   │   ├── reservation_routes.py
│   │   │   ├── menu_routes.py
│   │   │   └── contact_routes.py
│   │   ├── services/          # Business logic layer
│   │   │   ├── chat_service.py
│   │   │   ├── reservation_service.py
│   │   │   ├── email_service.py
│   │   │   └── prompt_builder_service.py
│   │   ├── repositories/      # Data access layer
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── core/              # Configuration
│   │   │   └── config.py
│   │   └── main.py           # Application entry point
│   ├── alembic/              # Database migrations
│   ├── restaurant.db         # SQLite database
│   ├── requirements.txt      # Python dependencies
│   └── run.py               # Server startup script
│
├── src/                       # Vue.js frontend
│   ├── components/           # Reusable Vue components
│   │   ├── ChatWidget.vue   # AI chat interface
│   │   ├── Header.vue
│   │   └── Footer.vue
│   ├── views/               # Page components
│   │   ├── Home.vue
│   │   ├── Menu.vue
│   │   ├── Reservations.vue
│   │   ├── Contact.vue
│   │   └── About.vue
│   ├── services/            # API client services
│   │   └── api.js
│   ├── router/              # Vue Router configuration
│   │   └── index.js
│   ├── config/              # Frontend configuration
│   │   └── restaurant.js
│   └── main.js             # Application entry point
│
├── package.json             # Node dependencies
├── vite.config.js          # Vite configuration
└── README.md              # This file
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 14+** - [Download](https://nodejs.org/)
- **OpenAI API Key** - [Get one](https://platform.openai.com/api-keys) (for chat feature)

### 1. Clone Repository

```bash
git clone <repository-url>
cd restaurant
```

### 2. Backend Setup (Terminal 1)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo 'OPENAI_API_KEY=your_key_here' > .env

# Initialize database
python migrate.py

# Seed sample data
python seed_data.py

# Start backend server
python run.py
```

Backend will be running at: **http://localhost:8000**

### 3. Frontend Setup (Terminal 2)

```bash
# From project root
cd ../

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be running at: **http://localhost:5173**

### 4. Access the Application

- **Website**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs
- **API Alternative Docs**: http://localhost:8000/redoc

---

## 🔧 Backend Setup (Detailed)

### 1. Virtual Environment

```bash
cd backend
python3 -m venv venv

# Activate
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Main dependencies:**
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - Database ORM
- `pydantic` - Data validation
- `openai` - AI chat integration
- `python-sendgrid` - Email service
- `alembic` - Database migrations

### 3. Environment Variables

Create `.env` file in `backend/` directory:

```env
# OpenAI Configuration (Required for chat)
OPENAI_API_KEY=sk-your-key-here

# SendGrid Configuration (Optional for emails)
SENDGRID_API_KEY=SG.your-key-here
SENDGRID_FROM_EMAIL=noreply@yourdomain.com
RESTAURANT_NOTIFICATION_EMAIL=admin@yourdomain.com

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

### 4. Database Setup

```bash
# Run migrations
python migrate.py

# Seed sample data (optional but recommended)
python seed_data.py
```

This creates:
- Restaurant profile
- Sample menu items
- Database tables

### 5. Start Backend

```bash
# Development mode (auto-reload)
python run.py

# Or with uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🎨 Frontend Setup (Detailed)

### 1. Install Dependencies

   ```bash
   npm install
   ```

**Main dependencies:**
- `vue` - JavaScript framework
- `vue-router` - Routing
- `marked` - Markdown parsing (for chat)
- `dompurify` - HTML sanitization

### 2. Frontend Configuration (Important!)

The frontend has **TWO configuration files** you need to know about:

#### 📁 **File 1: `src/config/env.config.js`** (Environment Settings)

This file manages API URLs and environment-specific settings.

**Location:** `/src/config/env.config.js`

```javascript
const ENV = {
  development: {
    apiBaseUrl: 'http://localhost:8000/api',  // ← Your local backend
    debug: true,
    enableMocks: false,
  },
  staging: {
    apiBaseUrl: 'https://staging-api.yoursite.com/api',  // ← Staging server
    debug: true,
    enableMocks: false,
  },
  production: {
    apiBaseUrl: 'https://api.yoursite.com/api',  // ← Production server
    debug: false,
    enableMocks: false,
  }
}
```

**What each setting means:**

| Setting | Meaning | Default | When to Change |
|---------|---------|---------|----------------|
| `apiBaseUrl` | Backend API URL | `http://localhost:8000/api` | **Change this!** Update to your backend URL |
| `debug` | Show console logs | `true` (dev), `false` (prod) | Usually keep as-is |
| `enableMocks` | Use fake API data | `false` | Enable if backend unavailable |

**🔴 IMPORTANT:** Change `development.apiBaseUrl` to match your backend:
```javascript
// If backend runs on localhost:8000
apiBaseUrl: 'http://localhost:8000/api'

// If using ngrok for testing
apiBaseUrl: 'https://your-ngrok-url.ngrok-free.app/api'

// If backend on different port
apiBaseUrl: 'http://localhost:3000/api'
```

#### 📁 **File 2: `src/config/restaurant.js`** (Restaurant Settings)

This file contains restaurant-specific configuration.

**Location:** `/src/config/restaurant.js`

```javascript
export const RESTAURANT_CONFIG = {
  // Unique identifier for this restaurant
  restaurantId: 'kurdiescurry',  // ← Must match backend restaurant ID
  
  // Backend API URL (from env.config.js)
  apiBaseUrl: CONFIG.apiBaseUrl,
  
  // Display name
  displayName: "Kurdie's Curry",
  
  // Feature flags
  features: {
    onlineReservations: true,  // Show reservation form
    contactForm: true,          // Show contact form
    menuDisplay: true,          // Show menu page
  }
}
```

**What each setting means:**

| Setting | Meaning | Example | When to Change |
|---------|---------|---------|----------------|
| `restaurantId` | Restaurant ID in database | `'kurdiescurry'` | **Must match backend!** Check `backend/seed_data.py` |
| `apiBaseUrl` | API URL (from env.config.js) | Auto-set | Don't change directly |
| `displayName` | Restaurant name shown in UI | `"Kurdie's Curry"` | Change to your restaurant name |
| `features.onlineReservations` | Enable/disable reservations | `true` | Set `false` to hide |
| `features.contactForm` | Enable/disable contact form | `true` | Set `false` to hide |
| `features.menuDisplay` | Enable/disable menu | `true` | Set `false` to hide |

#### 🔧 **Environment Variables (Optional Override)**

You can override settings using `.env` files:

**Create:** `.env.development` (for local development)
```bash
# Override API URL
VITE_API_BASE_URL=http://localhost:8000/api

# Override Restaurant ID
VITE_RESTAURANT_ID=kurdiescurry

# Enable debug mode
VITE_DEBUG=true
```

**Create:** `.env.production` (for deployment)
```bash
# Production API URL
VITE_API_BASE_URL=https://api.yourdomain.com/api

# Production Restaurant ID
VITE_RESTAURANT_ID=kurdiescurry

# Disable debug
VITE_DEBUG=false
```

**Priority:** Environment variables > Config files > Defaults

#### 📝 **Quick Setup Checklist:**

1. ✅ Open `src/config/env.config.js`
2. ✅ Update `development.apiBaseUrl` to your backend URL
3. ✅ Open `src/config/restaurant.js`
4. ✅ Verify `restaurantId` matches your backend
5. ✅ Update `displayName` if needed
6. ✅ Configure `features` flags as needed

### 3. Development Server

   ```bash
   npm run dev
   ```

Runs at: http://localhost:5173

### 4. Build for Production

```bash
npm run build
```

Creates optimized build in `dist/` folder.

### 5. Preview Production Build

```bash
npm run preview
```

---

## ⚙️ Configuration

### Frontend Configuration Files

The frontend uses a **two-tier configuration system**:

```
📁 src/config/
├── env.config.js          ← Environment settings (API URLs, debug mode)
└── restaurant.js          ← Restaurant settings (ID, features, display name)
                             ↳ imports from env.config.js
```

**Configuration Flow:**
```
.env files (if exist)
    ↓ (overrides)
env.config.js (environment-specific)
    ↓ (used by)
restaurant.js (restaurant-specific)
    ↓ (used by)
Vue Components & API Service
```

#### 1️⃣ **Environment Config: `src/config/env.config.js`**

Controls environment-specific settings (dev, staging, production).

**Purpose:** Manage different API URLs and debug settings per environment.

**Key Settings:**
```javascript
const ENV = {
  development: {
    apiBaseUrl: 'http://localhost:8000/api',  // Local backend
    debug: true,
    enableMocks: false,
  },
  // ... staging and production
}
```

| Setting | Type | Description | Example |
|---------|------|-------------|---------|
| `apiBaseUrl` | string | Backend API endpoint | `'http://localhost:8000/api'` |
| `debug` | boolean | Enable console logging | `true` (dev), `false` (prod) |
| `enableMocks` | boolean | Use mock data instead of API | `false` |

**When to Edit:**
- ✅ Changing backend URL
- ✅ Setting up staging/production environments
- ✅ Enabling/disabling debug mode

#### 2️⃣ **Restaurant Config: `src/config/restaurant.js`**

Restaurant-specific settings and feature flags.

**Purpose:** Configure restaurant identity and which features to show.

**Key Settings:**
```javascript
export const RESTAURANT_CONFIG = {
  restaurantId: 'kurdiescurry',  // Must match backend!
  displayName: "Kurdie's Curry",
  features: {
    onlineReservations: true,
    contactForm: true,
    menuDisplay: true,
  }
}
```

| Setting | Type | Description | Notes |
|---------|------|-------------|-------|
| `restaurantId` | string | Unique restaurant identifier | **Must match backend database** |
| `displayName` | string | Restaurant name shown in UI | Cosmetic only |
| `features.onlineReservations` | boolean | Show/hide reservation form | Hides entire page if false |
| `features.contactForm` | boolean | Show/hide contact form | Hides contact page if false |
| `features.menuDisplay` | boolean | Show/hide menu | Hides menu page if false |

**When to Edit:**
- ✅ Setting up a new restaurant
- ✅ Enabling/disabling features
- ✅ Changing display name

#### 🔧 **Environment Variables (Override)**

Create `.env.development` or `.env.production` to override:

```bash
# .env.development
VITE_API_BASE_URL=http://localhost:8000/api
VITE_RESTAURANT_ID=kurdiescurry
VITE_DEBUG=true
```

**Available Variables:**
- `VITE_API_BASE_URL` - Override API URL
- `VITE_RESTAURANT_ID` - Override restaurant ID
- `VITE_DEBUG` - Enable/disable debug logs
- `VITE_ENABLE_MOCKS` - Use mock data
- `VITE_LOG_LEVEL` - Set log level (debug, info, warn, error)

**Priority:** `.env` variables > config files > defaults

---

### Backend Configuration (`backend/app/core/config.py`)

```python
class Settings(BaseSettings):
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    
    # CORS - Add your domain
    cors_origins: List[str] = [
        "http://localhost:5173",
        "https://yourdomain.com"
    ]
    
    # Restaurant Info
    restaurant_name: str = "Kurdie's Curry"
    restaurant_address: str = "1337 N Spice Rd, Prescott Valley, AZ 86314"
    restaurant_phone: str = "(928) 555-1337"
    
    # Business Hours (24-hour format)
    business_hours: dict = {
        0: None,        # Sunday - CLOSED
        1: (11, 21),    # Monday: 11am-9pm
        2: (11, 21),    # Tuesday
        # ... etc
    }
    
    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1"
```

### Frontend Configuration (`src/config/restaurant.js`)

   ```javascript
export const RESTAURANT_ID = 'kc-001'
export const API_BASE_URL = import.meta.env.VITE_API_URL || 
                            'http://localhost:8000/api'
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Key Endpoints

#### Restaurants
```
GET    /restaurants              # List all restaurants
GET    /restaurants/{id}         # Get restaurant details
GET    /restaurants/{id}/status  # Check if open/closed
```

#### Menu
```
GET    /restaurants/{id}/menu    # Get full menu
GET    /restaurants/{id}/menu/search?q=curry  # Search menu
```

#### Reservations
```
POST   /restaurants/{id}/reservations  # Create reservation
GET    /restaurants/{id}/reservations/{reservation_id}  # Get reservation
```

#### Contact
```
POST   /restaurants/{id}/contact  # Submit contact form
```

#### Chat (AI Assistant)
```
POST   /restaurants/{id}/chat  # Send chat message
GET    /restaurants/{id}/chat/history/{session_id}  # Get chat history
```

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🤖 AI Chat Assistant

### Features
- Answers questions about menu, hours, location
- Handles reservation requests via function calling
- Maintains conversation context
- Markdown formatting support
- Persistent chat history

### How It Works

1. **User sends message** → Frontend sends to `/api/restaurants/{id}/chat`
2. **Backend builds context** → Restaurant info + chat history
3. **OpenAI processes** → GPT-4.1 generates response
4. **Function calling** → Can create reservations directly
5. **Response rendered** → Markdown formatted in UI

### Chat Configuration

Model: `gpt-4.1` (configurable in `config.py`)

System prompt includes:
- Restaurant details
- Menu information
- Business hours
- Reservation capabilities

### Testing Chat

```bash
# Test via API
curl -X POST http://localhost:8000/api/restaurants/kc-001/chat \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "test_123",
    "message": "What are your hours?"
  }'
```

---

## 🚢 Deployment

### Backend Deployment

#### Option 1: Docker (Recommended)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t restaurant-api .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_key restaurant-api
```

#### Option 2: Traditional Server

```bash
# Install dependencies
pip install -r requirements.txt

# Run with gunicorn (production ASGI server)
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend Deployment

#### Option 1: Netlify / Vercel (Easiest)

```bash
npm run build
# Deploy dist/ folder
```

#### Option 2: Nginx

```bash
npm run build

# Copy dist/ to nginx
cp -r dist/* /var/www/html/
```

**Nginx config:**
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    
    root /var/www/html;
    index index.html;
    
    location / {
        try_files $uri $uri/ /index.html;
    }
    
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🔍 Troubleshooting

### Backend Issues

#### "OPENAI_API_KEY is not configured"
```bash
# Add to .env file
echo 'OPENAI_API_KEY=sk-your-key' > backend/.env
```

#### "ModuleNotFoundError"
```bash
# Make sure virtual environment is activated
source backend/venv/bin/activate
pip install -r backend/requirements.txt
```

#### "Port 8000 already in use"
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or change port in config.py
```

#### Database errors
```bash
# Reset database
cd backend
rm restaurant.db
python migrate.py
python seed_data.py
```

### Frontend Issues

#### "Failed to fetch"
- Check backend is running on http://localhost:8000
- Check CORS is configured correctly
- Verify `API_BASE_URL` in `src/config/restaurant.js`

#### Build errors
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

#### Dark mode not working
- Check browser's color scheme preference
- Verify CSS variables are properly defined

### Configuration Issues

#### "API calls failing / 404 errors"

**Problem:** Frontend can't connect to backend.

**Solution:**
1. Check `src/config/env.config.js` → `development.apiBaseUrl`
   ```javascript
   // Should be:
   apiBaseUrl: 'http://localhost:8000/api'
   ```

2. Verify backend is running:
   ```bash
   curl http://localhost:8000/health
   # Should return: {"status":"healthy"}
   ```

3. Check console for errors:
   - Open browser DevTools (F12)
   - Look for CORS errors or 404s
   - Verify API URL in Network tab

#### "Wrong restaurant showing / Restaurant not found"

**Problem:** Restaurant ID mismatch between frontend and backend.

**Solution:**
1. Check frontend config: `src/config/restaurant.js`
   ```javascript
   restaurantId: 'kurdiescurry'  // This value
   ```

2. Check backend database:
   ```bash
   cd backend
   sqlite3 restaurant.db "SELECT id, name FROM restaurants;"
   ```

3. Make sure they match! Update one or the other.

#### "Features not showing (menu, reservations, etc.)"

**Problem:** Feature flags are disabled.

**Solution:**
1. Open `src/config/restaurant.js`
2. Check `features` object:
   ```javascript
   features: {
     onlineReservations: true,  // false = hidden
     contactForm: true,
     menuDisplay: true,
   }
   ```

3. Change to `true` to enable features

#### "Environment variables not working"

**Problem:** `.env` file changes not taking effect.

**Solution:**
1. Make sure file is named correctly:
   - `.env.development` (for dev)
   - `.env.production` (for prod)
   - NOT `env.development` or `.development.env`

2. Prefix all variables with `VITE_`:
   ```bash
   VITE_API_BASE_URL=...  # ✅ Correct
   API_BASE_URL=...       # ❌ Wrong - missing VITE_
   ```

3. Restart dev server after changing `.env`:
   ```bash
   # Stop (Ctrl+C) then restart
   npm run dev
   ```

#### "Can't find config files"

**Locations:**
```
Frontend configs:
├── src/config/env.config.js       # Environment settings
└── src/config/restaurant.js       # Restaurant settings

Backend config:
└── backend/app/core/config.py     # Backend settings
```

### Chat Issues

#### Empty chat responses
Check backend logs for:
```
❌ ERROR in process_message: [error details]
```

Common causes:
- Invalid/expired OpenAI API key
- No API credits remaining
- Model not available (try `gpt-3.5-turbo`)

#### Chat not rendering markdown
- Check browser console for errors
- Verify `marked` and `dompurify` are installed

---

## 📝 Development Tips

### Backend Development

#### Watch logs:
```bash
tail -f backend/backend.log
```

#### Test API with curl:
```bash
# Get menu
curl http://localhost:8000/api/restaurants/kc-001/menu

# Create reservation
curl -X POST http://localhost:8000/api/restaurants/kc-001/reservations \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","phone":"555-1234","date":"2024-12-25","time":"19:00","party_size":4}'
```

#### Database inspection:
```bash
sqlite3 backend/restaurant.db
.tables
.schema reservations
SELECT * FROM reservations;
```

### Frontend Development

#### Component structure:
- Keep components small and focused
- Use props for parent-child communication
- Emit events for child-parent communication

#### State management:
- Local state with `ref()` and `reactive()`
- No external state management library needed for this size

#### API calls:
- Centralized in `src/services/api.js`
- Consistent error handling

---

## 🤝 Contributing

### Code Style

**Backend (Python):**
- Follow PEP 8
- Use type hints
- Add docstrings to functions
- Keep functions small and focused

**Frontend (JavaScript/Vue):**
- Use `<script setup>` syntax
- Composition API over Options API
- Descriptive variable names
- Comment complex logic

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes
git add .
git commit -m "feat: add feature description"

# Push
git push origin feature/your-feature
```

---

## 📋 Configuration Quick Reference

### Frontend Configuration Locations

| What to Configure | File Location | Key Settings |
|-------------------|---------------|--------------|
| **API URL** | `src/config/env.config.js` | `development.apiBaseUrl` |
| **Restaurant ID** | `src/config/restaurant.js` | `restaurantId` |
| **Feature Flags** | `src/config/restaurant.js` | `features.*` |
| **Environment Override** | `.env.development` | `VITE_API_BASE_URL`, `VITE_RESTAURANT_ID` |

### Backend Configuration Locations

| What to Configure | File Location | Key Settings |
|-------------------|---------------|--------------|
| **OpenAI API Key** | `backend/.env` | `OPENAI_API_KEY` |
| **Email Service** | `backend/.env` | `SENDGRID_API_KEY` |
| **Restaurant Info** | `backend/app/core/config.py` | `restaurant_name`, `restaurant_address`, etc. |
| **Business Hours** | `backend/app/core/config.py` | `business_hours` |
| **Server Settings** | `backend/app/core/config.py` | `host`, `port`, `debug` |

### Configuration Priority (Frontend)

```
Highest Priority
    ↓
1. .env files (VITE_* variables)
    ↓
2. src/config/env.config.js (environment-specific)
    ↓
3. src/config/restaurant.js (restaurant-specific)
    ↓
4. Default values (in code)
    ↓
Lowest Priority
```

### Quick Setup Checklist

**Frontend:**
- [ ] Update `src/config/env.config.js` with your backend URL
- [ ] Verify `src/config/restaurant.js` has correct restaurant ID
- [ ] Check feature flags in `restaurant.js` are enabled
- [ ] Create `.env.development` if you need custom overrides

**Backend:**
- [ ] Create `backend/.env` file
- [ ] Add `OPENAI_API_KEY` to `.env`
- [ ] (Optional) Add `SENDGRID_API_KEY` for emails
- [ ] Update `backend/app/core/config.py` for restaurant details
- [ ] Run `python migrate.py` to initialize database

---

## 📄 License

MIT License - feel free to use for your own restaurant!

---

## 🆘 Support

### Get Help

1. **Check logs**: Backend logs show detailed error information
2. **API Docs**: http://localhost:8000/docs for endpoint testing
3. **Browser Console**: Check for frontend errors
4. **Debug Guide**: See `backend/CHAT_DEBUG_GUIDE.md`

### Common Commands Reference

```bash
# Backend
cd backend
source venv/bin/activate          # Activate environment
python run.py                     # Start server
python migrate.py                 # Run migrations
python seed_data.py              # Seed data
tail -f backend.log              # Watch logs

# Frontend
npm run dev                      # Development server
npm run build                    # Production build
npm run preview                  # Preview build

# Database
sqlite3 backend/restaurant.db    # Open database
python -m backend.check_database # Check database status
```

---

## 🎯 Key Features Summary

✅ **Full-stack restaurant website**
✅ **AI-powered chat assistant with GPT-4.1**
✅ **Online reservation system**
✅ **Interactive menu with search**
✅ **Contact form with email notifications**
✅ **Responsive design (mobile-first)**
✅ **Light/dark mode**
✅ **Real-time open/closed status**
✅ **Google Maps & phone integration**
✅ **Markdown rendering in chat**
✅ **Function calling for reservations**
✅ **Clean architecture & SOLID principles**
✅ **Comprehensive API documentation**

---

**Built with ❤️ for Kurdie's Curry**

🌐 Website: http://localhost:5173
📚 API Docs: http://localhost:8000/docs

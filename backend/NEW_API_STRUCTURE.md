# 🔄 New Multi-Restaurant API Structure

## Overview
The backend now supports multiple restaurants with complete branding, images, and individual settings.

---

## 📡 New API Endpoints

### Restaurant Management

#### 1. List All Restaurants
```http
GET /api/restaurants
```
**Response:**
```json
[
  {
    "id": "kurdiescurry",
    "name": "Kurdie's Curry",
    "slug": "kurdiescurry",
    "tagline": "Authentic Flavors, Modern Twist",
    "cuisine_type": "Indian-Kurdish Fusion",
    "logo_url": "https://...",
    "is_active": true
  }
]
```

#### 2. Get Restaurant Details
```http
GET /api/restaurants/{restaurant_id}
```
**Response:**
```json
{
  "id": "kurdiescurry",
  "name": "Kurdie's Curry",
  "slug": "kurdiescurry",
  "tagline": "Authentic Flavors, Modern Twist",
  "address": "1337 N Spice Rd, Prescott Valley, AZ 86314",
  "phone": "(928) 555-1337",
  "email": "info@kurdiescurry.com",
  "hero_image_url": "https://...",
  "about_image_url": "https://...",
  "owner_image_url": "https://...",
  "story": "Our story began...",
  "cuisine_type": "Indian-Kurdish Fusion",
  "owner_name": "Amrita Patel",
  "owner_bio": "Amrita's passion...",
  "is_active": true,
  "accepts_reservations": true
}
```

#### 3. Get Restaurant Status (Open/Closed)
```http
GET /api/restaurants/{restaurant_id}/status
```
**Response:**
```json
{
  "isOpen": true,
  "message": "Open until 9:00 PM"
}
```

#### 4. Get Restaurant Business Hours
```http
GET /api/restaurants/{restaurant_id}/hours
```
**Response:**
```json
{
  "Sunday": "CLOSED",
  "Monday": "11:00 AM - 9:00 PM",
  "Tuesday": "11:00 AM - 9:00 PM",
  ...
}
```

---

### Menu Endpoints (Restaurant-Scoped)

#### 1. Get Restaurant Menu
```http
GET /api/restaurants/{restaurant_id}/menu
```
**Response:**
```json
{
  "appetizers": [...],
  "signature_dishes": [...],
  "bread_and_sides": [...],
  "beverages": [...],
  "desserts": [...]
}
```

#### 2. Get Specific Menu Item
```http
GET /api/restaurants/{restaurant_id}/menu/items/{item_id}
```

#### 3. Get Items by Category
```http
GET /api/restaurants/{restaurant_id}/menu/category/{category}
```

#### 4. Search Menu
```http
GET /api/restaurants/{restaurant_id}/menu/search?query={term}
```

---

### Reservation Endpoints (Restaurant-Scoped)

#### 1. Create Reservation
```http
POST /api/restaurants/{restaurant_id}/reservations
```
**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "(555) 123-4567",
  "date": "2025-12-25",
  "time": "19:00",
  "party_size": 4,
  "special_requests": "Window seat preferred"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Reservation confirmed! See you soon.",
  "reservation_id": "abc123xyz"
}
```

#### 2. Get Reservation Details
```http
GET /api/restaurants/{restaurant_id}/reservations/{reservation_id}
```

#### 3. Cancel Reservation
```http
DELETE /api/restaurants/{restaurant_id}/reservations/{reservation_id}
```

---

### Contact Endpoints (Restaurant-Scoped)

#### 1. Submit Contact Form
```http
POST /api/restaurants/{restaurant_id}/contact
```
**Request Body:**
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "subject": "Catering inquiry",
  "message": "I would like to know about your catering services."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Message sent! We will get back to you."
}
```

---

## 🏗️ Restaurant Entity Structure

Each restaurant has:

### Basic Information
- `id`: Unique identifier
- `name`: Display name
- `slug`: URL-friendly identifier
- `tagline`: Short description/slogan

### Contact Information
- `address`: Physical address
- `phone`: Phone number
- `email`: Contact email

### Branding & Media
- `logo_url`: Restaurant logo
- `hero_image_url`: Homepage hero/banner image
- `about_image_url`: About section image
- `owner_image_url`: Owner/chef photo

### About Section
- `story`: Restaurant story/description
- `cuisine_type`: Type of cuisine
- `owner_name`: Owner/chef name
- `owner_bio`: Owner/chef biography

### Business Details
- `business_hours`: Operating hours by day
- `menu`: Complete menu with all items
- `is_active`: Whether restaurant is active
- `accepts_reservations`: Whether accepting reservations

---

## 📊 Frontend Integration

### Get Restaurant for Homepage
```javascript
// Get restaurant details with all branding
const response = await fetch(`${API_URL}/restaurants/kurdiescurry`);
const restaurant = await response.json();

// Use restaurant data
heroImage = restaurant.hero_image_url;
tagline = restaurant.tagline;
ownerName = restaurant.owner_name;
ownerBio = restaurant.owner_bio;
```

### Get Menu
```javascript
const menu = await fetch(`${API_URL}/restaurants/kurdiescurry/menu`);
```

### Check Status
```javascript
const status = await fetch(`${API_URL}/restaurants/kurdiescurry/status`);
```

### Create Reservation
```javascript
const reservation = await fetch(
  `${API_URL}/restaurants/kurdiescurry/reservations`,
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: "John Doe",
      email: "john@example.com",
      // ... other fields (no restaurant_id needed in body)
    })
  }
);
```

---

## 🔑 Key Design Decisions

1. **RESTful URLs**: Restaurant ID in path, not request body
2. **Complete Branding**: All images and content in one entity
3. **Scoped Resources**: Each resource belongs to a restaurant
4. **Backward Compatible Schemas**: Easy frontend migration

---

## 🚀 Migration Path for Frontend

1. **Update API base URLs** to include restaurant_id:
   - Old: `/api/menu`
   - New: `/api/restaurants/kurdiescurry/menu`

2. **Remove restaurant_id from request bodies**:
   - It's now in the URL path

3. **Use restaurant endpoint for branding**:
   ```javascript
   const restaurant = await fetch('/api/restaurants/kurdiescurry');
   // Get hero_image_url, owner_image_url, etc.
   ```

---

## 🎯 Benefits

✅ **Multi-tenant**: Support unlimited restaurants  
✅ **Complete Branding**: All images and content centralized  
✅ **RESTful Design**: Standard, predictable URLs  
✅ **Scalable**: Easy to add new restaurants  
✅ **Type-Safe**: Full validation with Pydantic  
✅ **SOLID Principles**: Clean separation of concerns  

---

**This design allows each restaurant to have its own unique identity, branding, and menu while sharing the same codebase!** 🍽️


# 🚀 API Quick Reference - Multi-Restaurant Backend

## Base URL
```
http://localhost:8000/api
```

---

## 🏪 Restaurants

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/restaurants` | List all restaurants |
| `GET` | `/restaurants/{id}` | Get restaurant with complete branding |
| `GET` | `/restaurants/{id}/status` | Check if open/closed |
| `GET` | `/restaurants/{id}/hours` | Get business hours |
| `GET` | `/restaurants/{id}/info` | Get contact information |

### Examples

```bash
# List all restaurants
curl http://localhost:8000/api/restaurants

# Get Kurdie's Curry details (with all images, story, etc.)
curl http://localhost:8000/api/restaurants/kurdiescurry

# Check if open
curl http://localhost:8000/api/restaurants/kurdiescurry/status

# Get business hours
curl http://localhost:8000/api/restaurants/kurdiescurry/hours
```

---

## 🍽️ Menu

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/restaurants/{id}/menu` | Get complete menu |
| `GET` | `/restaurants/{id}/menu/items/{item_id}` | Get specific item |
| `GET` | `/restaurants/{id}/menu/category/{category}` | Get items by category |
| `GET` | `/restaurants/{id}/menu/search?query=...` | Search menu |

### Examples

```bash
# Get full menu
curl http://localhost:8000/api/restaurants/kurdiescurry/menu

# Get specific item
curl http://localhost:8000/api/restaurants/kurdiescurry/menu/items/1

# Get appetizers only
curl http://localhost:8000/api/restaurants/kurdiescurry/menu/category/appetizers

# Search for "chicken"
curl "http://localhost:8000/api/restaurants/kurdiescurry/menu/search?query=chicken"
```

---

## 📅 Reservations

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/restaurants/{id}/reservations` | Create reservation |
| `GET` | `/restaurants/{id}/reservations/{res_id}` | Get reservation |
| `DELETE` | `/restaurants/{id}/reservations/{res_id}` | Cancel reservation |

### Examples

```bash
# Create reservation
curl -X POST http://localhost:8000/api/restaurants/kurdiescurry/reservations \
  -H "Content-Type: application/json" \
  -d '{
    "restaurant_id": "kurdiescurry",
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "(555) 123-4567",
    "date": "2025-12-25",
    "time": "19:00",
    "party_size": 4,
    "special_requests": "Window seat"
  }'

# Get reservation
curl http://localhost:8000/api/restaurants/kurdiescurry/reservations/abc123

# Cancel reservation
curl -X DELETE http://localhost:8000/api/restaurants/kurdiescurry/reservations/abc123
```

---

## 📧 Contact

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/restaurants/{id}/contact` | Submit contact form |

### Example

```bash
curl -X POST http://localhost:8000/api/restaurants/kurdiescurry/contact \
  -H "Content-Type: application/json" \
  -d '{
    "restaurant_id": "kurdiescurry",
    "name": "Jane Smith",
    "email": "jane@example.com",
    "subject": "Catering",
    "message": "I need catering for 50 people"
  }'
```

---

## 📊 Response Formats

### Restaurant Detail Response
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
  "logo_url": null,
  "story": "Kurdie's Curry is a culinary journey...",
  "cuisine_type": "Indian-Kurdish Fusion",
  "owner_name": "Amrita Patel",
  "owner_bio": "Amrita's passion for food...",
  "is_active": true,
  "accepts_reservations": true
}
```

### Menu Response
```json
{
  "appetizers": [...],
  "signature_dishes": [...],
  "bread_and_sides": [...],
  "beverages": [...],
  "desserts": [...]
}
```

### Status Response
```json
{
  "isOpen": true,
  "message": "Open until 9:00 PM"
}
```

### Reservation Confirmation
```json
{
  "success": true,
  "message": "Reservation confirmed! See you soon.",
  "reservation_id": "abc123xyz"
}
```

---

## 🔑 Available Restaurants

Currently available:
- **kurdiescurry** - Kurdie's Curry (Indian-Kurdish Fusion)

To add more restaurants, see `MULTI_RESTAURANT_COMPLETE.md`

---

## 🌐 CORS

Configured origins:
- `http://localhost:5173` (Vue.js dev server)
- `http://localhost:3000`

---

## 📖 Full Documentation

- **Swagger UI**: http://localhost:8000/docs (Interactive testing)
- **ReDoc**: http://localhost:8000/redoc (Clean documentation)

---

## ⚡ Quick Frontend Integration

```javascript
const API_URL = 'http://localhost:8000/api';
const RESTAURANT_ID = 'kurdiescurry';

// Get restaurant (for homepage branding)
const restaurant = await fetch(`${API_URL}/restaurants/${RESTAURANT_ID}`);

// Get menu
const menu = await fetch(`${API_URL}/restaurants/${RESTAURANT_ID}/menu`);

// Check status
const status = await fetch(`${API_URL}/restaurants/${RESTAURANT_ID}/status`);

// Create reservation
const reservation = await fetch(
  `${API_URL}/restaurants/${RESTAURANT_ID}/reservations`,
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
      restaurant_id: RESTAURANT_ID,
      /* ...reservation data */ 
    })
  }
);
```

---

**All endpoints tested and working! ✅**


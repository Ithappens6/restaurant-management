# 🔧 CORS Issue - Troubleshooting Guide

## ✅ Backend CORS Configuration is CORRECT

The backend is properly configured with CORS:

```python
# backend/app/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**CORS Test Results:**
```bash
curl -I -X OPTIONS http://localhost:8000/api/restaurants/kurdiescurry/status \
  -H "Origin: http://localhost:5173" \
  -H "Access-Control-Request-Method: GET"

# Response:
access-control-allow-origin: http://localhost:5173
access-control-allow-methods: DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT
access-control-allow-credentials: true
```

## 🔍 Frontend Changes Made

### 1. Fixed API Configuration
```javascript
// src/config/restaurant.js
apiBaseUrl: 'http://localhost:8000/api'  // Hardcoded correct URL
```

### 2. Enhanced Fetch Headers
```javascript
// src/services/api.js
const response = await fetch(url, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  mode: 'cors',
  credentials: 'omit',
})
```

### 3. Added Environment File
```bash
echo "VITE_API_URL=http://localhost:8000/api" > .env
```

## 🧪 Testing Steps

### Step 1: Clear Browser Cache
1. Open DevTools (F12)
2. Right-click refresh button
3. Select "Empty Cache and Hard Reload"

### Step 2: Check Console Logs
Look for these messages:
```
🍽️ Fetching menu from: http://localhost:8000/api/restaurants/kurdiescurry/menu
🕐 Fetching restaurant status from: http://localhost:8000/api/restaurants/kurdiescurry/status
```

### Step 3: Test in Browser Console
```javascript
// Run this in browser console
fetch('http://localhost:8000/api/restaurants/kurdiescurry/status', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  mode: 'cors',
  credentials: 'omit',
})
.then(response => {
  console.log('✅ Success!', response.status)
  return response.json()
})
.then(data => console.log('✅ Data:', data))
.catch(error => console.log('❌ Error:', error))
```

## 🐛 Common Issues & Solutions

### Issue 1: Still calling port 443
**Solution**: 
1. Restart frontend dev server completely
2. Clear browser cache
3. Check if there are multiple `.env` files

### Issue 2: CORS error persists
**Solution**:
1. Verify backend is running: `curl http://localhost:8000/api/restaurants`
2. Check browser Network tab for actual request URL
3. Ensure no proxy or redirect is changing the URL

### Issue 3: Repeated API calls
**Solution**: Fixed with proper interval cleanup in Home.vue

## 📊 Debug Information

### Backend Status
- ✅ Running on port 8000
- ✅ CORS configured for localhost:5173
- ✅ Database initialized
- ✅ All endpoints responding

### Frontend Status
- ✅ Configuration updated
- ✅ API service enhanced
- ✅ CORS headers added
- ✅ Environment file created

## 🚀 Next Steps

1. **Restart Frontend Server**:
   ```bash
   # Stop current server (Ctrl+C)
   npm run dev
   ```

2. **Clear Browser Cache**:
   - Hard refresh (Ctrl+Shift+R)
   - Or empty cache and hard reload

3. **Check Console**:
   - Look for the emoji-prefixed log messages
   - Verify URLs are correct

4. **Test Endpoints**:
   - Menu should load
   - Status should update
   - Forms should submit

## 📞 If Still Having Issues

Run this debug script in browser console:
```javascript
// debug-cors.js
import { RESTAURANT_CONFIG, getRestaurantApiUrl } from './src/config/restaurant.js'
console.log('Config:', RESTAURANT_CONFIG)
console.log('Menu URL:', getRestaurantApiUrl('/menu'))
```

The CORS configuration is correct on the backend side. The issue is likely browser cache or frontend configuration. The changes made should resolve it!


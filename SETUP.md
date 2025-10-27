# 🚀 Quick Setup Guide

## Step 1: Install Dependencies

```bash
cd /Users/lokesh/Desktop/restaurant
npm install
```

This will install Vue.js, Vue Router, and Vite.

## Step 2: Run the Development Server

```bash
npm run dev
```

Your app will open automatically at `http://localhost:5173`

## Step 3: Test the App

✅ **Home Page** - Hero section with navigation
✅ **Menu Page** - Browse menu with filters
✅ **Reservations** - Book a table
✅ **About Page** - Restaurant story
✅ **Contact Page** - Send a message

## What Changed?

### Before (Messy)
- Components in `.js` files with template strings
- Manual script loading
- `ref` import issues
- Navigation not working
- Hard to debug

### After (Clean)
- Components in `.vue` files
- Proper Vue Router
- Clean imports
- Navigation works perfectly
- Easy to maintain

## Next Steps

### To Connect to Your Backend:

1. **Create a `.env` file:**
   ```env
   VITE_API_URL=http://localhost:3000/api
   ```

2. **In `src/services/api.js`:**
   - Uncomment the API integration code
   - Remove the hardcoded data

3. **Your backend should provide:**
   - `GET /api/menu` - Menu data
   - `POST /api/reservations` - Save reservations
   - `POST /api/contact` - Save contact messages

See `README.md` for detailed API specifications.

## Troubleshooting

If you see any errors, just run:
```bash
npm install
```

Then start again:
```bash
npm run dev
```

---

**Enjoy your clean Vue.js app! 🎉**


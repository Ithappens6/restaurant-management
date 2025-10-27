# Kurdie's Curry - Vue.js Restaurant App

A modern, clean Vue.js 3 restaurant website with proper Single File Components (SFC), Vue Router, and API-ready architecture.

## 🚀 Quick Start

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   - The app will automatically open at `http://localhost:5173`

## 📁 Project Structure

```
restaurant/
├── src/
│   ├── views/              # Page components
│   │   ├── Home.vue        # Home page with hero section
│   │   ├── Menu.vue        # Menu with filtering
│   │   ├── Reservations.vue # Reservation form
│   │   ├── About.vue       # About page
│   │   └── Contact.vue     # Contact form
│   ├── components/         # Shared components
│   │   ├── Header.vue      # Page header
│   │   └── Footer.vue      # Bottom navigation
│   ├── services/           # API services
│   │   └── api.js          # API integration (with placeholders)
│   ├── router/             # Vue Router config
│   │   └── index.js        # Route definitions
│   ├── App.vue             # Root component
│   ├── main.js             # App entry point
│   └── style.css           # Global styles
├── index.html              # HTML entry point
├── vite.config.js          # Vite configuration
├── package.json            # Dependencies
└── README.md               # This file
```

## 🎯 Features

- ✅ **Clean Vue.js 3 SFC Architecture** - One `.vue` file per component
- ✅ **Vue Router** - Proper URL routing (e.g., `/menu`, `/reservations`)
- ✅ **API Ready** - Service layer with placeholder code for backend integration
- ✅ **Hot Module Reload** - Instant updates when you save files
- ✅ **Responsive Design** - Works on mobile, tablet, and desktop
- ✅ **Dark Mode Support** - Built-in dark mode styling
- ✅ **Tailwind CSS** - Modern utility-first CSS
- ✅ **Menu Filtering** - Filter by vegetarian, vegan, gluten-free
- ✅ **Shopping Cart** - Add items to cart
- ✅ **Reservation System** - Book tables online
- ✅ **Contact Form** - Send messages to restaurant

## 🔌 Backend API Integration

### Current Setup
The app currently uses **hardcoded data** in `src/services/api.js`. All API calls are mocked with `setTimeout` to simulate network delays.

### Integrating with Your Backend

1. **Set your API URL:**
   Create a `.env` file in the project root:
   ```env
   VITE_API_URL=http://localhost:3000/api
   ```

2. **Update API functions:**
   In `src/services/api.js`, uncomment the API integration code:

   ```javascript
   // UNCOMMENT THIS:
   export async function fetchMenu() {
     try {
       const response = await fetch(`${API_BASE_URL}/menu`, {
         method: 'GET',
         headers: {
           'Content-Type': 'application/json',
         },
       })
       
       if (!response.ok) {
         throw new Error(`HTTP error! status: ${response.status}`)
       }
       
       const data = await response.json()
       return data
     } catch (error) {
       console.error('Error fetching menu:', error)
       throw error
     }
   }

   // REMOVE/COMMENT OUT THE HARDCODED DATA
   ```

3. **Backend API Endpoints:**

   Your backend should provide these endpoints:

   **GET /api/menu**
   - Returns menu data organized by categories
   - Response format:
     ```json
     {
       "appetizers": [
         {
           "id": 1,
           "name": "Samosas",
           "description": "Crispy pastry...",
           "price": 5.99,
           "tags": ["vegetarian"],
           "image": "url_to_image"
         }
       ],
       "signature_dishes": [...],
       ...
     }
     ```

   **POST /api/reservations**
   - Accepts reservation data
   - Request body:
     ```json
     {
       "name": "John Doe",
       "phone": "123-456-7890",
       "email": "john@example.com",
       "partySize": "4 people",
       "date": "2024-12-25",
       "time": "7:00 PM"
     }
     ```
   - Response:
     ```json
     {
       "success": true,
       "message": "Reservation confirmed!",
       "reservationId": "abc123"
     }
     ```

   **POST /api/contact**
   - Accepts contact form data
   - Request body:
     ```json
     {
       "name": "John Doe",
       "email": "john@example.com",
       "subject": "Question",
       "message": "Hello..."
     }
     ```
   - Response:
     ```json
     {
       "success": true,
       "message": "Message sent successfully"
     }
     ```

## 📝 Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## 🎨 Customization

### Colors
Edit `src/style.css` to change the color scheme:
```css
:root {
  --color-primary: #ec7f13;
  --color-secondary: #5D4037;
  ...
}
```

### Menu Data
While in development mode, edit the hardcoded data in `src/services/api.js`.

### Restaurant Information
Update contact details, hours, and location in `src/views/Contact.vue`.

## 🚢 Deployment

### Build for Production
```bash
npm run build
```

This creates a `dist` folder with optimized files.

### Deploy to Netlify
1. Connect your GitHub repository to Netlify
2. Build command: `npm run build`
3. Publish directory: `dist`

### Deploy to Vercel
```bash
npm i -g vercel
vercel
```

### Deploy to Any Static Host
Upload the contents of the `dist` folder to your web server.

## 🐛 Troubleshooting

**Port already in use:**
```bash
lsof -ti:5173 | xargs kill -9
```

**Module errors:**
```bash
rm -rf node_modules package-lock.json
npm install
```

**API not working:**
- Check that your `.env` file has the correct `VITE_API_URL`
- Ensure your backend is running
- Check browser console for error messages

## 📱 Browser Support

- Chrome 88+
- Firefox 78+
- Safari 14+
- Edge 88+

## 📄 License

MIT License

---

**Happy Coding! 🎉**
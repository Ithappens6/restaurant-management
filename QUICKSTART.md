# 🚀 Quick Start Guide

## Option 1: Simple Local Server (No Build Required)

**Perfect for quick testing and development**

1. **Start a local server** (choose one):
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   
   # Node.js (if installed)
   npx serve .
   
   # PHP
   php -S localhost:8000
   ```

2. **Open browser**: `http://localhost:8000`

## Option 2: Development Server with Vue Router (Recommended)

**Best for full development with proper routing**

1. **Install Node.js** from [nodejs.org](https://nodejs.org/)

2. **Run setup script**:
   ```bash
   ./setup.sh
   ```

3. **Start development server**:
   ```bash
   npm run dev
   ```

4. **Open browser**: `http://localhost:5173`

## Option 3: Manual Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   ```

## 🔄 Switching Between Router and Non-Router Versions

In `index.html`, you can switch between:

- **Simple version** (current): Uses `js/app.js`
- **Router version**: Comment out `js/app.js` and uncomment `js/app-router.js`

## 📱 Testing on Mobile

1. **Find your computer's IP address**:
   ```bash
   # macOS/Linux
   ifconfig | grep "inet " | grep -v 127.0.0.1
   
   # Windows
   ipconfig
   ```

2. **Access from mobile**: `http://YOUR_IP:8000` or `http://YOUR_IP:5173`

## 🐛 Troubleshooting

- **Port already in use**: Kill the process or use a different port
- **Module errors**: Run `npm install` again
- **Router not working**: Make sure you're using the development server (`npm run dev`)

## 📦 Production Build

```bash
npm run build
npm run preview
```

The built files will be in the `dist/` folder.

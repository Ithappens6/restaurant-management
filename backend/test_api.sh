#!/bin/bash
# API Testing Script for Kurdie's Curry Restaurant Backend

echo "======================================"
echo "🍛 Testing Kurdie's Curry Backend API"
echo "======================================"
echo ""

BASE_URL="http://localhost:8000"

# Test Health Check
echo "1️⃣  Testing Health Check..."
curl -s $BASE_URL/health | python3 -m json.tool
echo ""

# Test Restaurant Status
echo "2️⃣  Testing Restaurant Status..."
curl -s $BASE_URL/api/restaurant/status | python3 -m json.tool
echo ""

# Test Menu
echo "3️⃣  Testing Menu (first 20 lines)..."
curl -s $BASE_URL/api/menu | python3 -m json.tool | head -20
echo "..."
echo ""

# Test Get Specific Menu Item
echo "4️⃣  Testing Get Menu Item (ID=1)..."
curl -s $BASE_URL/api/menu/items/1 | python3 -m json.tool
echo ""

# Test Create Reservation
echo "5️⃣  Testing Create Reservation..."
curl -s -X POST $BASE_URL/api/reservations \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "(555) 987-6543",
    "date": "2025-12-31",
    "time": "20:00",
    "party_size": 6,
    "special_requests": "Anniversary celebration"
  }' | python3 -m json.tool
echo ""

# Test Submit Contact Form
echo "6️⃣  Testing Contact Form..."
curl -s -X POST $BASE_URL/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "subject": "Catering Inquiry",
    "message": "I would like to inquire about catering services for 100 people."
  }' | python3 -m json.tool
echo ""

echo "======================================"
echo "✅ All tests completed!"
echo "======================================"
echo ""
echo "📚 For full API documentation, visit:"
echo "   http://localhost:8000/docs"
echo ""


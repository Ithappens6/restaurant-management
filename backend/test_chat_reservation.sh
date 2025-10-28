#!/bin/bash

# Test Chat Reservation Feature
# This script tests the chatbot's ability to create reservations

API_URL="http://localhost:8000/api"
RESTAURANT_ID="kurdiescurry"

echo "🧪 Testing Chat Reservation Tool"
echo "=================================="
echo ""

# Generate a session ID
SESSION_ID="test_$(date +%s)"

echo "📝 Session ID: $SESSION_ID"
echo ""

# Test 1: Ask about making a reservation
echo "Test 1: User wants to make a reservation"
echo "-----------------------------------------"
curl -X POST "$API_URL/restaurants/$RESTAURANT_ID/chat" \
  -H "Content-Type: application/json" \
  -H "ngrok-skip-browser-warning: true" \
  -d "{
    \"session_id\": \"$SESSION_ID\",
    \"restaurant_id\": \"$RESTAURANT_ID\",
    \"message\": \"I'd like to make a reservation for dinner\"
  }" | jq -r '.assistant_message'

echo ""
echo ""
sleep 2

# Test 2: Provide reservation details
echo "Test 2: Provide all reservation details"
echo "----------------------------------------"
curl -X POST "$API_URL/restaurants/$RESTAURANT_ID/chat" \
  -H "Content-Type: application/json" \
  -H "ngrok-skip-browser-warning: true" \
  -d "{
    \"session_id\": \"$SESSION_ID\",
    \"restaurant_id\": \"$RESTAURANT_ID\",
    \"message\": \"My name is John Doe, email is john@example.com, phone is 555-123-4567. I'd like to book for 4 people tomorrow at 7 PM. No special requests.\"
  }" | jq '.'

echo ""
echo ""
sleep 2

# Test 3: Check if reservation was created
echo "Test 3: Verify reservation in database"
echo "---------------------------------------"
cd /Users/lokesh/Desktop/restaurant/backend
source venv/bin/activate 2>/dev/null
python3 << 'EOF'
from app.database.base import SessionLocal
from app.database.models import ReservationModel

db = SessionLocal()
reservations = db.query(ReservationModel).order_by(ReservationModel.created_at.desc()).limit(3).all()

print("Recent Reservations:")
print("-" * 60)
for res in reservations:
    print(f"Name: {res.name}")
    print(f"Email: {res.email}")
    print(f"Phone: {res.phone}")
    print(f"Date: {res.date} at {res.time}")
    print(f"Party Size: {res.party_size}")
    print(f"Status: {res.status}")
    print(f"Created: {res.created_at}")
    print("-" * 60)

db.close()
EOF

echo ""
echo "✅ Test complete!"
echo ""
echo "Try it yourself:"
echo "  1. Open the chat widget"
echo "  2. Say: 'I want to make a reservation'"
echo "  3. Follow the chatbot's prompts"
echo "  4. The reservation will be created automatically!"


#!/bin/bash
# Test Chat API

echo "=== Testing Chat API ==="
echo ""

# Base URL
BASE_URL="http://localhost:8000/api/restaurants/kurdiescurry"

# Test 1: Generate Session ID
echo "1. Generating session ID..."
SESSION_RESPONSE=$(curl -s -X POST "${BASE_URL}/chat/session")
echo "Response: $SESSION_RESPONSE"
SESSION_ID=$(echo $SESSION_RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin)['session_id'])" 2>/dev/null || echo "test_session_$(date +%s)")
echo "Session ID: $SESSION_ID"
echo ""

# Test 2: Send first message
echo "2. Sending first chat message..."
curl -s -X POST "${BASE_URL}/chat" \
  -H "Content-Type: application/json" \
  -d "{
    \"session_id\": \"$SESSION_ID\",
    \"restaurant_id\": \"kurdiescurry\",
    \"message\": \"What are your vegetarian options?\"
  }" | python3 -m json.tool
echo ""

# Test 3: Send follow-up message
echo "3. Sending follow-up message..."
curl -s -X POST "${BASE_URL}/chat" \
  -H "Content-Type: application/json" \
  -d "{
    \"session_id\": \"$SESSION_ID\",
    \"restaurant_id\": \"kurdiescurry\",
    \"message\": \"What about vegan options?\"
  }" | python3 -m json.tool
echo ""

# Test 4: Get chat history
echo "4. Getting chat history..."
curl -s "${BASE_URL}/chat/history/$SESSION_ID" | python3 -m json.tool
echo ""

echo "=== Chat API Tests Complete ==="

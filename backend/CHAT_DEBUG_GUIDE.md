# Chat Service Debug Guide

## Current Implementation

### 1. **Using GPT-4.1 Model**
**Model:** `gpt-4.1`
**API:** Using standard `chat.completions.create()` with full tool calling support

### 2. **Tool Calling Enabled**
**Features:** 
- Full function calling support for reservations
- Proper message format with roles (system, user, assistant, tool)
- Two-step process: tool call → execution → final response

### 3. **Comprehensive Logging**
**Added:** Detailed logging throughout the entire flow
- Request details
- OpenAI API calls and responses
- Tool call execution
- Error handling with stack traces

## New Logging Output

When you send a chat message, you'll now see detailed logs:

```
============================================================
📨 NEW CHAT REQUEST
============================================================
🆔 Session ID: session_1761658497889_p2mzdog
🏪 Restaurant ID: kc-001
💬 User message: Hello, what's on the menu?
============================================================

🆕 Creating new session: session_1761658497889_p2mzdog
🤖 Calling OpenAI API for session: session_1761658497889_p2mzdog
📝 Messages count: 2
🔧 Tools enabled: True
✅ OpenAI Response received
📊 Response ID: chatcmpl-xyz123
📊 Model used: gpt-4.1
📊 Finish reason: stop
💬 Response message content: Hello! Here's our menu...
🔧 Has tool calls: False
✅ Regular response (no tool calls)
💾 Storing assistant message: Hello! Here's our menu...
✅ Message stored with ID: abc123
```

### For Tool Calls (Reservations)
```
🎯 Tool call detected: create_reservation
📋 Function args: {'name': 'John Doe', 'email': 'john@example.com', 'phone': '555-1234', ...}
📤 Function response: {"success": true, "reservation_id": "res_123"}
🔄 Calling OpenAI again with function results...
💬 Second response content: Great! I've created your reservation for John Doe on...
```

### For Errors
```
❌ ERROR in process_message: [error message]
❌ Error type: OpenAIError
❌ Traceback:
[full traceback here]
```

## How to Debug Empty Messages

With the new logging, check your backend logs (backend.log or console output) for:

1. **Check if OpenAI is being called:**
   - Look for: `🤖 Calling OpenAI API for session:`
   - If missing, the error happened before the API call

2. **Check the OpenAI response:**
   - Look for: `💬 Response message content:`
   - If it shows `None` or empty, OpenAI returned empty content

3. **Check finish reason:**
   - Look for: `📊 Finish reason:`
   - Should be `stop` for normal completion
   - If `length`, response was cut off (increase max_tokens)
   - If `tool_calls`, check tool call handling

4. **Check for errors:**
   - Look for: `❌ ERROR in process_message:`
   - This will show the full error details with stack trace

## Common Issues

### Empty Message Causes:

1. **API Key Issue**
   - Check: `OPENAI_API_KEY` is set in environment or config
   - Error will show: "OPENAI_API_KEY is not configured"

2. **Model Not Available**
   - Using: `gpt-4.1`
   - If you don't have access to gpt-4.1, you can use:
     - `gpt-4o` or `gpt-4o-mini` (newer models)
     - `gpt-4-turbo` or `gpt-4-turbo-preview`
     - `gpt-3.5-turbo` (cheaper, faster, but less capable)

3. **Response Empty**
   - Check: `💬 Response message content:`
   - If None, check if the model is accessible
   - Verify API key has proper permissions
   - Check finish_reason for clues

4. **Tool Calling Issues**
   - Check: `🔧 Has tool calls: True/False`
   - If True, follow the tool call flow logs
   - Check: `🔄 Calling OpenAI again with function results...`
   - The second call should produce the final response

## Testing

### Test in Terminal
```bash
cd backend
tail -f backend.log
```

### Test via API
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "restaurant_id": "kc-001",
    "session_id": "test_session_123",
    "message": "Hello, what is your menu?"
  }'
```

### Check OpenAI API Key
```bash
cd backend
python3 -c "from app.core.config import settings; print(settings.openai_api_key)"
```

## Quick Fixes

### If Still Getting Empty Messages:

1. **Restart the backend server** to pick up changes
   ```bash
   # Stop the current process (Ctrl+C)
   cd backend
   source venv/bin/activate
   python run.py
   ```

2. **Check OpenAI API status**
   - Visit: https://status.openai.com/

3. **Verify API Key has credits**
   - Visit: https://platform.openai.com/usage

4. **Try a different model**
   - If gpt-4.1 not available, try:
     - `gpt-4o-mini` (recommended)
     - `gpt-4-turbo-preview`
     - `gpt-3.5-turbo` (most compatible)

5. **Check tool calling permissions**
   - Some API keys may have restricted function calling
   - Test with a simple message first (no reservation)

## Monitoring

Watch logs in real-time:
```bash
cd backend
tail -f backend.log | grep -E "(📨|💬|❌|✅)"
```

This will show only the key log lines:
- 📨 New requests
- 💬 Message content
- ❌ Errors
- ✅ Success states


<template>
  <div class="chat-widget-container">
    <!-- Chat Button (when closed) -->
    <button
      v-if="!isOpen"
      @click="toggleChat"
      class="chat-bubble"
      aria-label="Open chat"
    >
      <span class="material-symbols-outlined">chat</span>
    </button>

    <!-- Chat Window (when open) -->
    <transition name="slide-up">
      <div v-if="isOpen" class="chat-window">
        <!-- Header -->
        <div class="chat-header">
          <div class="chat-header-content">
            <span class="material-symbols-outlined">smart_toy</span>
            <div>
              <h3>Kurdie's Curry Assistant</h3>
              <p>Ask me anything!</p>
            </div>
          </div>
          <div class="header-actions">
            <button 
              v-if="messages.length > 0" 
              @click="clearHistory" 
              class="clear-btn" 
              aria-label="Clear chat history"
              title="Clear chat"
            >
              <span class="material-symbols-outlined">delete</span>
            </button>
            <button @click="toggleChat" class="close-btn" aria-label="Close chat">
              <span class="material-symbols-outlined">close</span>
            </button>
          </div>
        </div>

        <!-- Messages Container -->
        <div class="chat-messages" ref="messagesContainer">
          <!-- Welcome Message -->
          <div v-if="messages.length === 0" class="message bot-message">
            <div class="message-avatar">
              <span class="material-symbols-outlined">smart_toy</span>
            </div>
            <div class="message-content">
              <p>👋 Hello! I'm your AI assistant. How can I help you today?</p>
            </div>
          </div>

          <!-- Chat Messages -->
          <div
            v-for="(message, index) in messages"
            :key="index"
            :class="['message', message.role === 'user' ? 'user-message' : 'bot-message']"
          >
            <div v-if="message.role === 'assistant'" class="message-avatar">
              <span class="material-symbols-outlined">smart_toy</span>
            </div>
            <div class="message-content">
              <p>{{ message.content }}</p>
              <span class="message-time">{{ formatTime(message.timestamp) }}</span>
            </div>
            <div v-if="message.role === 'user'" class="message-avatar user-avatar">
              <span class="material-symbols-outlined">person</span>
            </div>
          </div>

          <!-- Typing Indicator -->
          <div v-if="isTyping" class="message bot-message">
            <div class="message-avatar">
              <span class="material-symbols-outlined">smart_toy</span>
            </div>
            <div class="message-content">
              <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        </div>

        <!-- Input Area -->
        <div class="chat-input-area">
          <form @submit.prevent="sendMessage" class="chat-input-form">
            <input
              v-model="userInput"
              type="text"
              placeholder="Type your message..."
              :disabled="isTyping"
              ref="messageInput"
              class="chat-input"
            />
            <button
              type="submit"
              :disabled="!userInput.trim() || isTyping"
              class="send-btn"
              aria-label="Send message"
            >
              <span class="material-symbols-outlined">send</span>
            </button>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, nextTick, watch } from 'vue'
import { sendChatMessage } from '@/services/api'
import { RESTAURANT_ID } from '@/config/restaurant'

// State
const isOpen = ref(false)
const userInput = ref('')
const messages = ref([])
const isTyping = ref(false)
const sessionId = ref(generateSessionId())
const messagesContainer = ref(null)
const messageInput = ref(null)

// Generate unique session ID
function generateSessionId() {
  const timestamp = Date.now()
  const random = Math.random().toString(36).substring(2, 9)
  return `session_${timestamp}_${random}`
}

// Toggle chat window
function toggleChat() {
  isOpen.value = !isOpen.value
  if (isOpen.value) {
    nextTick(() => {
      messageInput.value?.focus()
    })
  }
}

// Clear chat history
function clearHistory() {
  if (confirm('Are you sure you want to clear the chat history?')) {
    messages.value = []
    sessionId.value = generateSessionId()
  }
}

// Format timestamp
function formatTime(timestamp) {
  const date = new Date(timestamp)
  return date.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' })
}

// Send message
async function sendMessage() {
  if (!userInput.value.trim() || isTyping.value) return

  const messageText = userInput.value.trim()
  userInput.value = ''

  // Add user message to chat
  messages.value.push({
    role: 'user',
    content: messageText,
    timestamp: Date.now()
  })

  // Scroll to bottom
  scrollToBottom()

  // Show typing indicator
  isTyping.value = true

  try {
    // Send to backend
    const response = await sendChatMessage({
      restaurant_id: RESTAURANT_ID,
      session_id: sessionId.value,
      message: messageText,
      chat_history: messages.value.slice(0, -1).map(msg => ({
        role: msg.role,
        content: msg.content
      }))
    })

    // Add bot response
    messages.value.push({
      role: 'assistant',
      content: response.assistant_message,
      timestamp: Date.now()
    })

    // Scroll to bottom
    scrollToBottom()
  } catch (error) {
    console.error('Chat error:', error)
    messages.value.push({
      role: 'assistant',
      content: 'Sorry, I encountered an error. Please try again.',
      timestamp: Date.now()
    })
  } finally {
    isTyping.value = false
  }
}

// Scroll to bottom of messages
function scrollToBottom() {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}

// Watch messages to auto-scroll
watch(() => messages.value.length, () => {
  scrollToBottom()
})
</script>

<style scoped>
.chat-widget-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

/* Chat Bubble Button */
.chat-bubble {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  position: fixed;
  bottom: 20px;
  right: 20px;
}

.chat-bubble:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

.chat-bubble .material-symbols-outlined {
  font-size: 28px;
}

/* Chat Window */
.chat-window {
  width: 380px;
  height: 600px;
  max-height: 80vh;
  background: white;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: fixed;
  bottom: 20px;
  right: 20px;
}

/* Chat Header */
.chat-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-header-content {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-header-content .material-symbols-outlined {
  font-size: 32px;
}

.chat-header h3 {
  margin: 0;
  font-size: 16px;
  font-weight: 600;
}

.chat-header p {
  margin: 0;
  font-size: 12px;
  opacity: 0.9;
}

.header-actions {
  display: flex;
  gap: 8px;
}

.clear-btn,
.close-btn {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.clear-btn:hover,
.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.clear-btn .material-symbols-outlined,
.close-btn .material-symbols-outlined {
  font-size: 20px;
}

/* Messages Container */
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  background: #f7f7f8;
}

/* Message Styles */
.message {
  display: flex;
  gap: 8px;
  margin-bottom: 16px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.user-avatar {
  background: #4a5568;
}

.message-avatar .material-symbols-outlined {
  font-size: 20px;
}

.message-content {
  max-width: 70%;
  padding: 10px 14px;
  border-radius: 12px;
  position: relative;
}

.bot-message .message-content {
  background: white;
  border-bottom-left-radius: 4px;
}

.user-message {
  flex-direction: row-reverse;
}

.user-message .message-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-bottom-right-radius: 4px;
}

.message-content p {
  margin: 0;
  font-size: 14px;
  line-height: 1.5;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.message-time {
  font-size: 10px;
  opacity: 0.6;
  display: block;
  margin-top: 4px;
}

/* Typing Indicator */
.typing-indicator {
  display: flex;
  gap: 4px;
  padding: 8px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #667eea;
  animation: bounce 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes bounce {
  0%, 60%, 100% {
    transform: translateY(0);
  }
  30% {
    transform: translateY(-8px);
  }
}

/* Input Area */
.chat-input-area {
  padding: 16px;
  background: white;
  border-top: 1px solid #e5e7eb;
}

.chat-input-form {
  display: flex;
  gap: 8px;
}

.chat-input {
  flex: 1;
  padding: 10px 14px;
  border: 1px solid #e5e7eb;
  border-radius: 24px;
  outline: none;
  font-size: 14px;
  transition: border-color 0.2s;
}

.chat-input:focus {
  border-color: #667eea;
}

.send-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.send-btn:hover:not(:disabled) {
  transform: scale(1.05);
}

.send-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Slide Up Animation */
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease;
}

.slide-up-enter-from,
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Mobile Responsive */
@media (max-width: 640px) {
  .chat-bubble {
    bottom: 10px;
    right: 10px;
  }

  .chat-window {
    width: calc(100vw - 20px);
    height: calc(100vh - 100px);
    max-height: none;
    bottom: 10px;
    right: 10px;
  }
}

/* Scrollbar Styles */
.chat-messages::-webkit-scrollbar {
  width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.chat-messages::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>

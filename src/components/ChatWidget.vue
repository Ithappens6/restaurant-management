<!--
  ChatWidget Component
  
  AI-powered chat assistant with:
  - Markdown rendering (bold, italic, lists, code, tables)
  - Session-based conversation history
  - Real-time typing indicators
  - Automatic scrolling
  - Clear history functionality
  
  Features:
  - Uses marked.js for markdown parsing
  - DOMPurify for XSS protection
  - Persistent session across page reloads
  - Mobile-optimized design
-->

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
              <div class="message-text">
                <p>👋 Hello! I'm your AI assistant. How can I help you today?</p>
              </div>
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
              <div 
                class="message-text" 
                v-html="parseMarkdown(message.content)"
              ></div>
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
/**
 * Chat Widget Component Logic
 * 
 * Manages:
 * - Chat state (open/closed, messages, typing indicator)
 * - Session management with unique IDs
 * - Message sending and receiving
 * - Markdown parsing and rendering
 * - Auto-scrolling to latest message
 */

import { ref, nextTick, watch } from 'vue'
import { sendChatMessage } from '@/services/api'
import { RESTAURANT_ID } from '@/config/restaurant'
import { marked } from 'marked'
import DOMPurify from 'dompurify'

// Configure markdown parser
marked.setOptions({
  breaks: true,  // Convert line breaks to <br>
  gfm: true,     // GitHub Flavored Markdown (tables, strikethrough, etc.)
})

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
  messages.value = []
  sessionId.value = generateSessionId()
}

// Format timestamp
function formatTime(timestamp) {
  const date = new Date(timestamp)
  return date.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' })
}

// Parse markdown content safely
function parseMarkdown(content) {
  if (!content) return ''
  
  try {
    // Parse markdown to HTML
    const rawHTML = marked.parse(content)
    // Sanitize HTML to prevent XSS attacks
    return DOMPurify.sanitize(rawHTML, {
      ALLOWED_TAGS: ['p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
                     'ul', 'ol', 'li', 'blockquote', 'code', 'pre', 'a', 'hr', 'table', 
                     'thead', 'tbody', 'tr', 'th', 'td'],
      ALLOWED_ATTR: ['href', 'target', 'rel']
    })
  } catch (error) {
    console.error('Markdown parsing error:', error)
    return content
  }
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
    // Note: Backend pulls chat history from database using session_id
    const response = await sendChatMessage({
      restaurant_id: RESTAURANT_ID,
      session_id: sessionId.value,
      message: messageText
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
  bottom: 75px;
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
  bottom: 75px;
  right: 20px;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.chat-bubble:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

.chat-bubble:active {
  transform: scale(0.95);
}

.chat-bubble .material-symbols-outlined {
  font-size: 28px;
}

/* Chat Window */
.chat-window {
  width: 380px;
  height: 550px;
  max-height: 70vh;
  background: white;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: fixed;
  bottom: 75px;
  right: 20px;
  transition: all 0.3s ease;
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
  transition: all 0.2s;
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
}

.clear-btn:hover,
.close-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.clear-btn:active,
.close-btn:active {
  transform: scale(0.9);
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
  max-width: 75%;
  padding: 10px 14px;
  border-radius: 12px;
  position: relative;
  word-break: break-word;
  overflow-wrap: break-word;
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

/* Markdown Styling */
.message-text {
  font-size: 14px;
  line-height: 1.6;
}

.message-text p {
  margin: 0 0 8px 0;
}

.message-text p:last-child {
  margin-bottom: 0;
}

.message-text h1,
.message-text h2,
.message-text h3,
.message-text h4,
.message-text h5,
.message-text h6 {
  margin: 8px 0 6px 0;
  font-weight: 600;
  line-height: 1.3;
}

.message-text h1 { font-size: 18px; }
.message-text h2 { font-size: 16px; }
.message-text h3 { font-size: 15px; }
.message-text h4 { font-size: 14px; }
.message-text h5 { font-size: 13px; }
.message-text h6 { font-size: 12px; }

.message-text ul,
.message-text ol {
  margin: 6px 0 6px 0;
  padding-left: 20px;
}

.message-text li {
  margin: 2px 0;
}

.message-text code {
  background: rgba(0, 0, 0, 0.05);
  padding: 2px 5px;
  border-radius: 3px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 13px;
}

.user-message .message-text code {
  background: rgba(255, 255, 255, 0.2);
}

.message-text pre {
  background: rgba(0, 0, 0, 0.05);
  padding: 8px 10px;
  border-radius: 6px;
  overflow-x: auto;
  margin: 6px 0;
}

.user-message .message-text pre {
  background: rgba(255, 255, 255, 0.15);
}

.message-text pre code {
  background: none;
  padding: 0;
}

.message-text blockquote {
  border-left: 3px solid rgba(102, 126, 234, 0.3);
  padding-left: 10px;
  margin: 6px 0;
  color: rgba(0, 0, 0, 0.7);
}

.user-message .message-text blockquote {
  border-left-color: rgba(255, 255, 255, 0.4);
  color: rgba(255, 255, 255, 0.9);
}

.message-text strong {
  font-weight: 600;
}

.message-text em {
  font-style: italic;
}

.message-text a {
  color: #667eea;
  text-decoration: underline;
  transition: opacity 0.2s;
}

.user-message .message-text a {
  color: white;
  text-decoration: underline;
}

.message-text a:hover {
  opacity: 0.8;
}

.message-text hr {
  border: none;
  border-top: 1px solid rgba(0, 0, 0, 0.1);
  margin: 8px 0;
}

.user-message .message-text hr {
  border-top-color: rgba(255, 255, 255, 0.3);
}

.message-text table {
  border-collapse: collapse;
  width: 100%;
  margin: 6px 0;
  font-size: 13px;
}

.message-text th,
.message-text td {
  border: 1px solid rgba(0, 0, 0, 0.1);
  padding: 4px 8px;
  text-align: left;
}

.message-text th {
  background: rgba(0, 0, 0, 0.05);
  font-weight: 600;
}

.user-message .message-text th,
.user-message .message-text td {
  border-color: rgba(255, 255, 255, 0.3);
}

.user-message .message-text th {
  background: rgba(255, 255, 255, 0.15);
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
  font-family: inherit;
  -webkit-appearance: none;
  touch-action: manipulation;
}

.chat-input:focus {
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.chat-input::placeholder {
  color: #9ca3af;
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
  -webkit-tap-highlight-color: transparent;
  touch-action: manipulation;
  flex-shrink: 0;
}

.send-btn:hover:not(:disabled) {
  transform: scale(1.05);
}

.send-btn:active:not(:disabled) {
  transform: scale(0.95);
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

/* Tablet Responsive */
@media (max-width: 768px) and (min-width: 641px) {
  .chat-window {
    width: 360px;
    height: 500px;
    max-height: 65vh;
  }
}

/* Mobile Responsive */
@media (max-width: 640px) {
  .chat-bubble {
    width: 56px;
    height: 56px;
    bottom: 76px;
    right: 16px;
  }

  .chat-bubble .material-symbols-outlined {
    font-size: 26px;
  }

  .chat-window {
    width: calc(100vw - 32px);
    height: 500px;
    max-height: 60vh;
    bottom: 76px;
    right: 16px;
    left: 16px;
    border-radius: 20px;
  }

  .chat-header {
    padding: 14px;
  }

  .chat-header h3 {
    font-size: 15px;
  }

  .chat-header p {
    font-size: 11px;
  }

  .chat-header-content .material-symbols-outlined {
    font-size: 28px;
  }

  .chat-messages {
    padding: 12px;
  }

  .message {
    margin-bottom: 12px;
  }

  .message-avatar {
    width: 28px;
    height: 28px;
  }

  .message-avatar .material-symbols-outlined {
    font-size: 18px;
  }

  .message-content {
    max-width: 80%;
    padding: 9px 12px;
    font-size: 14px;
  }

  .message-content p {
    font-size: 13px;
    line-height: 1.4;
  }

  .chat-input-area {
    padding: 12px;
  }

  .chat-input {
    padding: 9px 12px;
    font-size: 14px;
  }

  .send-btn {
    width: 38px;
    height: 38px;
  }

  .header-actions {
    gap: 6px;
  }

  .clear-btn,
  .close-btn {
    width: 30px;
    height: 30px;
  }

  .clear-btn .material-symbols-outlined,
  .close-btn .material-symbols-outlined {
    font-size: 18px;
  }
}

/* Small Mobile (iPhone SE, etc) */
@media (max-width: 380px) {
  .chat-window {
    width: calc(100vw - 24px);
    height: 480px;
    max-height: 65vh;
    left: 12px;
    right: 12px;
    bottom: 72px;
  }

  .chat-bubble {
    bottom: 72px;
    right: 12px;
  }

  .message-content {
    max-width: 85%;
  }
}

/* Landscape Mobile */
@media (max-width: 896px) and (max-height: 414px) and (orientation: landscape) {
  .chat-window {
    width: 360px;
    height: calc(100vh - 60px);
    max-height: 90vh;
    bottom: 10px;
    right: 10px;
  }

  .chat-messages {
    padding: 10px;
  }

  .message {
    margin-bottom: 10px;
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

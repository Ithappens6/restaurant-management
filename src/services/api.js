/**
 * API Service for Backend Integration
 * 
 * This file handles all API calls to the FastAPI backend
 * Backend runs on: http://localhost:8000
 */

import { getRestaurantApiUrl, RESTAURANT_ID } from '@/config/restaurant'

/**
 * Common fetch configuration for all API calls
 */
const FETCH_CONFIG = {
  mode: 'cors',
  credentials: 'omit',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'ngrok-skip-browser-warning': 'true',  // Skip ngrok browser warning page
  }
}

/**
 * GET Menu Data from API
 * @param {string} category - Optional category filter (e.g., 'signature_dishes')
 * @returns {Promise<Object>} Menu data organized by categories
 */
export async function fetchMenu(category = null) {
  try {
    let url = getRestaurantApiUrl('/menu')
    
    // Add category filter if provided
    if (category) {
      url += `?category=${encodeURIComponent(category)}`
    }
    
    console.log('🍽️ Fetching menu from:', url)
    
    const response = await fetch(url, {
      ...FETCH_CONFIG,
      method: 'GET',
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log('Menu data received:', data)
    
    // Backend returns: { category_name: [items], ... }
    // Frontend expects: { category_name: [items], ... }
    // No transformation needed - backend already returns correct format!
    
    return data
  } catch (error) {
    console.error('Error fetching menu:', error)
    throw error
  }
}

/**
 * GET Signature Dishes from API
 * Convenience function to fetch only signature dishes
 * @returns {Promise<Array>} Array of signature dish items
 */
export async function fetchSignatureDishes() {
  try {
    const data = await fetchMenu('signature_dishes')
    // Return the array of items from the signature_dishes category
    return data.signature_dishes || []
  } catch (error) {
    console.error('Error fetching signature dishes:', error)
    throw error
  }
}

/**
 * POST Reservation to API
 * @param {Object} reservationData - Reservation form data
 * @returns {Promise<Object>} Response from server
 */
export async function submitReservation(reservationData) {
  try {
    const url = getRestaurantApiUrl('/reservations')
    console.log('📅 Submitting reservation to:', url)
    
    // Transform frontend data to backend format
    const payload = {
      restaurant_id: RESTAURANT_ID,
      name: reservationData.name,
      email: reservationData.email || undefined,
      phone: reservationData.phone,
      date: reservationData.date,
      time: reservationData.time,
      party_size: parseInt(reservationData.partySize) || 2,
      special_requests: reservationData.specialRequests || undefined
    }
    
    console.log('Reservation payload:', payload)
    
    const response = await fetch(url, {
      ...FETCH_CONFIG,
      method: 'POST',
      body: JSON.stringify(payload)
    })
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.detail || errorData.message || 'Failed to book reservation.')
    }
    
    const result = await response.json()
    console.log('Reservation response:', result)
    
    // Backend returns: { success: true, message: "...", reservation_id: "..." }
    return {
      success: result.success,
      message: result.message,
      reservationId: result.reservation_id
    }
  } catch (error) {
    console.error('Reservation error:', error)
    throw error
  }
}

/**
 * GET Restaurant Status (Open/Closed)
 * @returns {Promise<Object>} Restaurant status
 */
export async function getRestaurantStatus() {
  try {
    const url = getRestaurantApiUrl('/status')
    console.log('🕐 Fetching restaurant status from:', url)
    
    const response = await fetch(url, {
      ...FETCH_CONFIG,
      method: 'GET',
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log('Restaurant status received:', data)
    
    // Backend returns: { isOpen: true/false, message: "..." }
    return {
      isOpen: data.isOpen,
      message: data.message
    }
  } catch (error) {
    console.error('Error fetching restaurant status:', error)
    throw error
  }
}

/**
 * POST Contact Form to API
 * @param {Object} contactData - Contact form data
 * @returns {Promise<Object>} Response from server
 */
export async function submitContactForm(contactData) {
  try {
    const url = getRestaurantApiUrl('/contact')
    console.log('📧 Submitting contact form to:', url)
    
    // Transform frontend data to backend format
    const payload = {
      restaurant_id: RESTAURANT_ID,
      name: contactData.name,
      email: contactData.email,
      subject: contactData.subject || undefined,
      message: contactData.message
    }
    
    console.log('Contact form payload:', payload)
    
    const response = await fetch(url, {
      ...FETCH_CONFIG,
      method: 'POST',
      body: JSON.stringify(payload)
    })
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.detail || errorData.message || 'Failed to send message.')
    }
    
    const result = await response.json()
    console.log('Contact form response:', result)
    
    // Backend returns: { success: true, message: "..." }
    return {
      success: result.success,
      message: result.message
    }
  } catch (error) {
    console.error('Contact form error:', error)
    throw error
  }
}

/**
 * GET Restaurant Information
 * @returns {Promise<Object>} Restaurant info (name, address, phone, email)
 */
export async function getRestaurantInfo() {
  try {
    const url = getRestaurantApiUrl('/info')
    console.log('Fetching restaurant info from:', url)
    
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log('Restaurant info received:', data)
    return data
  } catch (error) {
    console.error('Error fetching restaurant info:', error)
    throw error
  }
}

/**
 * GET Restaurant Business Hours
 * @returns {Promise<Object>} Business hours by day
 */
export async function getRestaurantHours() {
  try {
    const url = getRestaurantApiUrl('/hours')
    console.log('Fetching restaurant hours from:', url)
    
    const response = await fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data = await response.json()
    console.log('Restaurant hours received:', data)
    return data
  } catch (error) {
    console.error('Error fetching restaurant hours:', error)
    throw error
  }
}

/**
 * POST Chat Message to AI Assistant
 * @param {Object} chatData - Chat message data
 * @returns {Promise<Object>} AI response
 */
export async function sendChatMessage(chatData) {
  try {
    const url = getRestaurantApiUrl('/chat')
    console.log('💬 Sending chat message to:', url)
    console.log('💬 Message:', chatData.message)
    
    const response = await fetch(url, {
      ...FETCH_CONFIG,
      method: 'POST',
      body: JSON.stringify(chatData)
    })
    
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}))
      throw new Error(errorData.detail || 'Failed to send chat message')
    }
    
    const result = await response.json()
    console.log('💬 Chat response received')
    return result
    
  } catch (error) {
    console.error('Chat error:', error)
    throw error
  }
}

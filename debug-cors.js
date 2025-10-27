// Debug CORS Issue - Run this in browser console
console.log('=== CORS DEBUG ===')

// Test 1: Check if config is correct
import { RESTAURANT_CONFIG, getRestaurantApiUrl } from './src/config/restaurant.js'
console.log('Config:', RESTAURANT_CONFIG)

// Test 2: Test a simple fetch
const testUrl = 'http://localhost:8000/api/restaurants/kurdiescurry/status'
console.log('Testing URL:', testUrl)

fetch(testUrl, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  mode: 'cors',
  credentials: 'omit',
})
.then(response => {
  console.log('✅ Success! Status:', response.status)
  return response.json()
})
.then(data => {
  console.log('✅ Data received:', data)
})
.catch(error => {
  console.log('❌ Error:', error)
  console.log('Error details:', error.message)
})

// Test 3: Check what URLs are being called
console.log('Menu URL:', getRestaurantApiUrl('/menu'))
console.log('Status URL:', getRestaurantApiUrl('/status'))

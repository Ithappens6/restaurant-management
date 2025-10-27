// Test Configuration - Run this in browser console to debug
console.log('=== RESTAURANT CONFIG TEST ===')

// Import the config
import { RESTAURANT_CONFIG, getRestaurantApiUrl } from './src/config/restaurant.js'

console.log('Restaurant ID:', RESTAURANT_CONFIG.restaurantId)
console.log('API Base URL:', RESTAURANT_CONFIG.apiBaseUrl)
console.log('Menu URL:', getRestaurantApiUrl('/menu'))
console.log('Status URL:', getRestaurantApiUrl('/status'))

// Test if URLs are correct
const expectedUrls = {
  menu: 'http://localhost:8000/api/restaurants/kurdiescurry/menu',
  status: 'http://localhost:8000/api/restaurants/kurdiescurry/status',
  reservations: 'http://localhost:8000/api/restaurants/kurdiescurry/reservations',
  contact: 'http://localhost:8000/api/restaurants/kurdiescurry/contact'
}

console.log('=== EXPECTED URLs ===')
Object.entries(expectedUrls).forEach(([key, url]) => {
  console.log(`${key}:`, url)
})

console.log('=== ACTUAL URLs ===')
console.log('Menu:', getRestaurantApiUrl('/menu'))
console.log('Status:', getRestaurantApiUrl('/status'))
console.log('Reservations:', getRestaurantApiUrl('/reservations'))
console.log('Contact:', getRestaurantApiUrl('/contact'))

// Check if URLs match
const actualMenuUrl = getRestaurantApiUrl('/menu')
const expectedMenuUrl = expectedUrls.menu

if (actualMenuUrl === expectedMenuUrl) {
  console.log('✅ Configuration is correct!')
} else {
  console.log('❌ Configuration mismatch!')
  console.log('Expected:', expectedMenuUrl)
  console.log('Actual:', actualMenuUrl)
}

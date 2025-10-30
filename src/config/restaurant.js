/**
 * Restaurant Configuration
 * 
 * This file contains restaurant-specific settings including the unique restaurant ID
 * used for API calls to the backend.
 * 
 * TODO: In the future, this could be:
 * - Loaded from environment variables
 * - Determined by subdomain (kurdiescurry.example.com)
 * - Selected via URL path (/restaurants/kurdiescurry)
 * - Stored in localStorage for multi-restaurant selection
 */

import CONFIG from './env.config.js'

export const RESTAURANT_CONFIG = {
  // Unique identifier for this restaurant (used in API calls)
  restaurantId: import.meta.env.VITE_RESTAURANT_ID || 'kurdiescurry',
  
  // Backend API base URL (from environment config)
  apiBaseUrl: CONFIG.apiBaseUrl,
  
  // Restaurant display information (can be fetched from API later)
  displayName: "Kurdie's Curry",
  
  // Feature flags
  features: {
    onlineReservations: true,
    contactForm: true,
    menuDisplay: true,
  }
}

// Helper function to get API endpoint for this restaurant
export function getRestaurantApiUrl(endpoint) {
  return `${RESTAURANT_CONFIG.apiBaseUrl}/restaurants/${RESTAURANT_CONFIG.restaurantId}${endpoint}`
}

// Export individual values for convenience
export const RESTAURANT_ID = RESTAURANT_CONFIG.restaurantId
export const API_BASE_URL = RESTAURANT_CONFIG.apiBaseUrl


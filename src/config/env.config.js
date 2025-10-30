/**
 * Environment Configuration
 * 
 * This file manages environment-specific settings (development, staging, production)
 * Configuration is determined by:
 * 1. Environment variables (highest priority)
 * 2. NODE_ENV/MODE detection (auto-detect)
 * 3. Default values (fallback)
 */

const ENV = {
  development: {
    apiBaseUrl: 'http://localhost:8000/api',
    debug: true,
    enableMocks: false,
  },
  staging: {
    apiBaseUrl: 'https://staging-api.kurdiescurry.com/api',
    debug: true,
    enableMocks: false,
  },
  production: {
    apiBaseUrl: 'https://api.kurdiescurry.com/api',
    debug: false,
    enableMocks: false,
  }
}

// Detect current environment
const currentEnv = import.meta.env.MODE || 'development'

// Get config for current environment
const envConfig = ENV[currentEnv] || ENV.development

// Export final config with environment variable overrides
export const CONFIG = {
  // API Configuration
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL || envConfig.apiBaseUrl,
  
  // Environment info
  environment: currentEnv,
  isDevelopment: currentEnv === 'development',
  isStaging: currentEnv === 'staging',
  isProduction: currentEnv === 'production',
  
  // Debug settings
  debug: import.meta.env.VITE_DEBUG === 'true' || envConfig.debug,
  enableMocks: import.meta.env.VITE_ENABLE_MOCKS === 'true' || envConfig.enableMocks,
  
  // Logging
  logLevel: import.meta.env.VITE_LOG_LEVEL || (envConfig.debug ? 'debug' : 'error'),
}

// Log config in development
if (CONFIG.isDevelopment && CONFIG.debug) {
  console.log('🔧 Environment Config:', {
    environment: CONFIG.environment,
    apiBaseUrl: CONFIG.apiBaseUrl,
    debug: CONFIG.debug
  })
}

export default CONFIG


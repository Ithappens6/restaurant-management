import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 5173,
    open: true,
    host: true, // Listen on all addresses including LAN and public
    allowedHosts: [
      '.ngrok-free.app',
      '.ngrok.io',
      'localhost'
    ]
    // Removed hmr.clientPort: 443 - was causing requests to localhost:443
  }
})
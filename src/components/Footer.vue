<template>
  <nav class="fixed bottom-0 left-0 right-0 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700 flex justify-around items-center h-16 z-50">
    <router-link 
      to="/" 
      :class="currentRoute === 'Home' ? 'text-primary' : 'text-gray-500 dark:text-gray-400'" 
      class="flex flex-col items-center hover:text-primary dark:hover:text-primary transition-colors"
    >
      <span class="material-symbols-outlined">home</span>
      <span class="text-xs">Home</span>
    </router-link>
    
    <router-link 
      to="/menu" 
      :class="currentRoute === 'Menu' ? 'text-primary' : 'text-gray-500 dark:text-gray-400'" 
      class="flex flex-col items-center hover:text-primary dark:hover:text-primary transition-colors"
    >
      <span class="material-symbols-outlined">restaurant_menu</span>
      <span class="text-xs">Menu</span>
    </router-link>
    
    <router-link 
      to="/reservations" 
      :class="currentRoute === 'Reservations' ? 'text-primary' : 'text-gray-500 dark:text-gray-400'" 
      class="flex flex-col items-center hover:text-primary dark:hover:text-primary transition-colors"
    >
      <span class="material-symbols-outlined">book_online</span>
      <span class="text-xs">Reserve</span>
    </router-link>
    
    <router-link 
      to="/contact" 
      :class="currentRoute === 'Contact' ? 'text-primary' : 'text-gray-500 dark:text-gray-400'" 
      class="flex flex-col items-center hover:text-primary dark:hover:text-primary transition-colors"
    >
      <span class="material-symbols-outlined">phone</span>
      <span class="text-xs">Contact</span>
    </router-link>
  </nav>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const currentRoute = computed(() => route.name)
</script>


<template>
  <div class="flex flex-col min-h-screen">
    <Header title="Our Menu" />
    
    <main class="flex-grow pb-20">
      <!-- Menu Headers (Filters & Categories) -->
      <div class="sticky top-[72px] z-10 bg-background-light dark:bg-background-dark">
        <!-- Filter Chips -->
        <div class="px-4 pb-3">
          <div class="flex items-center gap-2 overflow-x-auto whitespace-nowrap pb-2">
            <button 
              v-for="filter in menuFilters" 
              :key="filter.value"
              @click="activeMenuFilter = filter.value"
              :class="activeMenuFilter === filter.value ? 'bg-primary text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-200'"
              class="px-4 py-2 text-sm font-medium rounded-full transition-colors"
            >
              {{ filter.name }}
            </button>
          </div>
        </div>
        
        <!-- Category Nav -->
        <div class="overflow-x-auto whitespace-nowrap">
          <div class="flex border-b border-gray-200 dark:border-gray-700 px-4 justify-start space-x-4">
            <a 
              v-for="(items, categorySlug) in filteredMenu" 
              :key="categorySlug"
              :href="'#' + categorySlug"
              @click="activeMenuCategory = categorySlug"
              :class="activeMenuCategory === categorySlug ? 'border-b-primary text-primary' : 'border-b-transparent text-gray-500 dark:text-gray-400 hover:text-primary'"
              class="flex flex-col items-center justify-center border-b-[3px] pb-[13px] pt-4 px-2"
            >
              <p class="text-sm font-bold leading-normal tracking-[0.015em] capitalize">
                {{ categorySlug.replace('_', ' ') }}
              </p>
            </a>
          </div>
        </div>
      </div>

      <!-- Menu List -->
      <div class="p-4 space-y-8">
        <div v-if="isLoadingMenu" class="text-center p-8">
          <p>Loading menu...</p>
        </div>
        <div v-else-if="Object.keys(filteredMenu).length === 0" class="text-center p-8">
          <p>No items match your filter.</p>
        </div>
        
        <!-- Loop through each Category -->
        <div v-else v-for="(items, categorySlug) in filteredMenu" :key="categorySlug" :id="categorySlug">
          <h3 class="text-text-light dark:text-text-dark text-lg font-bold leading-tight tracking-[-0.015em] px-4 pb-2 pt-4 capitalize">
            {{ categorySlug.replace('_', ' ') }}
          </h3>
          <div class="space-y-4">
            <!-- Loop through each Item in Category -->
            <div 
              v-for="item in items" 
              :key="item.id" 
              class="bg-white dark:bg-background-dark/50 rounded-lg p-4 flex items-stretch justify-between gap-4 shadow-sm"
            >
              <div class="flex flex-[2_2_0px] flex-col gap-2">
                <p class="text-text-light dark:text-text-dark text-base font-bold leading-tight">{{ item.name }}</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm font-normal leading-normal">{{ item.description }}</p>
                
                <!-- Tags -->
                <div class="flex items-center gap-2 mt-1">
                  <span v-if="item.tags.includes('vegetarian')" class="material-symbols-outlined text-green-600" title="Vegetarian">eco</span>
                  <span v-if="item.tags.includes('vegan')" class="rounded-full bg-green-200 text-green-800 text-xs px-2 py-1 font-bold">V</span>
                  <span v-if="item.tags.includes('gluten-free')" class="rounded-full bg-blue-200 text-blue-800 text-xs px-2 py-1 font-bold">GF</span>
                </div>
                
                <p class="text-text-light dark:text-text-dark font-bold mt-2">${{ item.price.toFixed(2) }}</p>
              </div>
              <div 
                class="w-24 h-24 bg-center bg-no-repeat aspect-square bg-cover rounded-lg flex-shrink-0" 
                :style="{ 'background-image': `url(${item.image})` }"
              ></div>
            </div>
          </div>
        </div>
      </div>
    </main>
    
    <Footer />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import { fetchMenu } from '@/services/api'

const isLoadingMenu = ref(true)
const menu = ref(null)
const activeMenuFilter = ref('all')
const activeMenuCategory = ref('appetizers')

const menuFilters = [
  { name: 'All', value: 'all' },
  { name: 'Vegetarian', value: 'vegetarian' },
  { name: 'Vegan', value: 'vegan' },
  { name: 'Gluten-Free', value: 'gluten-free' }
]

const filteredMenu = computed(() => {
  if (!menu.value) return {}
  if (activeMenuFilter.value === 'all') {
    return menu.value
  }
  const filtered = {}
  for (const category in menu.value) {
    const items = menu.value[category].filter(item =>
      item.tags.includes(activeMenuFilter.value)
    )
    if (items.length > 0) {
      filtered[category] = items
    }
  }
  return filtered
})

const loadMenu = async () => {
  isLoadingMenu.value = true
  try {
    // Call API service
    const data = await fetchMenu()
    console.log('🍽️ Menu data loaded:', data)
    console.log('🍽️ Menu categories:', Object.keys(data))
    console.log('🍽️ Active filter:', activeMenuFilter.value)
    menu.value = data
  } catch (error) {
    console.error('Failed to load menu:', error)
  } finally {
    isLoadingMenu.value = false
  }
}

onMounted(() => {
  loadMenu()
})
</script>


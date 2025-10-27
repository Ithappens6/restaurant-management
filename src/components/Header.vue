<template>
  <header class="sticky top-0 z-20 bg-background-light dark:bg-background-dark shadow-sm flex items-center p-4 pb-2 justify-between">
    <button 
      @click="$router.push('/')" 
      class="text-text-light dark:text-text-dark flex size-12 shrink-0 items-center justify-start hover:text-primary transition-colors"
    >
      <span class="material-symbols-outlined">arrow_back</span>
    </button>
    <h1 class="text-text-light dark:text-text-dark text-xl font-bold leading-tight tracking-[-0.015em] flex-1 text-center">
      {{ title }}
    </h1>
    <div class="w-12 shrink-0"></div>
  </header>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  }
})
</script>


<template>
  <router-view />
  <ChatWidget />
</template>

<script setup>
import ChatWidget from '@/components/ChatWidget.vue'
// Main app component with global chat widget
// Routing is handled by vue-router
</script>

<style>
/* Global styles are imported in main.js */
</style>
<template>
  <div class="relative flex flex-col w-full">
    <!-- Hero Section (Full Screen) -->
    <section class="relative flex h-screen w-full flex-col">
      <!-- Header for Home Page -->
      <header class="absolute top-0 left-0 right-0 z-50 bg-transparent pointer-events-none">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          <nav class="flex items-center justify-center py-4 sm:py-6 pointer-events-auto">
            <!-- Navigation Buttons (All Screen Sizes) -->
            <div class="flex items-center space-x-3 sm:space-x-6 pointer-events-auto bg-black/30 backdrop-blur-md rounded-full px-4 sm:px-8 py-2 sm:py-3">
              <button 
                @click="scrollToSection('about')" 
                class="text-white hover:text-primary transition-colors px-2 sm:px-4 py-2 cursor-pointer font-medium text-sm sm:text-base"
              >
                About
              </button>
              <button 
                @click="scrollToSection('hours')" 
                class="text-white hover:text-primary transition-colors px-2 sm:px-4 py-2 cursor-pointer font-medium text-sm sm:text-base"
              >
                Hours
              </button>
              <button 
                @click="scrollToSection('contact')" 
                class="text-white hover:text-primary transition-colors px-2 sm:px-4 py-2 cursor-pointer font-medium text-sm sm:text-base"
              >
                Contact
              </button>
            </div>
          </nav>
        </div>
      </header>
      
      <!-- Hero Content -->
      <div class="flex-grow" id="hero">
        <div class="relative h-full">
          <div 
            class="absolute inset-0 bg-cover bg-center" 
            style='background-image: linear-gradient(rgba(0, 0, 0, 0.4) 0%, rgba(0, 0, 0, 0.6) 100%), url("https://lh3.googleusercontent.com/aida-public/AB6AXuAdsrlIdyBHH5LqfXHXGtHqm24viU0ioFujJ-RZmf4jTEnhjXFdVQ188aA9Ysf1_VLFewh-MYNRETUoHOWv8CunSTc1SeQm9ixrfVn-sqaefWY07I4V4-DsF1IkPvd5TY_8fnB70rlrjI8HeZLR7iIXC0RuYgaNO4W7ve8qWnogeaOmfQugYglmBzII7o-UmYhrmjm-vUywo46hyoO8dBPsM6YcWydBw-xk1-UYuIkiC20HfBIn3atDrxZwv9D_6WkN-Evevdc1_x2F");'
          ></div>
          <div class="relative z-10 flex h-full flex-col items-center justify-center text-center text-white p-4">
            <div class="flex flex-col gap-4">
              <h1 class="text-5xl font-black leading-tight tracking-[-0.033em] md:text-7xl">Kurdie's Curry</h1>
              <h2 class="text-lg font-normal leading-normal md:text-xl">Authentic Flavors, Modern Twist</h2>
            </div>
            <div class="mt-8 flex flex-col sm:flex-row gap-4">
              <button 
                @click="scrollToSection('specialty-menu')"
                class="flex min-w-[180px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-6 bg-primary text-white text-base font-bold leading-normal tracking-[0.015em] hover:bg-primary/90 transition-colors"
              >
                <span class="truncate">View Menu</span>
              </button>
              <router-link 
                to="/reservations" 
                class="flex min-w-[180px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-6 bg-background-light text-gray-800 text-base font-bold leading-normal tracking-[0.015em] hover:bg-background-light/90 transition-colors"
              >
                <span class="truncate">Make a Reservation</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="min-h-screen bg-background-light dark:bg-background-dark py-16">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="@container mb-8">
          <div class="@[480px]:px-4 @[480px]:py-3">
            <div 
              class="w-full bg-center bg-no-repeat bg-cover flex flex-col justify-end overflow-hidden bg-white @[480px]:rounded-lg min-h-80" 
              style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCDOe9z56owu9TgP3lHYSF-quDFp7o1Zd2_0sAryJYPR7_xbr0CBuMWgEzWQNol7naaoJheGOa8guWKuIRTD1x8ToyHcOtPtq07U7ZpjK_cDPVFyYUZepPVJfliJUQuZBRRvotnIgpWf9_iBzOg9I-GwAF92jUlrqXjyG-EAqltnik5ZooA4PFVMvvWv7XlSwy9hS-rF1hu7GeOb4kuGn_zS6yTZpFyb_16hqmZBlUrlbiyRqSgz_R7tyX5qcXkN0tSqXw-rG9Uw3Hn");'
            ></div>
          </div>
        </div>
        
        <h1 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight text-center pb-3 pt-6">
          Our Story: A Fusion of Flavors and Family
        </h1>
        <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal pb-3 pt-1 max-w-3xl mx-auto text-center">
          Kurdie's Curry is a culinary journey that blends the vibrant spices of India with the rich, comforting flavors of Kurdistan. Our story began with a dream to share the unique dishes from our two cultures, creating a dining experience that is both familiar and excitingly new.
        </p>
        
        <div class="py-6 max-w-3xl mx-auto">
          <div class="border-l-4 border-primary pl-4">
            <p class="text-text-light dark:text-text-dark text-xl italic font-semibold leading-relaxed">
              "Food is our common ground, a universal experience that connects us all."
            </p>
          </div>
        </div>
        
        <h2 class="text-text-light dark:text-text-dark text-2xl font-bold pt-6 pb-2 max-w-3xl mx-auto">Our Cuisine Philosophy</h2>
        <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal pb-3 pt-1 max-w-3xl mx-auto">
          We believe in the power of food to tell stories. Our menu is a carefully crafted tapestry of Indian and Kurdish culinary traditions. We use time-honored recipes, passed down through generations, and infuse them with a modern twist. Expect the bold spices of India to dance with the hearty, soulful flavors of Kurdish home cooking.
        </p>
        
        <div class="pt-8 pb-4 max-w-3xl mx-auto">
          <div class="flex flex-col items-center gap-4 md:flex-row md:items-start">
            <div class="flex-shrink-0">
              <img 
                alt="Portrait of Amrita Patel, the owner of Kurdie's Curry." 
                class="w-32 h-32 rounded-full object-cover" 
                src="https://lh3.googleusercontent.com/aida-public/AB6AXuD3S1Eprs9v5t8UMmOSbQVdTWHWhjDOOgK_Rz75Cn5q40FG5J77NF78AaxIyidfYmjeA1thI8CZx3_2sS7Xg0j8jr4jCrUowfaPC-hvtdBME_NfFzIiCUngQLlpHEOMXIv7tGt3k9wdA3M-eIZhggOzL09Ip5W1TcvDyBiQhaCmmVEG28a0ghuHdTl5e18lYX6Tvf4Ri2FY3ZP_JbQEBJmlVBIHf0f9SKioYXDfjVNBFGq84_lGJvSFWH0COtnKoEtDmVVocEsitaOX" 
              />
            </div>
            <div class="text-center md:text-left">
              <h3 class="text-text-light dark:text-text-dark text-xl font-bold">Meet Amrita Patel</h3>
              <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal mt-2">
                Amrita's passion for food is rooted in her dual heritage. Growing up in a family that celebrated both Indian and Kurdish traditions, her kitchen was always a place of discovery. With Kurdie's Curry, she brings her family's legacy to your table, sharing the love and flavors that shaped her life.
              </p>
            </div>
          </div>
        </div>

        <!-- Scroll Down Indicator -->
        <div class="flex justify-center mt-12">
          <a href="#specialty-menu" class="flex flex-col items-center text-text-light dark:text-text-dark hover:text-primary transition-colors">
            <span class="text-sm mb-2">Our Menu</span>
            <span class="material-symbols-outlined text-4xl animate-bounce">expand_more</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Specialty Menu Section -->
    <section id="specialty-menu" class="bg-white dark:bg-gray-900 py-16">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-text-light dark:text-text-dark text-center mb-2">Our Signature Dishes</h2>
        <p class="text-center text-gray-600 dark:text-gray-400 mb-8">Handcrafted specialties that define our cuisine</p>
        
        <!-- Loading State -->
        <div v-if="isLoadingSignatureDishes" class="text-center py-8">
          <p class="text-gray-600 dark:text-gray-400">Loading our specialties...</p>
        </div>
        
        <!-- Error State -->
        <div v-else-if="signatureDishesError" class="text-center py-8">
          <p class="text-red-600">Failed to load signature dishes</p>
        </div>
        
        <!-- Horizontal Scroll Container -->
        <div v-else-if="signatureDishes.length > 0" class="relative">
          <div 
            ref="scrollContainer"
            @mouseenter="pauseAutoScroll"
            @mouseleave="resumeAutoScroll"
            @touchstart="pauseAutoScroll"
            @scroll="handleManualScroll"
            class="flex gap-6 overflow-x-auto pb-4 snap-x snap-mandatory scrollbar-hide scroll-smooth"
          >
            <div 
              v-for="dish in signatureDishes" 
              :key="dish.id"
              class="flex-shrink-0 snap-start w-80"
            >
              <div class="bg-white dark:bg-gray-800 rounded-lg shadow-md hover:shadow-xl transition-shadow overflow-hidden group">
                <div 
                  class="w-full h-56 bg-center bg-cover"
                  :style="{ 'background-image': `url(${dish.image})` }"
                ></div>
                <div class="p-4">
                  <h3 class="text-lg font-bold text-text-light dark:text-text-dark mb-2">
                    {{ dish.name }}
                  </h3>
                  <p class="text-sm text-gray-600 dark:text-gray-400 mb-3 line-clamp-2">
                    {{ dish.description }}
                  </p>
                  <p class="text-xl font-bold text-primary">
                    ${{ dish.price.toFixed(2) }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Empty State -->
        <div v-else class="text-center py-8">
          <p class="text-gray-600 dark:text-gray-400">No signature dishes available</p>
        </div>
        
        <!-- View Full Menu Button -->
        <div class="text-center mt-8">
          <router-link 
            to="/menu" 
            class="inline-flex items-center justify-center px-6 py-3 bg-primary text-white font-semibold rounded-lg hover:bg-primary/90 transition-colors"
          >
            View Full Menu
          </router-link>
        </div>
        
        <!-- Scroll Down to Contact -->
        <div class="flex justify-center mt-12">
          <a href="#contact" class="flex flex-col items-center text-text-light dark:text-text-dark hover:text-primary transition-colors">
            <span class="text-sm mb-2">Contact Us</span>
            <span class="material-symbols-outlined text-4xl animate-bounce">expand_more</span>
          </a>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="min-h-screen bg-white dark:bg-gray-900 py-16">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 max-w-4xl">
        <div class="mb-8">
          <div 
            class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-lg object-cover" 
            style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCrROru0aRXYnIm3p9IU3stLaaN0yOq5HAIdqYM3YexaISzKSski96679FFYL_uzHQl9oJofuQY988V0Efp7p_p2hla3Zm2w49jYdRKJ5HOgk5lIAGrE6F0olT-ETey73E8ZGKhIN8GCDuDRYU5bIP_HTtYPQnTZyoJ0vJRI2LOD1-pQtg8RW9YVnARyAUCKu2-6wWaylK8I_8ux5D09TJk-NJTjPc3gUgxj8-C8RjOvxRNVFh7BrEYMyzzcdX_rrXmW7g1v7JaB5uN");'
          ></div>
        </div>
        
        <h2 class="text-3xl font-bold text-text-light dark:text-text-dark text-center mb-8">Get In Touch</h2>
        
        <div class="grid md:grid-cols-2 gap-8 mb-12">
          <!-- Location Info -->
          <div id="hours" class="space-y-4">
            <h3 class="text-lg font-bold leading-tight tracking-[-0.015em] text-text-light dark:text-text-dark mb-4">
              Our Location & Hours
            </h3>
            
            <div class="flex items-start gap-4">
              <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10">
                <span class="material-symbols-outlined">location_on</span>
              </div>
              <div>
                <p class="text-base font-normal leading-normal text-text-light dark:text-text-dark">
                  1337 N Spice Rd<br>Prescott Valley, AZ 86314
                </p>
                <a 
                  href="https://www.google.com/maps/search/?api=1&query=1337+N+Spice+Rd+Prescott+Valley+AZ+86314" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  class="text-base font-medium leading-normal text-primary hover:underline mt-1 inline-block"
                >
                  Get directions
                </a>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10">
                <span class="material-symbols-outlined">call</span>
              </div>
              <div>
                <p class="text-base font-normal leading-normal text-text-light dark:text-text-dark">
                  (928) 555-1337
                </p>
                <a 
                  href="tel:+19285551337" 
                  class="text-base font-medium leading-normal text-primary hover:underline mt-1 inline-block"
                >
                  Call
                </a>
              </div>
            </div>
            
            <div class="flex items-start gap-4">
              <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10">
                <span class="material-symbols-outlined">schedule</span>
              </div>
              <div class="text-base font-normal leading-normal text-text-light dark:text-text-dark">
                <p>Mon-Thu: 11am-9pm</p>
                <p>Fri-Sat: 11am-10pm</p>
                <p>Sun: CLOSED</p>
              </div>
            </div>
          </div>
          
          <!-- Contact Form -->
          <div>
            <h3 class="text-lg font-bold leading-tight tracking-[-0.015em] pb-4 text-text-light dark:text-text-dark">
              Send Us a Message
            </h3>
            <form @submit.prevent="handleSubmit" class="space-y-4">
              <div>
                <input 
                  v-model="form.name"
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
                  placeholder="Name" 
                  type="text" 
                  required 
                />
              </div>
              <div>
                <input 
                  v-model="form.email"
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
                  placeholder="Email" 
                  type="email" 
                  required 
                />
              </div>
              <div>
                <input 
                  v-model="form.subject"
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
                  placeholder="Subject" 
                  type="text" 
                />
              </div>
              <div>
                <textarea 
                  v-model="form.message"
                  class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
                  placeholder="Message" 
                  rows="4" 
                  required
                ></textarea>
              </div>
              <div>
                <button 
                  class="w-full bg-primary text-white font-bold py-3 px-4 rounded-lg hover:bg-opacity-90 transition-colors" 
                  type="submit"
                  :disabled="isSubmitting"
                >
                  {{ isSubmitting ? 'Sending...' : 'Send Message' }}
                </button>
              </div>
              
              <div 
                v-if="status" 
                :class="status.success ? 'bg-green-100 border-green-400 text-green-700' : 'bg-red-100 border-red-400 text-red-700'"
                class="border px-4 py-3 rounded relative" 
                role="alert"
              >
                <span class="block sm:inline">{{ status.message }}</span>
              </div>
            </form>
          </div>
        </div>

        <!-- Back to Top -->
        <div class="flex justify-center mt-12">
          <a href="#hero" class="flex flex-col items-center text-text-light dark:text-text-dark hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-4xl rotate-180">expand_more</span>
            <span class="text-sm mt-2">Back to top</span>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { submitContactForm, fetchSignatureDishes } from '@/services/api'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const status = ref(null)
const isSubmitting = ref(false)

// Signature dishes state
const signatureDishes = ref([])
const isLoadingSignatureDishes = ref(false)
const signatureDishesError = ref(false)

// Auto-scroll state
const scrollContainer = ref(null)
let autoScrollInterval = null
let isAutoScrollPaused = false
let manualScrollTimeout = null

// Load signature dishes
const loadSignatureDishes = async () => {
  isLoadingSignatureDishes.value = true
  signatureDishesError.value = false
  
  try {
    const dishes = await fetchSignatureDishes()
    signatureDishes.value = dishes
    console.log('✨ Signature dishes loaded:', dishes)
  } catch (error) {
    console.error('Failed to load signature dishes:', error)
    signatureDishesError.value = true
  } finally {
    isLoadingSignatureDishes.value = false
  }
}

// Smooth scroll to section
const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  }
}

const handleSubmit = async () => {
  status.value = null
  isSubmitting.value = true
  
  try {
    const result = await submitContactForm(form.value)
    status.value = { success: true, message: result.message }
    
    form.value = {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
    
    setTimeout(() => {
      status.value = null
    }, 4000)
  } catch (error) {
    status.value = { success: false, message: error.message || 'Failed to send message.' }
  } finally {
    isSubmitting.value = false
  }
}

// Auto-scroll functions
const startAutoScroll = () => {
  if (!scrollContainer.value || signatureDishes.value.length <= 1) return
  
  autoScrollInterval = setInterval(() => {
    if (isAutoScrollPaused) return
    
    const container = scrollContainer.value
    const cardWidth = 320 + 24 // 80*4 (w-80) + 24 (gap-6)
    const maxScroll = container.scrollWidth - container.clientWidth
    
    // If at the end, loop back to start
    if (container.scrollLeft >= maxScroll - 10) {
      container.scrollLeft = 0
    } else {
      // Scroll to next item
      container.scrollLeft += cardWidth
    }
  }, 2000) // Scroll every 2 seconds
}

const stopAutoScroll = () => {
  if (autoScrollInterval) {
    clearInterval(autoScrollInterval)
    autoScrollInterval = null
  }
}

const pauseAutoScroll = () => {
  isAutoScrollPaused = true
}

const resumeAutoScroll = () => {
  isAutoScrollPaused = false
}

const handleManualScroll = () => {
  // Pause auto-scroll when user manually scrolls
  isAutoScrollPaused = true
  
  // Clear existing timeout
  if (manualScrollTimeout) {
    clearTimeout(manualScrollTimeout)
  }
  
  // Resume auto-scroll after 3 seconds of no manual interaction
  manualScrollTimeout = setTimeout(() => {
    isAutoScrollPaused = false
  }, 3000)
}

// Load signature dishes on mount
onMounted(() => {
  loadSignatureDishes()
  
  // Start auto-scroll after dishes are loaded
  setTimeout(() => {
    if (signatureDishes.value.length > 1) {
      startAutoScroll()
    }
  }, 1000)
})

// Cleanup on unmount
onUnmounted(() => {
  stopAutoScroll()
  if (manualScrollTimeout) {
    clearTimeout(manualScrollTimeout)
  }
})
</script>

<style scoped>
/* Hide scrollbar for Chrome, Safari and Opera */
.scrollbar-hide::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.scrollbar-hide {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>

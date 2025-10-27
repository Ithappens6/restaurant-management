<template>
  <div class="relative flex flex-col w-full">
    <!-- Hero Section (Full Screen) -->
    <section class="relative flex h-screen w-full flex-col">
      <!-- Desktop Header for Home Page -->
      <header class="absolute top-0 left-0 right-0 z-50 bg-transparent pointer-events-none">
        <div class="container mx-auto px-4 sm:px-6 lg:px-8">
          <nav class="flex items-center justify-between py-6 pointer-events-auto">
            <!-- Logo with Status -->
            <div class="flex flex-col pointer-events-auto">
              <div class="text-2xl font-bold text-white">Kurdie's Curry</div>
              <!-- Restaurant Status Indicator -->
              <div class="flex items-center gap-2 mt-1">
                <div class="flex items-center gap-1.5">
                  <span 
                    class="w-2 h-2 rounded-full animate-pulse"
                    :class="restaurantStatus.isOpen ? 'bg-green-500' : 'bg-red-500'"
                  ></span>
                  <span 
                    class="text-xs font-semibold uppercase tracking-wide"
                    :class="restaurantStatus.isOpen ? 'text-green-400' : 'text-red-400'"
                  >
                    {{ restaurantStatus.isOpen ? 'Open' : 'Closed' }}
                  </span>
                </div>
                <span class="text-xs text-white/80">{{ restaurantStatus.message }}</span>
              </div>
            </div>
            
            <!-- Desktop Menu -->
            <div class="hidden md:flex items-center space-x-8 pointer-events-auto">
              <a href="#about" class="text-white hover:text-primary transition-colors px-3 py-2 cursor-pointer font-medium pointer-events-auto">About</a>
              <a href="#contact" class="text-white hover:text-primary transition-colors px-3 py-2 cursor-pointer font-medium pointer-events-auto">Contact</a>
            </div>
            
            <!-- Mobile Menu Button -->
            <button 
              @click="showMobileMenu = !showMobileMenu" 
              class="md:hidden text-white cursor-pointer pointer-events-auto z-50 relative"
            >
              <span class="material-symbols-outlined">{{ showMobileMenu ? 'close' : 'menu' }}</span>
            </button>
          </nav>
          
          <!-- Mobile Menu Dropdown -->
          <div 
            v-if="showMobileMenu"
            class="md:hidden absolute top-full left-0 right-0 bg-gray-900/95 backdrop-blur-sm pointer-events-auto"
          >
            <div class="flex flex-col py-4 px-4 space-y-2">
              <a 
                href="#about" 
                @click="showMobileMenu = false"
                class="text-white hover:text-primary transition-colors px-4 py-3 cursor-pointer font-medium rounded-lg hover:bg-white/10"
              >
                About
              </a>
              <a 
                href="#contact" 
                @click="showMobileMenu = false"
                class="text-white hover:text-primary transition-colors px-4 py-3 cursor-pointer font-medium rounded-lg hover:bg-white/10"
              >
                Contact
              </a>
            </div>
          </div>
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
              <router-link 
                to="/menu" 
                class="flex min-w-[180px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-12 px-6 bg-primary text-white text-base font-bold leading-normal tracking-[0.015em] hover:bg-primary/90 transition-colors"
              >
                <span class="truncate">View Menu</span>
              </router-link>
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
          <div class="space-y-4">
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
                <button class="text-base font-medium leading-normal text-primary hover:underline mt-1">Get directions</button>
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
                <button class="text-base font-medium leading-normal text-primary hover:underline mt-1">Call</button>
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
import { submitContactForm, getRestaurantStatus } from '@/services/api'

const showMobileMenu = ref(false)
const restaurantStatus = ref({
  isOpen: true,
  message: 'Loading...'
})

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const status = ref(null)
const isSubmitting = ref(false)

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

// Fetch restaurant status on mount
const fetchStatus = async () => {
  try {
    console.log('Fetching restaurant status...')
    const statusData = await getRestaurantStatus()
    restaurantStatus.value = statusData
    console.log('Restaurant status updated:', statusData)
  } catch (error) {
    console.error('Failed to fetch restaurant status:', error)
    // Default to open if API fails
    restaurantStatus.value = {
      isOpen: true,
      message: 'Call us for hours'
    }
  }
}

onMounted(() => {
  fetchStatus()
  // Update status every 5 minutes (300000ms)
  const intervalId = setInterval(fetchStatus, 5 * 60 * 1000)
  
  // Clean up interval on unmount
  onUnmounted(() => {
    clearInterval(intervalId)
  })
})
</script>

<style scoped>
/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}
</style>

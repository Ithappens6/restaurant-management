<template>
  <div class="flex flex-col min-h-screen">
    <Header title="Contact Us" />
    
    <main class="flex-grow pb-20">
      <div class="flex px-4 py-3">
        <div 
          class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-lg object-cover" 
          style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCrROru0aRXYnIm3p9IU3stLaaN0yOq5HAIdqYM3YexaISzKSski96679FFYL_uzHQl9oJofuQY988V0Efp7p_p2hla3Zm2w49jYdRKJ5HOgk5lIAGrE6F0olT-ETey73E8ZGKhIN8GCDuDRYU5bIP_HTtYPQnTZyoJ0vJRI2LOD1-pQtg8RW9YVnARyAUCKu2-6wWaylK8I_8ux5D09TJk-NJTjPc3gUgxj8-C8RjOvxRNVFh7BrEYMyzzcdX_rrXmW7g1v7JaB5uN");'
        ></div>
      </div>
      
      <h3 class="text-lg font-bold leading-tight tracking-[-0.015em] px-4 pb-2 pt-4 text-text-light dark:text-text-dark">
        Our Location & Hours
      </h3>
      
      <div class="flex items-center gap-4 bg-background-light dark:bg-background-dark px-4 min-h-14 justify-between">
        <div class="flex items-center gap-4">
          <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10">
            <span class="material-symbols-outlined">location_on</span>
          </div>
          <p class="text-base font-normal leading-normal flex-1 truncate text-text-light dark:text-text-dark">
            1337 N Spice Rd, Prescott Valley, AZ 86314
          </p>
        </div>
        <div class="shrink-0">
          <button class="text-base font-medium leading-normal text-primary hover:underline">Get directions</button>
        </div>
      </div>
      
      <div class="flex items-center gap-4 bg-background-light dark:bg-background-dark px-4 min-h-14 justify-between">
        <div class="flex items-center gap-4">
          <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10">
            <span class="material-symbols-outlined">call</span>
          </div>
          <p class="text-base font-normal leading-normal flex-1 truncate text-text-light dark:text-text-dark">
            (928) 555-1337
          </p>
        </div>
        <div class="shrink-0">
          <button class="text-base font-medium leading-normal text-primary hover:underline">Call</button>
        </div>
      </div>
      
      <div class="flex items-start gap-4 bg-background-light dark:bg-background-dark px-4 min-h-14 justify-between">
        <div class="flex items-start gap-4">
          <div class="text-text-light dark:text-text-dark flex items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-700/50 shrink-0 size-10 mt-1">
            <span class="material-symbols-outlined">schedule</span>
          </div>
          <div class="text-base font-normal leading-normal flex-1 text-text-light dark:text-text-dark">
            <p>Mon-Thu: 11am-9pm</p>
            <p>Fri-Sat: 11am-10pm</p>
            <p>Sun: CLOSED</p>
          </div>
        </div>
      </div>
      
      <div class="px-4 py-6 bg-background-light dark:bg-background-dark">
        <h3 class="text-lg font-bold leading-tight tracking-[-0.015em] pb-4 text-text-light dark:text-text-dark">
          Send Us a Message
        </h3>
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <div>
            <label class="sr-only" for="name">Name</label>
            <input 
              v-model="form.name"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
              id="name" 
              name="name" 
              placeholder="Name" 
              type="text" 
              required 
            />
          </div>
          <div>
            <label class="sr-only" for="email">Email</label>
            <input 
              v-model="form.email"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
              id="email" 
              name="email" 
              placeholder="Email" 
              type="email" 
              required 
            />
          </div>
          <div>
            <label class="sr-only" for="subject">Subject</label>
            <input 
              v-model="form.subject"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
              id="subject" 
              name="subject" 
              placeholder="Subject" 
              type="text" 
            />
          </div>
          <div>
            <label class="sr-only" for="message">Message</label>
            <textarea 
              v-model="form.message"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-text-light dark:text-text-dark focus:outline-none focus:ring-2 focus:ring-primary" 
              id="message" 
              name="message" 
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
    </main>
    
    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import { submitContactForm } from '@/services/api'

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
    console.log('Submitting contact form:', form.value)
    
    // Call API service
    const result = await submitContactForm(form.value)
    status.value = { success: true, message: result.message }
    console.log('Contact form submitted successfully!')
    
    // Reset form on success
    form.value = {
      name: '',
      email: '',
      subject: '',
      message: ''
    }
    
    // Hide message after 4 seconds
    setTimeout(() => {
      status.value = null
    }, 4000)
  } catch (error) {
    status.value = { success: false, message: error.message || 'Failed to send message.' }
    console.error('Contact form failed:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>


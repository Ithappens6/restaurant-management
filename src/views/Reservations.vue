<template>
  <div class="flex flex-col min-h-screen">
    <Header title="Book Your Table" />
    
    <main class="flex-grow pb-20">
      <div class="p-4" style="background-color: #FDF5E6;">
        <h1 class="tracking-light text-[32px] font-bold leading-tight text-left pb-3 pt-6 form-label-reservations">
          Book Your Table
        </h1>
        <p class="text-base font-normal leading-normal pb-3 pt-1 text-text-light">
          For parties of 4 or more, we recommend making a reservation in advance. Friday and Saturday evenings are our busiest times, so be sure to book ahead!
        </p>
        
        <form @submit.prevent="handleSubmit" class="flex flex-col gap-4 py-3">
          <label class="flex flex-col w-full">
            <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Full Name</p>
            <input 
              v-model="form.name" 
              class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 placeholder:text-gray-400 p-[15px] text-base font-normal leading-normal form-input-reservations" 
              placeholder="Enter your full name" 
              required 
            />
          </label>
          
          <label class="flex flex-col w-full">
            <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Phone Number</p>
            <input 
              v-model="form.phone" 
              class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 placeholder:text-gray-400 p-[15px] text-base font-normal leading-normal form-input-reservations" 
              placeholder="Enter your phone number" 
              required 
            />
          </label>
          
          <label class="flex flex-col w-full">
            <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Email Address</p>
            <input 
              v-model="form.email" 
              class="form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 placeholder:text-gray-400 p-[15px] text-base font-normal leading-normal form-input-reservations" 
              placeholder="Enter your email address" 
              type="email" 
            />
          </label>
          
          <div class="grid grid-cols-2 gap-4">
            <label class="flex flex-col w-full">
              <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Party Size</p>
              <div class="relative">
                <select 
                  v-model="form.partySize" 
                  class="form-select appearance-none w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 p-[15px] text-base font-normal leading-normal form-input-reservations" 
                  required
                >
                  <option>1 person</option>
                  <option>2 people</option>
                  <option>3 people</option>
                  <option>4 people</option>
                  <option>5 people</option>
                  <option>6 people</option>
                  <option>7 people</option>
                  <option>8+ people</option>
                </select>
                <span class="material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-gray-400">expand_more</span>
              </div>
            </label>
            
            <label class="flex flex-col w-full">
              <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Date</p>
              <div class="relative">
                <input 
                  v-model="form.date" 
                  class="form-input w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 p-[15px] text-base font-normal leading-normal placeholder:text-gray-400 form-input-reservations" 
                  type="date" 
                  required 
                />
              </div>
            </label>
          </div>
          
          <label class="flex flex-col w-full">
            <p class="text-base font-medium leading-normal pb-2 form-label-reservations">Time</p>
            <div class="relative">
              <select 
                v-model="form.time" 
                class="form-select appearance-none w-full min-w-0 flex-1 resize-none overflow-hidden rounded-lg focus:outline-0 focus:ring-0 h-14 p-[15px] text-base font-normal leading-normal form-input-reservations" 
                required
              >
                <option>5:00 PM</option>
                <option>5:30 PM</option>
                <option>6:00 PM</option>
                <option>6:30 PM</option>
                <option>7:00 PM</option>
                <option>7:30 PM</option>
                <option>8:00 PM</option>
                <option>8:30 PM</option>
                <option>9:00 PM</option>
              </select>
              <span class="material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-gray-400">expand_more</span>
            </div>
          </label>
          
          <div class="pt-6">
            <button 
              class="w-full h-14 font-bold rounded-lg text-lg btn-reservations hover:opacity-90 transition-opacity" 
              type="submit"
              :disabled="isSubmitting"
            >
              {{ isSubmitting ? 'Submitting...' : 'Confirm Reservation' }}
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
import { submitReservation } from '@/services/api'

const form = ref({
  name: '',
  phone: '',
  email: '',
  partySize: '2 people',
  date: '',
  time: '5:00 PM'
})

const status = ref(null)
const isSubmitting = ref(false)

const handleSubmit = async () => {
  status.value = null
  isSubmitting.value = true
  
  try {
    // Parse party size (extract number from "X people" format)
    const partySizeMatch = form.value.partySize.match(/\d+/)
    const partySizeNumber = partySizeMatch ? parseInt(partySizeMatch[0]) : 2
    
    // Convert time from "5:00 PM" to "17:00" format (24-hour)
    const timeParts = form.value.time.match(/(\d+):(\d+)\s*(AM|PM)/)
    let hour = parseInt(timeParts[1])
    const minute = timeParts[2]
    const period = timeParts[3]
    
    if (period === 'PM' && hour !== 12) hour += 12
    if (period === 'AM' && hour === 12) hour = 0
    
    const time24 = `${hour.toString().padStart(2, '0')}:${minute}`
    
    // Format the form data for API
    const reservationData = {
      ...form.value,
      partySize: partySizeNumber,
      time: time24
    }
    
    console.log('Submitting reservation:', reservationData)
    
    // Call API service
    const result = await submitReservation(reservationData)
    status.value = { success: true, message: result.message }
    console.log('Reservation successful! ID:', result.reservationId)
    
    // Reset form on success
    form.value = {
      name: '',
      phone: '',
      email: '',
      partySize: '2 people',
      date: '',
      time: '5:00 PM'
    }
    
    // Hide message after 4 seconds
    setTimeout(() => {
      status.value = null
    }, 4000)
  } catch (error) {
    status.value = { success: false, message: error.message || 'Failed to book reservation.' }
    console.error('Reservation failed:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script>


<template>
  <div class="flex flex-col min-h-screen">
    <Header title="About Us" />
    
    <main class="flex-grow pb-20">
      <div class="@container">
        <div class="@[480px]:px-4 @[480px]:py-3">
          <div 
            class="w-full bg-center bg-no-repeat bg-cover flex flex-col justify-end overflow-hidden bg-white @[480px]:rounded-lg min-h-80" 
            style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCDOe9z56owu9TgP3lHYSF-quDFp7o1Zd2_0sAryJYPR7_xbr0CBuMWgEzWQNol7naaoJheGOa8guWKuIRTD1x8ToyHcOtPtq07U7ZpjK_cDPVFyYUZepPVJfliJUQuZBRRvotnIgpWf9_iBzOg9I-GwAF92jUlrqXjyG-EAqltnik5ZooA4PFVMvvWv7XlSwy9hS-rF1hu7GeOb4kuGn_zS6yTZpFyb_16hqmZBlUrlbiyRqSgz_R7tyX5qcXkN0tSqXw-rG9Uw3Hn");'
          ></div>
        </div>
      </div>
      
      <h1 class="text-text-light dark:text-text-dark tracking-light text-[32px] font-bold leading-tight px-4 text-center pb-3 pt-6">
        Our Story: A Fusion of Flavors and Family
      </h1>
      <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal pb-3 pt-1 px-4">
        Kurdie's Curry is a culinary journey that blends the vibrant spices of India with the rich, comforting flavors of Kurdistan. Our story began with a dream to share the unique dishes from our two cultures, creating a dining experience that is both familiar and excitingly new.
      </p>
      
      <div class="px-4 py-6">
        <div class="border-l-4 border-primary pl-4">
          <p class="text-text-light dark:text-text-dark text-xl italic font-semibold leading-relaxed">
            "Food is our common ground, a universal experience that connects us all."
          </p>
        </div>
      </div>
      
      <h2 class="text-text-light dark:text-text-dark text-2xl font-bold px-4 pt-6 pb-2">Our Cuisine Philosophy</h2>
      <p class="text-text-light dark:text-text-dark text-base font-normal leading-normal pb-3 pt-1 px-4">
        We believe in the power of food to tell stories. Our menu is a carefully crafted tapestry of Indian and Kurdish culinary traditions. We use time-honored recipes, passed down through generations, and infuse them with a modern twist. Expect the bold spices of India to dance with the hearty, soulful flavors of Kurdish home cooking.
      </p>
      
      <div class="px-4 pt-8 pb-4">
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
    </main>
    
    <Footer />
  </div>
</template>

<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
</script>


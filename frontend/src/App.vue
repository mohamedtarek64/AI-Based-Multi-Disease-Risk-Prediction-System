<script setup lang="ts">
import { RouterView, useRouter, useRoute } from 'vue-router'
import { computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useToastStore } from '@/stores/toast'
import ToastContainer from '@/components/ToastContainer.vue'
import BrandLogo from '@/components/BrandLogo.vue'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()
const toast = useToastStore()

const isAuthPage = computed(() => ['login', 'register'].includes(route.name as string))

const navLinks = [
  { name: 'Dashboard', to: '/', iconPath: 'M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z' },
  { name: 'AI Hub', to: '/predict', iconPath: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4z' },
  { name: 'History', to: '/history', iconPath: 'M13 3c-4.97 0-9 4.03-9 9H1l3.89 3.89.07.14L9 12H6c0-3.87 3.13-7 7-7s7 3.13 7 7-3.13 7-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42C8.27 19.99 10.51 21 13 21c4.97 0 9-4.03 9-9s-4.03-9-9-9zm-1 5v5l4.28 2.54.72-1.21-3.5-2.08V8H12z' },
  { name: 'Profile', to: '/profile', iconPath: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 4c1.93 0 3.5 1.57 3.5 3.5S13.93 13 12 13s-3.5-1.57-3.5-3.5S10.07 6 12 6zm0 14c-2.03 0-4.43-.82-6.14-2.88C7.55 15.8 9.68 15 12 15s4.45.8 6.14 2.12C16.43 19.18 14.03 20 12 20z' }
]

const handleLogout = async () => {
  await auth.logout()
  toast.show('Session ended securely.', 'info')
  router.push('/login')
}
</script>

<template>
  <div class="antialiased text-gray-900 flex min-h-screen bg-[#F0F2F5] selection:bg-blue-100">
    <!-- Dynamic Mesh & SVG Background System -->
    <div class="fixed inset-0 pointer-events-none -z-20 overflow-hidden bg-[#F8FAFC]">
      <!-- Primary Mesh Orbs -->
      <div class="absolute top-[-15%] left-[-10%] w-[60%] h-[60%] bg-gradient-to-br from-blue-400/20 to-indigo-500/0 rounded-full blur-[120px] animate-pulse"></div>
      <div class="absolute bottom-[-10%] right-[-5%] w-[50%] h-[50%] bg-gradient-to-tl from-indigo-400/20 to-purple-500/0 rounded-full blur-[120px]"></div>
      <div class="absolute top-[20%] right-[10%] w-[30%] h-[30%] bg-blue-300/10 rounded-full blur-[100px] animate-bounce"></div>

      <!-- Advanced SVG Technical Pattern -->
      <svg class="absolute inset-0 w-full h-full opacity-[0.03]" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="technical-grid" width="60" height="60" patternUnits="userSpaceOnUse">
            <path d="M 60 0 L 0 0 0 60" fill="none" stroke="currentColor" stroke-width="0.5"/>
            <circle cx="0" cy="0" r="1.5" fill="currentColor"/>
          </pattern>
          <pattern id="diagonal-dots" width="20" height="20" patternUnits="userSpaceOnUse">
            <circle cx="2" cy="2" r="0.8" fill="currentColor"/>
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill="url(#technical-grid)" class="text-blue-600" />
        <rect width="100%" height="100%" fill="url(#diagonal-dots)" class="text-indigo-900" />
      </svg>

      <!-- Glassy Vignette -->
      <div class="absolute inset-0 bg-gradient-to-b from-transparent via-white/20 to-white/60"></div>
    </div>

    <!-- Premium Sidebar -->
    <aside 
      v-if="!isAuthPage"
      class="w-20 lg:w-72 bg-white/80 backdrop-blur-xl border-r border-gray-200 flex flex-col transition-all duration-300 shadow-2xl relative z-50"
    >
      <div class="p-8">
        <div class="flex items-center gap-4">
          <BrandLogo size="md" />
          <div class="hidden lg:block">
            <h2 class="font-black text-xl tracking-tighter text-gray-900 leading-none">AI CORE</h2>
            <p class="text-[9px] font-black text-blue-600 uppercase tracking-widest mt-1">Medical Intelligence</p>
          </div>
        </div>
      </div>
      
      <nav class="flex-1 px-4 space-y-2 mt-4">
        <router-link 
          v-for="link in navLinks" 
          :key="link.name" 
          :to="link.to" 
          class="flex items-center gap-4 p-4 rounded-2xl transition-all hover:bg-gray-100 group relative" 
          active-class="bg-blue-600 !text-white shadow-xl shadow-blue-200"
        >
          <svg class="w-6 h-6 transition-transform group-hover:scale-110" fill="currentColor" viewBox="0 0 24 24">
            <path :d="link.iconPath" />
          </svg>
          <span class="font-bold hidden lg:block">{{ link.name }}</span>
          <div v-if="route.path === link.to" class="absolute left-[-1rem] w-1.5 h-8 bg-blue-600 rounded-r-full hidden lg:block"></div>
        </router-link>
      </nav>

      <div class="p-6 mt-auto space-y-6">
        <div v-if="auth.user" class="bg-gray-50/50 backdrop-blur-sm p-4 rounded-[2rem] flex items-center gap-4 border border-gray-100 lg:w-full w-fit mx-auto lg:mx-0">
          <div class="w-10 h-10 rounded-full bg-gradient-to-br from-blue-100 to-indigo-100 flex items-center justify-center text-blue-600 font-black shadow-inner">
            {{ auth.user.name.charAt(0) }}
          </div>
          <div class="overflow-hidden hidden lg:block">
            <p class="text-sm font-black text-gray-900 truncate">{{ auth.user.name }}</p>
            <p class="text-[10px] font-bold text-gray-400 uppercase tracking-tight">Active Pulse</p>
          </div>
        </div>

        <button @click="handleLogout" class="w-full flex items-center gap-4 p-4 rounded-2xl transition-all hover:bg-rose-50 text-gray-400 hover:text-rose-600 group">
          <svg class="w-6 h-6 transition-transform group-hover:scale-125" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          <span class="font-bold hidden lg:block">Disconnect Engine</span>
        </button>
      </div>
    </aside>

    <main class="flex-1 overflow-y-auto relative">
      <RouterView v-slot="{ Component }">
        <transition 
          name="fade" 
          mode="out-in"
        >
          <component :is="Component" />
        </transition>
      </RouterView>
    </main>
    <ToastContainer />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&display=swap');

body {
  font-family: 'Plus Jakarta Sans', sans-serif;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: #CBD5E1;
  border-radius: 20px;
}
::-webkit-scrollbar-thumb:hover {
  background: #94A3B8;
}
</style>

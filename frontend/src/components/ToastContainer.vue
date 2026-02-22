<script setup lang="ts">
import { useToastStore } from '@/stores/toast';

const toastStore = useToastStore();
</script>

<template>
  <div class="fixed top-8 right-8 z-[9999] space-y-4 pointer-events-none">
    <transition-group 
      name="toast"
      enter-active-class="transform ease-out duration-300 transition"
      enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2"
      enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
      leave-active-class="transition ease-in duration-100"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div 
        v-for="toast in toastStore.toasts" 
        :key="toast.id"
        class="max-w-sm w-full bg-white shadow-2xl rounded-2xl pointer-events-auto overflow-hidden border border-gray-100 flex items-center p-4 gap-4 ring-1 ring-black/5"
      >
        <div :class="[
          'w-10 h-10 rounded-xl flex items-center justify-center text-xl shrink-0',
          toast.type === 'success' ? 'bg-green-100 text-green-600' : 
          toast.type === 'error' ? 'bg-red-100 text-red-600' : 
          toast.type === 'warning' ? 'bg-yellow-100 text-yellow-600' : 'bg-blue-100 text-blue-600'
        ]">
          {{ toast.type === 'success' ? '✅' : toast.type === 'error' ? '❌' : toast.type === 'warning' ? '⚠️' : 'ℹ️' }}
        </div>
        <div class="flex-1">
          <p class="text-sm font-black text-gray-900 leading-tight">{{ toast.message }}</p>
        </div>
        <button 
          @click="toastStore.remove(toast.id)"
          class="text-gray-400 hover:text-gray-600 transition-colors"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
    </transition-group>
  </div>
</template>

<style scoped>
.toast-move {
  transition: all 0.3s ease;
}
</style>

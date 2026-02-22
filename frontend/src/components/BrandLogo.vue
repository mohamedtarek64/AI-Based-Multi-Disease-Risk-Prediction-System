<template>
  <div :class="[sizeClasses[props.size || 'md'], 'relative flex items-center justify-center shrink-0']">
    <!-- Outer Glow -->
    <div class="absolute inset-0 bg-blue-400/20 blur-xl rounded-full scale-150 animate-pulse"></div>
    
    <!-- Shield Base -->
    <svg 
      class="w-full h-full relative z-10 drop-shadow-2xl" 
      viewBox="0 0 100 100" 
      fill="none" 
      xmlns="http://www.w3.org/2000/svg"
    >
      <defs>
        <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#3B82F6" />
          <stop offset="100%" stop-color="#1E1B4B" />
        </linearGradient>
      </defs>
      
      <!-- Hexagon Morph -->
      <path 
        d="M50 5L90 27.5V72.5L50 95L10 72.5V27.5L50 5Z" 
        fill="url(#logoGrad)" 
        stroke="white" 
        stroke-width="2"
        stroke-opacity="0.2"
      />
      
      <!-- AI Nodes & Pulse -->
      <path 
        d="M30 50H45L50 35L55 65L60 50H75" 
        stroke="white" 
        stroke-width="5" 
        stroke-linecap="round" 
        stroke-linejoin="round"
        class="animate-[dash_3s_linear_infinite]"
        stroke-dasharray="100"
        stroke-dashoffset="100"
      />
      
      <!-- Orbitals -->
      <circle cx="50" cy="50" r="38" stroke="white" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="4 4" />
      <circle cx="85" cy="30" r="4" fill="#60A5FA" />
      <circle cx="15" cy="70" r="4" fill="#818CF8" />
    </svg>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  size?: 'sm' | 'md' | 'lg' | 'xl';
}>();

const sizeClasses = {
  sm: 'w-8 h-8',
  md: 'w-12 h-12',
  lg: 'w-16 h-16',
  xl: 'w-24 h-24'
};
</script>

<style scoped>
@keyframes dash {
  0% { stroke-dashoffset: 200; opacity: 0; }
  20% { opacity: 1; }
  80% { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 0; }
}
</style>

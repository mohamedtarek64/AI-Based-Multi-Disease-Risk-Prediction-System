<script setup lang="ts">
defineProps<{
  type: 'diet' | 'exercise' | 'medical' | 'lifestyle';
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high';
}>();

const icons = {
  diet: 'M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71L12 2z', // Salad/Leaf abstract
  exercise: 'M13.5 5.5c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zM9.8 8.9L7 21h2l2.1-8.9L13 14v7h2V12.5l-2.1-2.1c1.3-.8 2.3-2.1 2.3-3.6h-2c0 1.1-.9 2-2 2v-2z', // Runner
  medical: 'M19 3H5c-1.1 0-1.99.9-1.99 2L3 19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-1 11h-4v4h-4v-4H6v-4h4V6h4v4h4v4z', // Hospital/Cross
  lifestyle: 'M12 22a9 9 0 1 1 0-18 9 9 0 0 1 0 18zm0-2a7 7 0 1 0 0-14 7 7 0 0 0 0 14z' // Circle/Meditation
};

const priorityColors = {
  low: 'text-blue-600 bg-blue-50 border-blue-100',
  medium: 'text-orange-600 bg-orange-50 border-orange-100',
  high: 'text-rose-600 bg-rose-50 border-rose-100'
};
</script>

<template>
  <div class="p-6 border border-gray-100/50 rounded-[2rem] bg-white/80 backdrop-blur-sm shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all group">
    <div class="flex items-start gap-5">
      <div class="w-14 h-14 shrink-0 bg-gray-50 rounded-2xl flex items-center justify-center text-gray-400 group-hover:bg-blue-600 group-hover:text-white transition-colors">
        <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24">
          <path :d="icons[type]" />
        </svg>
      </div>
      <div class="flex-1">
        <div class="flex justify-between items-start mb-2">
          <h4 class="font-black text-gray-900 tracking-tight group-hover:text-blue-600 transition-colors">{{ title }}</h4>
          <span :class="['px-3 py-1 rounded-full text-[9px] font-black uppercase tracking-widest border', priorityColors[priority]]">
            {{ priority }}
          </span>
        </div>
        <p class="text-xs text-gray-500 font-medium leading-relaxed">{{ description }}</p>
      </div>
    </div>
  </div>
</template>

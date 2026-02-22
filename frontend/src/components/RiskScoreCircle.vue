<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  score: number;
  level: string;
}>();

const color = computed(() => {
  switch (props.level.toLowerCase()) {
    case 'low': return '#10B981'; // Emerald 500
    case 'medium': return '#F59E0B'; // Amber 500
    case 'high': return '#EF4444'; // Red 500
    case 'critical': return '#7F1D1D'; // Red 900
    default: return '#6B7280'; // Gray 500
  }
});

const circumference = 2 * Math.PI * 45;
const offset = computed(() => circumference - (props.score / 100) * circumference);
</script>

<template>
  <div class="relative flex items-center justify-center w-48 h-48">
    <svg class="transform -rotate-90 w-full h-full">
      <!-- Background Circle -->
      <circle
        cx="96" cy="96" r="45"
        stroke="currentColor"
        stroke-width="12"
        fill="transparent"
        class="text-gray-200"
      />
      <!-- Progress Circle -->
      <circle
        cx="96" cy="96" r="45"
        stroke="currentColor"
        stroke-width="12"
        fill="transparent"
        :stroke-dasharray="circumference"
        :stroke-dashoffset="offset"
        stroke-linecap="round"
        :style="{ color: color }"
        class="transition-all duration-1000 ease-out"
      />
    </svg>
    <div class="absolute flex flex-col items-center">
      <span class="text-4xl font-bold" :style="{ color: color }">{{ Math.round(score) }}%</span>
      <span class="text-sm font-medium uppercase tracking-wider text-gray-500">{{ level }}</span>
    </div>
  </div>
</template>

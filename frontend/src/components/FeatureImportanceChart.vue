<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  factors: Record<string, number>;
}>();

const sortedFactors = computed(() => {
  return Object.entries(props.factors)
    .sort((a, b) => Math.abs(b[1]) - Math.abs(a[1]))
    .slice(0, 8); // Top 8 factors
});

const maxVal = computed(() => {
  return Math.max(...sortedFactors.value.map(f => Math.abs(f[1])), 0.1);
});

const formatLabel = (label: string) => {
  return label.replace(/_/g, ' ').toUpperCase();
};
</script>

<template>
  <div class="space-y-4 w-full">
    <h3 class="text-lg font-semibold text-gray-800">Key Risk Drivers (SHAP Analysis)</h3>
    <div class="space-y-3">
      <div v-for="[name, value] in sortedFactors" :key="name" class="group">
        <div class="flex justify-between text-xs font-medium mb-1">
          <span class="text-gray-600">{{ formatLabel(name) }}</span>
          <span :class="value > 0 ? 'text-red-500' : 'text-blue-500'">
            {{ value > 0 ? '+' : '' }}{{ value.toFixed(2) }}
          </span>
        </div>
        <div class="relative h-2 bg-gray-100 rounded-full overflow-hidden">
          <div 
            class="absolute top-0 h-full transition-all duration-1000"
            :class="value > 0 ? 'bg-red-500 right-1/2 left-auto' : 'bg-blue-500 left-1/2 right-auto'"
            :style="{ width: (Math.abs(value) / maxVal * 50) + '%' }"
          ></div>
          <!-- Center line -->
          <div class="absolute inset-y-0 left-1/2 w-px bg-gray-300"></div>
        </div>
      </div>
    </div>
    <div class="flex justify-between text-[10px] uppercase text-gray-400 font-bold px-1">
      <span>Decreases Risk</span>
      <span>Increases Risk</span>
    </div>
  </div>
</template>

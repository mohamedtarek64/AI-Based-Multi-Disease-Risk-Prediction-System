<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';
import { useToastStore } from '@/stores/toast';

const router = useRouter();
const predictionStore = usePredictionStore();
const toast = useToastStore();

const form = ref<any>({
  age: 45,
  gender: 'female',
  smoking_years: 10,
  alcohol_consumption: 'medium',
  family_history: false,
  environmental_exposure: false,
  bmi: 24.5,
  radiation_exposure: false,
  genetic_markers: false
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('cancer', form.value);
    toast.show('Genetic markers decoded successfully.', 'success');
    router.push({ name: 'prediction-result', params: { id: result.id } });
  } catch (error) {
    toast.show('ML Engine Error: Assessment failed.', 'error');
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 font-sans">
    <div class="max-w-4xl mx-auto">
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-purple-50">
        <!-- Header -->
        <div class="bg-gradient-to-br from-indigo-700 to-purple-800 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">🧬</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Oncology AI Risk</h1>
              <p class="text-purple-100 font-medium opacity-90 text-lg">Genetic & Environmental Risk Assessment</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Age</label>
              <input v-model="form.age" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-purple-500 transition-all font-bold text-lg border" />
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Alcohol Consumption</label>
              <select v-model="form.alcohol_consumption" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-purple-500 transition-all font-bold text-lg border">
                <option value="none">None / Rare</option>
                <option value="medium">Social / Moderate</option>
                <option value="high">High / Frequent</option>
              </select>
            </div>
          </div>

          <div class="space-y-8">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-purple-600 rounded-full"></span>
              Exposure & Lifestyle
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Smoking Years</label>
                <input v-model="form.smoking_years" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-purple-500 border transition-all font-bold" />
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">BMI (Body Mass Index)</label>
                <input v-model="form.bmi" type="number" step="0.1" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-purple-500 border transition-all font-bold" />
              </div>
            </div>
          </div>

          <!-- Risk Factors Toggles -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div v-for="(val, key) in { family_history: 'Family History', environmental_exposure: 'Toxic Exposure', radiation_exposure: 'Radiation History', genetic_markers: 'Known Genetic Markers' }" :key="key" 
                 class="flex items-center justify-between p-6 bg-purple-50 rounded-3xl border border-purple-100/50">
              <span class="font-black text-purple-900">{{ val }}</span>
              <label class="relative inline-flex items-center cursor-pointer">
                <input type="checkbox" v-model="form[key]" class="sr-only peer">
                <div class="w-11 h-6 bg-gray-200 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-purple-600"></div>
              </label>
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-purple-900 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-purple-900 hover:-translate-y-1 active:scale-[0.98] transition-all flex items-center justify-center gap-4"
          >
            <span v-if="isSubmitting" class="animate-pulse">✨</span>
            {{ isSubmitting ? 'Decoding DNA Patterns...' : 'Run Oncology Analysis' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';

const router = useRouter();
const predictionStore = usePredictionStore();

const form = ref({
  age: 40,
  smoking_status: 'never',
  air_pollution_exposure: 'medium',
  cough_freq: 1,
  shortness_of_breath: 0,
  fatigue_level: 2,
  chest_tightness: false,
  fever_episodes: 0,
  occupational_dust: false
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('respiratory', form.value);
    router.push({ name: 'prediction-result', params: { id: result.id } });
  } catch (error) {
    alert('Analysis failed.');
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 font-sans">
    <div class="max-w-4xl mx-auto">
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-cyan-50">
        <!-- Header -->
        <div class="bg-gradient-to-br from-cyan-600 to-sky-700 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">🫁</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Respiratory Health</h1>
              <p class="text-cyan-50 font-medium opacity-90 text-lg">Lung & Airway System Assessment</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Smoking Status</label>
              <select v-model="form.smoking_status" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-cyan-500 transition-all font-bold text-lg border">
                <option value="never">Never Smoked</option>
                <option value="former">Former Smoker</option>
                <option value="current">Current Smoker</option>
              </select>
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Air Quality exposure</label>
              <select v-model="form.air_pollution_exposure" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-cyan-500 transition-all font-bold text-lg border">
                <option value="low">Low (Rural/Clean)</option>
                <option value="medium">Medium (Urban)</option>
                <option value="high">High (Industrial)</option>
              </select>
            </div>
          </div>

          <div class="space-y-10">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-cyan-500 rounded-full"></span>
              Symptom Severity
            </h3>
            <div v-for="symptom in [
              { key: 'cough_freq', label: 'Cough Frequency' },
              { key: 'shortness_of_breath', label: 'Breath Shortness' },
              { key: 'fatigue_level', label: 'Overall Fatigue' },
              { key: 'fever_episodes', label: 'Recent Fever Episodes' }
            ]" :key="symptom.key" class="space-y-4">
              <div class="flex justify-between items-center">
                <label class="text-sm font-black text-gray-700 uppercase">{{ symptom.label }}</label>
                <span class="px-3 py-1 bg-cyan-100 text-cyan-700 rounded-lg text-xs font-black">{{ form[symptom.key] }} / 4</span>
              </div>
              <input type="range" min="0" max="4" v-model="form[symptom.key]" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-cyan-600" />
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex items-center justify-between p-6 bg-cyan-50 rounded-3xl border border-cyan-100/50">
              <span class="font-black text-cyan-900">Chest Tightness</span>
              <input type="checkbox" v-model="form.chest_tightness" class="w-8 h-8 rounded-xl text-cyan-600 focus:ring-cyan-500 border-none shadow-sm" />
            </div>
            <div class="flex items-center justify-between p-6 bg-cyan-50 rounded-3xl border border-cyan-100/50">
              <span class="font-black text-cyan-900">Occupational Dust</span>
              <input type="checkbox" v-model="form.occupational_dust" class="w-8 h-8 rounded-xl text-cyan-600 focus:ring-cyan-500 border-none shadow-sm" />
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-cyan-700 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-cyan-800 transition-all flex items-center justify-center gap-4"
          >
            {{ isSubmitting ? 'Measuring Airflow...' : 'Start Assessment' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

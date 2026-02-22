<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';

const router = useRouter();
const predictionStore = usePredictionStore();

const form = ref({
  age: 45,
  bmi: 27.5,
  stress_level: 5,
  salt_intake: 'medium',
  alcohol_consumption: 'medium',
  physical_activity: 'medium',
  smoking: 'never',
  sleep_hours: 7,
  genetics: false
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('hypertension', form.value);
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
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-blue-50">
        <!-- Header -->
        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">💉</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Hypertension Monitor</h1>
              <p class="text-blue-50 font-medium opacity-90 text-lg">Vascular System Risk Evaluation</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Age</label>
              <input v-model="form.age" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-blue-500 transition-all font-bold text-lg border" />
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">BMI</label>
              <input v-model="form.bmi" type="number" step="0.1" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-blue-500 transition-all font-bold text-lg border" />
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Sleep Hours</label>
              <input v-model="form.sleep_hours" type="number" step="0.5" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-blue-500 transition-all font-bold text-lg border" />
            </div>
          </div>

          <div class="space-y-10">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-blue-500 rounded-full"></span>
              Lifestyle & Stress
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="block text-xs font-extrabold text-gray-500 uppercase tracking-widest">Stress Level (1-10)</label>
                <input type="range" min="1" max="10" v-model="form.stress_level" class="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-600" />
                <div class="flex justify-between text-xs font-bold text-blue-600"><span>Calm</span><span>Stressed</span></div>
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-extrabold text-gray-500 uppercase tracking-widest">Salt Intake</label>
                <select v-model="form.salt_intake" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-blue-500 border transition-all font-bold">
                  <option value="low">Low / Dash Diet</option>
                  <option value="medium">Medium / Standard</option>
                  <option value="high">High / Salt Heavy</option>
                </select>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
             <div class="flex items-center justify-between p-6 bg-blue-50 rounded-3xl border border-blue-100/50">
              <span class="font-black text-blue-900">Genetics (Family Hx)</span>
              <input type="checkbox" v-model="form.genetics" class="w-8 h-8 rounded-xl text-blue-600 focus:ring-blue-500 border-none shadow-sm" />
            </div>
            <div class="space-y-3 px-6">
              <label class="block text-xs font-extrabold text-gray-400 uppercase tracking-widest">Physical Activity</label>
              <select v-model="form.physical_activity" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-blue-500 border transition-all font-bold">
                <option value="low">Sedentary</option>
                <option value="medium">Moderate</option>
                <option value="high">Active</option>
              </select>
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-blue-700 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-blue-800 transition-all flex items-center justify-center gap-4"
          >
            {{ isSubmitting ? 'Measuring Pressure Patterns...' : 'Run Prediction Engine' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

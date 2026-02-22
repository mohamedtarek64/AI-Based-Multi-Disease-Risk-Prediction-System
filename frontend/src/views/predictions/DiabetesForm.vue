<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';
import { useToastStore } from '@/stores/toast';

const router = useRouter();
const predictionStore = usePredictionStore();
const toast = useToastStore();

const form = ref({
  age: 45,
  gender: 'male',
  bmi: 28.5,
  glucose: 120,
  blood_pressure: 80,
  insulin: 85,
  family_history: false,
  physical_activity: 'medium',
  smoking: 'never'
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('diabetes', form.value);
    toast.show('AI Analysis Complete!', 'success');
    router.push({ name: 'prediction-result', params: { id: result.id } });
  } catch (error) {
    toast.show('ML Service Connection Failed', 'error');
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <div class="bg-white rounded-3xl shadow-xl overflow-hidden border border-gray-100">
        <!-- Header -->
        <div class="bg-gradient-to-r from-orange-500 to-red-500 p-8 text-white">
          <div class="flex items-center gap-4 mb-2">
            <span class="text-4xl">🩺</span>
            <h1 class="text-3xl font-bold">Diabetes Risk Assessment</h1>
          </div>
          <p class="text-orange-50 opacity-90">Please provide accurate medical data for a precise AI evaluation.</p>
        </div>

        <form @submit.prevent="handleSubmit" class="p-8 space-y-8">
          <!-- Bio Data Section -->
          <section>
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center">
              <span class="w-8 h-8 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center mr-3 text-sm">1</span>
              Personal & Biological Info
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 uppercase tracking-wider">Age</label>
                <input v-model="form.age" type="number" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border" />
              </div>
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 uppercase tracking-wider">Gender</label>
                <select v-model="form.gender" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border">
                  <option value="male">Male</option>
                  <option value="female">Female</option>
                </select>
              </div>
            </div>
          </section>

          <hr class="border-gray-100" />

          <!-- Clinical Data Section -->
          <section>
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center">
              <span class="w-8 h-8 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center mr-3 text-sm">2</span>
              Clinical Measurements
            </h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 uppercase tracking-wider">BMI</label>
                <input v-model="form.bmi" type="number" step="0.1" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border" />
              </div>
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 uppercase tracking-wider text-xs">Glucose (mg/dL)</label>
                <input v-model="form.glucose" type="number" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border" />
              </div>
              <div class="space-y-2">
                <label class="text-sm font-bold text-gray-700 uppercase tracking-wider text-xs">Pressure (mmHg)</label>
                <input v-model="form.blood_pressure" type="number" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border" />
              </div>
            </div>
          </section>

          <hr class="border-gray-100" />

          <!-- Lifestyle Section -->
          <section>
            <h2 class="text-xl font-bold text-gray-900 mb-6 flex items-center">
              <span class="w-8 h-8 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center mr-3 text-sm">3</span>
              Lifestyle & History
            </h2>
            <div class="space-y-6">
              <div class="flex items-center justify-between p-4 bg-orange-50 rounded-2xl border border-orange-100">
                <div>
                  <h4 class="font-bold text-orange-900">Family History</h4>
                  <p class="text-sm text-orange-700">Does any close relative have diabetes?</p>
                </div>
                <label class="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" v-model="form.family_history" class="sr-only peer">
                  <div class="w-14 h-7 bg-gray-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all peer-checked:bg-orange-600"></div>
                </label>
              </div>

              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-2">
                  <label class="text-sm font-bold text-gray-700 uppercase tracking-wider">Physical Activity</label>
                  <select v-model="form.physical_activity" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border">
                    <option value="low">Low (Sedentary)</option>
                    <option value="medium">Medium</option>
                    <option value="high">High (Athlete)</option>
                  </select>
                </div>
                <div class="space-y-2">
                  <label class="text-sm font-bold text-gray-700 uppercase tracking-wider">Smoking Status</label>
                  <select v-model="form.smoking" class="w-full px-4 py-3 rounded-xl border-gray-200 focus:border-orange-500 focus:ring-orange-500 bg-gray-50 transition-all border">
                    <option value="never">Never Smoked</option>
                    <option value="former">Former Smoker</option>
                    <option value="current">Current Smoker</option>
                  </select>
                </div>
              </div>
            </div>
          </section>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-4 bg-orange-600 text-white rounded-2xl font-bold text-xl shadow-xl shadow-orange-100 hover:bg-orange-700 hover:-translate-y-1 active:scale-95 transition-all flex items-center justify-center gap-3"
          >
            <span v-if="isSubmitting" class="animate-spin text-2xl">⏳</span>
            {{ isSubmitting ? 'Analyzing Data...' : 'Run Prediction Engine' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

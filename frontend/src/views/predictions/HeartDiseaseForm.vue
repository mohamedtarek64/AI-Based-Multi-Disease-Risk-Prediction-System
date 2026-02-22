<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';
import { useToastStore } from '@/stores/toast';

const router = useRouter();
const predictionStore = usePredictionStore();
const toast = useToastStore();

const form = ref({
  age: 55,
  gender: 'male',
  chest_pain_type: 1,
  resting_bp: 130,
  cholesterol: 240,
  fasting_bs: false,
  resting_ecg: 1,
  max_heart_rate: 150,
  exercise_angina: false,
  st_depression: 1.0,
  st_slope: 1,
  major_vessels: 0,
  thalassemia: 2
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('heart', form.value);
    toast.show('Neural Engine: Analysis Success', 'success');
    router.push({ name: 'prediction-result', params: { id: result.id } });
  } catch (error) {
    toast.show('Service unavailable. Try again.', 'error');
  } finally {
    isSubmitting.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8 font-sans">
    <div class="max-w-4xl mx-auto">
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-gray-100">
        <!-- Header -->
        <div class="bg-gradient-to-br from-rose-600 to-red-700 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">❤️</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Cardiovascular Risk</h1>
              <p class="text-rose-100 font-medium opacity-90 text-lg">Deep AI Heart Health Diagnostics</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <!-- Bio & Basics -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Age</label>
              <input v-model="form.age" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:ring-4 focus:ring-rose-500/10 focus:border-rose-500 transition-all font-bold text-lg border" />
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Gender</label>
              <select v-model="form.gender" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:ring-4 focus:ring-rose-500/10 focus:border-rose-500 transition-all font-bold text-lg border">
                <option value="male">Male</option>
                <option value="female">Female</option>
              </select>
            </div>
          </div>

          <hr class="border-gray-50" />

          <!-- Clinical Section -->
          <div class="space-y-8">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-rose-500 rounded-full"></span>
              Cardiac Measurements
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Resting BP (mmHg)</label>
                <input v-model="form.resting_bp" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-rose-500 border transition-all font-bold" />
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Cholesterol (mg/dL)</label>
                <input v-model="form.cholesterol" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-rose-500 border transition-all font-bold" />
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Max Heart Rate</label>
                <input v-model="form.max_heart_rate" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-rose-500 border transition-all font-bold" />
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Chest Pain Type (0-3)</label>
                <select v-model="form.chest_pain_type" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-rose-500 border transition-all font-bold">
                  <option :value="0">Typical Angina</option>
                  <option :value="1">Atypical Angina</option>
                  <option :value="2">Non-anginal Pain</option>
                  <option :value="3">Asymptomatic</option>
                </select>
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">ST Depression</label>
                <input v-model="form.st_depression" type="number" step="0.1" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-rose-500 border transition-all font-bold" />
              </div>
            </div>
          </div>

          <!-- Toggles -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="flex items-center justify-between p-6 bg-rose-50 rounded-3xl border border-rose-100/50">
              <div>
                <h4 class="font-black text-rose-900">Exercise Angina</h4>
                <p class="text-xs text-rose-700 font-medium">Induced chest pain during activity?</p>
              </div>
              <input type="checkbox" v-model="form.exercise_angina" class="w-6 h-6 rounded text-rose-600 focus:ring-rose-500 border-none bg-white shadow-sm" />
            </div>
            <div class="flex items-center justify-between p-6 bg-rose-50 rounded-3xl border border-rose-100/50">
              <div>
                <h4 class="font-black text-rose-900">High Blood Sugar</h4>
                <p class="text-xs text-rose-700 font-medium">Fasting BS > 120 mg/dl?</p>
              </div>
              <input type="checkbox" v-model="form.fasting_bs" class="w-6 h-6 rounded text-rose-600 focus:ring-rose-500 border-none bg-white shadow-sm" />
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-gray-900 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-black hover:-translate-y-1 active:scale-[0.98] transition-all disabled:bg-gray-400 flex items-center justify-center gap-4"
          >
            <span v-if="isSubmitting" class="animate-spin text-2xl">⚡</span>
            {{ isSubmitting ? 'Processing Cardiac Data...' : 'Start Clinical Analysis' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

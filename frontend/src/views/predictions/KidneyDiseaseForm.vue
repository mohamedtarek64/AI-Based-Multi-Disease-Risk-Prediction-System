<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';

const router = useRouter();
const predictionStore = usePredictionStore();

const form = ref({
  age: 50,
  blood_pressure: 80,
  specific_gravity: 1.020,
  albumin: 0,
  sugar: 0,
  red_blood_cells: 'normal',
  pus_cell: 'normal',
  bacteria: 'notpresent',
  blood_glucose_random: 120
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('kidney', form.value);
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
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-emerald-50">
        <!-- Header -->
        <div class="bg-gradient-to-br from-emerald-600 to-teal-700 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">🫘</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Kidney Function Scan</h1>
              <p class="text-emerald-50 font-medium opacity-90 text-lg">Renal System Clinical AI Evaluation</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Age</label>
              <input v-model="form.age" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-emerald-500 transition-all font-bold text-lg border" />
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Blood Glucose Random</label>
              <input v-model="form.blood_glucose_random" type="number" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-emerald-500 transition-all font-bold text-lg border" />
            </div>
          </div>

          <div class="space-y-10">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-emerald-500 rounded-full"></span>
              Urine & Blood markers
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div class="space-y-3">
                <label class="block text-xs font-extrabold text-gray-500 uppercase tracking-widest">Specific Gravity</label>
                <select v-model="form.specific_gravity" class="w-full px-4 py-3 rounded-xl border-gray-100 bg-gray-50 font-bold border">
                  <option v-for="v in [1.005, 1.010, 1.015, 1.020, 1.025]" :key="v" :value="v">{{ v }}</option>
                </select>
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-extrabold text-gray-500 uppercase tracking-widest">Albumin (0-5)</label>
                <input v-model="form.albumin" type="number" min="0" max="5" class="w-full px-4 py-4 rounded-xl border-gray-100 bg-gray-50 font-bold border" />
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-extrabold text-gray-500 uppercase tracking-widest">Sugar (0-5)</label>
                <input v-model="form.sugar" type="number" min="0" max="5" class="w-full px-4 py-4 rounded-xl border-gray-100 bg-gray-50 font-bold border" />
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div v-for="(val, key) in { red_blood_cells: 'Red Blood Cells', pus_cell: 'Pus Cells', bacteria: 'Bacteria' }" :key="key" 
                 class="p-6 bg-emerald-50 rounded-3xl border border-emerald-100/50 space-y-3 font-sans">
              <span class="block font-black text-emerald-900 text-xs uppercase tracking-widest">{{ val }}</span>
              <select v-model="form[key]" class="w-full bg-transparent border-b-2 border-emerald-200 outline-none font-bold text-emerald-800">
                <option v-if="key !== 'bacteria'" value="normal">Normal</option>
                <option v-if="key !== 'bacteria'" value="abnormal">Abnormal</option>
                <option v-if="key === 'bacteria'" value="present">Present</option>
                <option v-if="key === 'bacteria'" value="notpresent">Not Present</option>
              </select>
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-emerald-700 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-emerald-800 transition-all flex items-center justify-center gap-4"
          >
            {{ isSubmitting ? 'Evaluating Renal Biomarkers...' : 'Calculate Kidney Risk' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

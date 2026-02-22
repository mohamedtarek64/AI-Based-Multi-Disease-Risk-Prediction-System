<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';

const router = useRouter();
const predictionStore = usePredictionStore();

const form = ref({
  age: 38,
  diet_quality: 'medium',
  processed_meat_intake: 'medium',
  abdominal_pain_freq: 2,
  heartburn_freq: 1,
  bowel_habit_changes: false,
  family_history: false,
  bmi: 26.0,
  unexplained_weight_loss: false
});

const isSubmitting = ref(false);

const handleSubmit = async () => {
  isSubmitting.value = true;
  try {
    const result = await predictionStore.predictDisease('digestive', form.value);
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
      <div class="bg-white rounded-[2.5rem] shadow-2xl overflow-hidden border border-yellow-50">
        <!-- Header -->
        <div class="bg-gradient-to-br from-yellow-500 to-orange-600 p-10 text-white">
          <div class="flex items-center gap-6 mb-4">
            <span class="text-5xl bg-white/20 p-4 rounded-3xl backdrop-blur-md">🍕</span>
            <div>
              <h1 class="text-4xl font-black tracking-tight">Digestive AI Screening</h1>
              <p class="text-yellow-50 font-medium opacity-90 text-lg">Gastrointestinal System Health Scan</p>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit" class="p-10 space-y-12">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Diet Quality</label>
              <select v-model="form.diet_quality" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-yellow-500 transition-all font-bold text-lg border">
                <option value="healthy">Healthy (Whole foods)</option>
                <option value="medium">Medium / Balanced</option>
                <option value="junk">Junk / Processed</option>
              </select>
            </div>
            <div class="space-y-3">
              <label class="block text-sm font-extrabold text-gray-400 uppercase tracking-widest">Processed Meat Intake</label>
              <select v-model="form.processed_meat_intake" class="w-full px-5 py-4 rounded-2xl border-gray-100 bg-gray-50 focus:border-yellow-500 transition-all font-bold text-lg border">
                <option value="low">Low (Rarely)</option>
                <option value="medium">Medium (Social)</option>
                <option value="high">High (Daily)</option>
              </select>
            </div>
          </div>

          <div class="space-y-8">
            <h3 class="text-2xl font-black text-gray-900 flex items-center gap-3">
              <span class="w-2 h-8 bg-yellow-500 rounded-full"></span>
              Symptom Frequency (0-4)
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Abdominal Pain</label>
                <input v-model="form.abdominal_pain_freq" type="range" min="0" max="4" class="w-full h-3 bg-gray-100 rounded-lg appearance-none cursor-pointer accent-yellow-500" />
                <div class="flex justify-between text-[10px] font-bold text-gray-400 uppercase"><span>Never</span><span>Frequent</span></div>
              </div>
              <div class="space-y-3">
                <label class="block text-xs font-bold text-gray-500 uppercase">Heartburn / Reflux</label>
                <input v-model="form.heartburn_freq" type="range" min="0" max="4" class="w-full h-3 bg-gray-100 rounded-lg appearance-none cursor-pointer accent-yellow-500" />
                <div class="flex justify-between text-[10px] font-bold text-gray-400 uppercase"><span>Never</span><span>Frequent</span></div>
              </div>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="(val, key) in { bowel_habit_changes: 'Bowel Habit Changes', family_history: 'Family GI History', unexplained_weight_loss: 'Weight Loss' }" :key="key" 
                 class="flex flex-col gap-4 p-6 bg-yellow-50 rounded-3xl border border-yellow-100/50">
              <span class="font-black text-yellow-900 text-sm">{{ val }}</span>
              <input type="checkbox" v-model="form[key]" class="w-8 h-8 rounded-xl text-yellow-600 focus:ring-yellow-500 border-none bg-white shadow-inner" />
            </div>
            <div class="flex flex-col gap-2 p-6 bg-gray-50 rounded-3xl border border-gray-100">
               <span class="font-black text-gray-900 text-sm">BMI</span>
               <input v-model="form.bmi" type="number" step="0.1" class="w-full p-2 bg-transparent border-b-2 border-yellow-500 font-bold outline-none" />
            </div>
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="w-full py-6 bg-yellow-600 text-white rounded-3xl font-black text-xl shadow-2xl hover:bg-yellow-700 hover:-translate-y-1 active:scale-[0.98] transition-all flex items-center justify-center gap-4"
          >
            {{ isSubmitting ? 'Analyzing Gut Biome...' : 'Scan System' }}
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

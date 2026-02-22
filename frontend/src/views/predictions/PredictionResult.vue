<script setup lang="ts">
import { onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';
import RiskScoreCircle from '@/components/RiskScoreCircle.vue';
import FeatureImportanceChart from '@/components/FeatureImportanceChart.vue';
import RecommendationCard from '@/components/RecommendationCard.vue';

const route = useRoute();
const router = useRouter();
const predictionStore = usePredictionStore();

const prediction = computed(() => predictionStore.currentPrediction);

onMounted(async () => {
  if (!prediction.value) {
    const id = route.params.id as string;
    await predictionStore.fetchPredictionById(id);
    
    // Fallback if still not found
    if (!predictionStore.currentPrediction) {
      router.push({ name: 'predict-select' });
    }
  }
});

const recommendations = computed(() => {
  if (!prediction.value) return [];
  const level = prediction.value.risk_level.toLowerCase();
  const type = prediction.value.disease_type.toLowerCase();
  
  const recs: any[] = [];

  // Critical/High Risk - Urgent Actions
  if (level === 'high' || level === 'critical') {
    recs.push({ 
      type: 'medical', 
      title: 'Urgent Clinical Review', 
      description: `Your ${type} markers indicate significant concern. Please consult a specialist immediately.`, 
      priority: 'high' 
    });
  }

  // Disease Specific Advice
  if (type === 'diabetes') {
    recs.push({ type: 'diet', title: 'Glycemic Management', description: 'Eliminate refined sugars and focus on low-GI complex carbohydrates.', priority: level === 'low' ? 'medium' : 'high' });
    recs.push({ type: 'exercise', title: 'Insulin Sensitivity', description: '30 min of resistance training helps improve glucose uptake.', priority: 'medium' });
  } else if (type === 'heart' || type === 'hypertension') {
    recs.push({ type: 'diet', title: 'DASH Diet', description: 'Reduce sodium intake to < 2300mg/day and increase potassium-rich foods.', priority: 'high' });
    recs.push({ type: 'exercise', title: 'Cardiovascular Conditioning', description: 'Daily brisk walking or light jogging to strengthen heart muscle.', priority: 'medium' });
  } else if (type === 'kidney') {
    recs.push({ type: 'diet', title: 'Renal Nutrition', description: 'Monitor protein intake and stay hydrated. Avoid excessive salt.', priority: 'high' });
    recs.push({ type: 'medical', title: 'GFR Monitoring', description: 'Monthly blood tests to monitor glomerular filtration rate.', priority: 'medium' });
  } else if (type === 'cancer') {
    recs.push({ type: 'medical', title: 'Oncology Screening', description: 'Schedule biopsy or advanced imaging if recommended by your physician.', priority: 'high' });
    recs.push({ type: 'diet', title: 'Antioxidant Rich Diet', description: 'Increase intake of cruciferous vegetables and dark berries.', priority: 'medium' });
  } else if (type === 'respiratory') {
    recs.push({ type: 'exercise', title: 'Pulmonary Rehab', description: 'Breath control exercises to improve lung capacity and efficiency.', priority: 'medium' });
    recs.push({ type: 'medical', title: 'Spirometry Test', description: 'Regular lung function testing to track obstruction levels.', priority: 'high' });
  } else if (type === 'digestive') {
    recs.push({ type: 'diet', title: 'Microbiome Support', description: 'Integrate probiotics and fermented foods to balance gut flora.', priority: 'medium' });
    recs.push({ type: 'medical', title: 'Endoscopy Referral', description: 'Consider specialist consultation if symptoms persist.', priority: 'medium' });
  }

  return recs;
});
</script>

<template>
  <div v-if="prediction" class="min-h-screen bg-gray-50 p-8">
    <div class="max-w-6xl mx-auto">
      <header class="mb-12 text-center">
        <div class="inline-block px-4 py-1.5 bg-blue-100 text-blue-700 rounded-full text-xs font-bold uppercase tracking-widest mb-4">
          Analysis Complete
        </div>
        <h1 class="text-4xl font-extrabold text-gray-900">Your Health Report</h1>
      </header>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Result Summary -->
        <div class="lg:col-span-2 space-y-8">
          <div class="bg-white rounded-3xl p-10 shadow-xl border border-gray-100 flex flex-col md:flex-row items-center gap-12">
            <RiskScoreCircle :score="prediction.risk_score" :level="prediction.risk_level" />
            <div class="flex-1 text-center md:text-left">
              <h2 class="text-3xl font-black text-gray-900 mb-4">{{ prediction.disease_type.toUpperCase() }} Result</h2>
              <div :class="['inline-block px-6 py-2 rounded-2xl text-xl font-bold mb-6', 
                prediction.risk_level === 'Low' ? 'bg-emerald-100 text-emerald-700' : 'bg-red-100 text-red-700']">
                {{ prediction.risk_level }} Risk Detected
              </div>
              <p class="text-gray-600 leading-relaxed italic text-lg opacity-80">
                {{ prediction.prediction_result.interpretation }}
              </p>
            </div>
          </div>

          <!-- SHAP Details -->
          <div class="bg-white rounded-3xl p-10 shadow-lg border border-gray-100">
            <FeatureImportanceChart :factors="prediction.prediction_result.top_contributing_factors" />
          </div>
        </div>

        <!-- Sidebar Actions -->
        <div class="space-y-6">
          <h3 class="text-xl font-bold text-gray-900 flex items-center gap-2">
            <span>🛡️</span> Prevention Plan
          </h3>
          <RecommendationCard 
            v-for="rec in recommendations" 
            :key="rec.title"
            v-bind="rec"
          />
          
          <button @click="router.push('/predict')" class="w-full py-4 bg-gray-900 text-white rounded-2xl font-bold hover:bg-black transition-all">
            Perform Another Test
          </button>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="flex items-center justify-center min-h-screen">
    <div class="animate-pulse text-2xl font-bold text-gray-400">Loading Result...</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { usePredictionStore } from '@/stores/prediction';
import { useAuthStore } from '@/stores/auth';
import RiskScoreCircle from '@/components/RiskScoreCircle.vue';
import FeatureImportanceChart from '@/components/FeatureImportanceChart.vue';
import RecommendationCard from '@/components/RecommendationCard.vue';

const store = usePredictionStore();
const auth = useAuthStore();
const router = useRouter();

onMounted(() => {
  store.fetchHistory();
});

const lastPrediction = computed(() => {
  if (store.history.length === 0) return null;
  return store.history[0]; // history is sorted by latest
});

const stats = computed(() => [
  { label: 'Total Assessments', value: store.history.length.toString(), icon: 'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4z', color: 'text-blue-600' },
  { label: 'Current Level', value: lastPrediction.value?.risk_level || 'N/A', icon: 'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z', color: 'text-indigo-600' },
  { label: 'Latest Risk', value: lastPrediction.value ? `${lastPrediction.value.risk_score}%` : '0%', icon: 'M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z', color: 'text-rose-600' },
]);

// Trend Line Calculation
const trendPoints = computed(() => {
  const history = [...store.history].slice(0, 5).reverse();
  if (history.length < 2) return [];
  
  return history.map((p, i) => ({
    x: (i / (history.length - 1)) * 1000,
    y: 180 - (p.risk_score / 100) * 160 // Scale to 180 height
  }));
});

const trendPath = computed(() => {
  if (trendPoints.value.length < 2) return '';
  const points = trendPoints.value;
  let d = `M ${points[0].x} ${points[0].y}`;
  
  for (let i = 1; i < points.length; i++) {
    // Smooth curve approximation
    const cp1x = points[i-1].x + (points[i].x - points[i-1].x) / 2;
    d += ` C ${cp1x} ${points[i-1].y}, ${cp1x} ${points[i].y}, ${points[i].x} ${points[i].y}`;
  }
  
  // Close the path for gradient area
  const last = points[points.length - 1];
  const areaD = `${d} L ${last.x} 200 L 0 200 Z`;
  
  return d; // Returning line path for now
});

const trendAreaPath = computed(() => {
  if (trendPoints.value.length < 2) return '';
  const p = trendPath.value;
  const last = trendPoints.value[trendPoints.value.length - 1];
  return `${p} L ${last.x} 200 L 0 200 Z`;
});
const dashboardRecs = computed(() => {
  if (!lastPrediction.value) return [
    { type: 'medical' as const, title: 'Complete Profile', description: 'Finish your account setup to receive personalized AI medical insights.', priority: 'high' as const }
  ];
  const level = lastPrediction.value.risk_level.toLowerCase();
  if (level === 'high' || level === 'critical') {
    return [
      { type: 'medical' as const, title: 'Specialist Referral', description: 'Based on your recent critical scores, a specialized physical exam is recommended.', priority: 'high' as const },
      { type: 'diet' as const, title: 'Immediate Lifestyle Shift', description: 'Strict adherence to medical-grade nutrition is vital for risk mitigation.', priority: 'medium' as const }
    ];
  }
  return [
    { type: 'exercise' as const, title: 'Maintain Momentum', description: 'Your current risk levels are managed. Keep your daily activity consistent.', priority: 'medium' as const },
    { type: 'diet' as const, title: 'Systemic Health', description: 'Ensure balanced antioxidant intake to support long-term metabolic health.', priority: 'low' as const }
  ];
});
</script>

<template>
  <div class="min-h-screen bg-transparent p-8 lg:p-12">
    <div class="max-w-7xl mx-auto">
      <header class="mb-12 flex flex-col md:flex-row justify-between items-center md:items-end gap-6">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 bg-blue-100/50 text-blue-700 text-[10px] font-black uppercase tracking-widest rounded-full mb-4 border border-blue-200/50 backdrop-blur-md">
             <span class="w-1.5 h-1.5 bg-blue-500 rounded-full animate-pulse"></span>
             Clinical System Secure
          </div>
          <h1 class="text-6xl font-[1000] text-gray-900 tracking-tighter">Your <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent italic">Health Overview</span></h1>
          <p class="text-gray-400 mt-3 font-medium text-lg italic">Analytical breakdown of your latest specialist assessments.</p>
        </div>
        <button @click="router.push('/predict')" class="px-8 py-4 bg-gray-900 text-white rounded-[2rem] font-black shadow-2xl hover:bg-blue-600 hover:-translate-y-1 transition-all active:scale-95 flex items-center gap-3 group">
          <span>New AI Assessment</span>
          <svg class="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </button>
      </header>

      <div v-if="!lastPrediction" class="flex flex-col items-center justify-center py-32 bg-white/40 backdrop-blur-3xl rounded-[4rem] border border-dashed border-gray-200">
        <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mb-8">
           <svg class="w-12 h-12 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        </div>
        <h2 class="text-4xl font-[1000] text-gray-900 mb-4 tracking-tight">No Reports Generated</h2>
        <p class="text-gray-400 mb-10 font-bold text-lg">Initialize your first clinical exam to view analytical stats.</p>
        <button @click="router.push('/predict')" class="px-10 py-5 bg-blue-600 text-white rounded-[2rem] font-black shadow-2xl shadow-blue-200 hover:bg-blue-700 transition-all hover:scale-105">
          Start Clinical Exam
        </button>
      </div>

      <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Main Risk Card -->
        <div class="lg:col-span-2 space-y-8">
          <div class="bg-white/60 backdrop-blur-2xl rounded-[3rem] p-10 shadow-sm border border-white/50">
            <div class="flex flex-col md:flex-row items-center gap-12">
              <RiskScoreCircle :score="lastPrediction.risk_score" :level="lastPrediction.risk_level" />
              <div class="flex-1">
                <h2 class="text-3xl font-[1000] text-gray-900 mb-2 capitalize italic tracking-tight">{{ lastPrediction.disease_type }} Risk</h2>
                <div class="bg-blue-50/50 p-6 rounded-[2rem] border border-blue-100/50 mb-8 italic text-blue-900 font-medium leading-relaxed leading-relaxed">
                  "{{ lastPrediction.prediction_result.interpretation }}"
                </div>
                <div class="grid grid-cols-3 gap-4">
                  <div v-for="stat in stats" :key="stat.label" class="bg-white/80 p-6 rounded-3xl border border-gray-100/50 shadow-sm hover:shadow-md transition-shadow">
                    <div :class="['w-8 h-8 mb-4', stat.color]">
                      <svg viewBox="0 0 24 24" fill="currentColor"><path :d="stat.icon" /></svg>
                    </div>
                    <div class="text-xl font-[1000] text-gray-900">{{ stat.value }}</div>
                    <div class="text-[9px] font-black text-gray-400 uppercase tracking-widest mt-1">{{ stat.label }}</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- SHAP Explanation Area -->
          <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100">
            <FeatureImportanceChart :factors="lastPrediction.prediction_result.top_contributing_factors" />
          </div>

          <!-- Risk Evolution Trend -->
          <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100">
            <div class="flex items-center justify-between mb-8">
              <h3 class="text-xl font-bold text-gray-900">Risk Evolution</h3>
              <div class="flex gap-4">
                 <div class="flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-blue-600"></span><span class="text-[10px] uppercase font-bold text-gray-400">Past Trend</span></div>
              </div>
            </div>
            
            <!-- Simple Premium SVG Trend Line -->
            <div class="h-48 w-full relative group">
              <svg class="w-full h-full" viewBox="0 0 1000 200" preserveAspectRatio="none">
                <defs>
                  <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="rgba(37, 99, 235, 0.2)" />
                    <stop offset="100%" stop-color="rgba(37, 99, 235, 0)" />
                  </linearGradient>
                </defs>
                <!-- Area -->
                <path 
                  :d="trendAreaPath" 
                  fill="url(#gradient)"
                  class="transition-all duration-1000"
                />
                <!-- Line -->
                <path 
                  :d="trendPath" 
                  fill="none" 
                  stroke="#2563eb" 
                  stroke-width="4" 
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="transition-all duration-1000"
                />
                <!-- Data Points -->
                <circle 
                  v-for="(point, i) in trendPoints" :key="i"
                  :cx="point.x" :cy="point.y" r="6" 
                  fill="white" stroke="#2563eb" stroke-width="3"
                  class="hover:scale-125 transition-transform cursor-pointer"
                />
              </svg>
              <!-- X-Axis Labels -->
              <div class="flex justify-between mt-4 px-2">
                <span v-for="(p, i) in store.history.slice(0, 5).reverse()" :key="i" class="text-[10px] font-bold text-gray-400 uppercase tracking-tighter">
                  {{ new Date(p.created_at).toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Recommendations column -->
        <div class="space-y-6">
          <div class="bg-white/80 backdrop-blur-3xl rounded-[3rem] p-8 border border-white/50 shadow-sm">
            <h3 class="text-xl font-black text-gray-900 px-2 flex items-center gap-3 mb-8">
              <div class="w-10 h-10 bg-blue-100 rounded-2xl flex items-center justify-center text-blue-600">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg>
              </div>
              Prevention Hub
            </h3>
            <div class="space-y-4">
              <RecommendationCard 
                v-for="(rec, i) in dashboardRecs" 
                :key="i"
                v-bind="rec"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

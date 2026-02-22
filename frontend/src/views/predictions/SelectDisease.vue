<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const diseases = [
  { 
    name: 'Diabetes', 
    id: 'diabetes', 
    icon: 'M12 2c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z', // Alert icon style but we'll use a better one
    description: 'Specialized metabolic analysis for Type 2 Diabetes using glucose and insulin response markers.',
    color: 'from-blue-500 to-indigo-600',
    path: '/predict/diabetes',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z"/></svg>`
  },
  { 
    name: 'Cardiology', 
    id: 'heart', 
    icon: '❤️', 
    description: 'Deep neural evaluation of cardiovascular health including coronary metrics and arterial flow.',
    color: 'from-rose-500 to-red-600',
    path: '/predict/heart',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>`
  },
  { 
    name: 'Oncology', 
    id: 'cancer', 
    icon: '🧬', 
    description: 'Precision oncological risk screening based on genetic markers and environmental exposure data.',
    color: 'from-purple-600 to-violet-800',
    path: '/predict/cancer',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4.75 3.5l14.5 17M19.25 3.5l-14.5 17M12 3.5v17M3.5 12h17"/></svg>` // Abstract DNA
  },
  { 
    name: 'Vascular', 
    id: 'hypertension', 
    icon: '💉', 
    description: 'Hemodynamic assessment of systemic blood pressure and hypertension risk factors.',
    color: 'from-emerald-500 to-teal-700',
    path: '/predict/hypertension',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20m-7-7l7-7 7 7"/></svg>` // Upward trend / pressure
  },
  { 
    name: 'Nephrology', 
    id: 'kidney', 
    icon: '🫘', 
    description: 'Clinical evaluation of renal function and chronic kidney disease progression risk.',
    color: 'from-orange-500 to-amber-700',
    path: '/predict/kidney',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>` // Shield / Protection
  },
  { 
    name: 'Gastro', 
    id: 'digestive', 
    icon: '🍕', 
    description: 'Comprehensive screening for gastrointestinal disorders and internal systemic health.',
    color: 'from-pink-500 to-rose-700',
    path: '/predict/digestive',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3c-4.97 0-9 4.03-9 9s4.03 9 9 9s9-4.03 9-9s-4.03-9-9-9zm0 16c-3.87 0-7-3.13-7-7s3.13-7 7-7s7 3.13 7 7s-3.13 7-7 7z"/></svg>`
  },
  { 
    name: 'Pulmonology', 
    id: 'respiratory', 
    icon: '🫁', 
    description: 'Airway and pulmonary function analysis, focusing on chronic respiratory conditions.',
    color: 'from-cyan-500 to-blue-700',
    path: '/predict/respiratory',
    svg: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 11c2.21 0 4-1.79 4-4s-1.79-4-4-4s-4 1.79-4 4s1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>`
  }
];
</script>

<template>
  <div class="min-h-screen p-8 lg:p-16 relative overflow-hidden bg-transparent">
    <div class="max-w-7xl mx-auto relative z-10">
      <header class="mb-16">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-blue-100/50 backdrop-blur-md rounded-full text-blue-700 text-[10px] font-black uppercase tracking-widest mb-6 border border-blue-200/50">
          <span class="w-2 h-2 bg-blue-600 rounded-full animate-ping"></span>
          AI Diagnostic Cluster Active
        </div>
        <h1 class="text-6xl font-[1000] text-gray-900 tracking-tighter mb-4 leading-tight">
          Select <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent italic">Specialist</span> Module
        </h1>
        <p class="text-gray-500 text-xl font-medium max-w-2xl leading-relaxed">
          Initialize a specialized AI assessment. Our models use peer-reviewed clinical data to provide state-of-the-art health insights.
        </p>
      </header>

      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-8">
        <div
          v-for="disease in diseases"
          :key="disease.id"
          @click="router.push(disease.path)"
          class="group relative bg-white/40 backdrop-blur-2xl rounded-[3rem] p-8 transition-all duration-500 cursor-pointer border border-white/50 hover:border-blue-200/50 hover:shadow-[0_20px_80px_-20px_rgba(0,0,0,0.1)] hover:-translate-y-3"
        >
          <!-- Card Content -->
          <div :class="['w-20 h-20 rounded-[2rem] flex items-center justify-center mb-8 shadow-2xl transition-all duration-500 group-hover:scale-110 group-hover:rotate-6 bg-gradient-to-br text-white', disease.color]">
            <div class="w-10 h-10" v-html="disease.svg"></div>
          </div>

          <h3 class="text-2xl font-[900] text-gray-900 mb-4 tracking-tight">{{ disease.name }}</h3>
          <p class="text-gray-500 font-medium text-sm leading-relaxed mb-8">
            {{ disease.description }}
          </p>

          <div class="flex items-center justify-between">
            <span class="text-[10px] font-black text-gray-400 uppercase tracking-widest group-hover:text-gray-900 transition-colors">Start Assessment</span>
            <div class="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center transition-all group-hover:bg-blue-600 group-hover:text-white">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Background Pattern -->
    <div class="fixed inset-0 pointer-events-none -z-10 opacity-[0.05]" style="background-image: radial-gradient(#2563eb 1px, transparent 1px); background-size: 40px 40px;"></div>
  </div>
</template>

<style scoped>
.grid {
  perspective: 1000px;
}
</style>

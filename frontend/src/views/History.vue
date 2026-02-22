<script setup lang="ts">
import { onMounted } from 'vue';
import { usePredictionStore } from '@/stores/prediction';
import { useRouter } from 'vue-router';

const store = usePredictionStore();
const router = useRouter();

const diseaseIcons: Record<string, string> = {
  heart: 'M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l8.78-8.78 1.06-1.06a5.5 5.5 0 000-7.78z',
  diabetes: 'M12 2L4.5 20.29l.71.71L12 18l6.79 3 .71-.71z',
  cancer: 'M4.75 3.5l14.5 17M19.25 3.5l-14.5 17M12 3.5v17M3.5 12h17',
  default: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'
};

onMounted(() => {
  store.fetchHistory();
});

const getRiskColor = (level: string) => {
  const l = level.toLowerCase();
  if (l === 'critical' || l === 'high') return 'text-red-600 bg-red-50 border-red-100';
  if (l === 'medium') return 'text-yellow-600 bg-yellow-50 border-yellow-100';
  return 'text-green-600 bg-green-50 border-green-100';
};
</script>

<template>
  <div class="p-8 lg:p-12 max-w-6xl mx-auto bg-transparent">
    <header class="mb-16">
      <div class="inline-flex items-center gap-2 px-3 py-1 bg-gray-100/50 backdrop-blur-md rounded-full text-gray-400 text-[10px] font-black uppercase tracking-widest mb-4 border border-gray-200/50">
         Historical Record Vault
      </div>
      <h1 class="text-5xl font-[1000] text-gray-900 tracking-tighter">Diagnostic <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent italic">History</span></h1>
      <p class="text-gray-400 mt-3 font-medium text-lg italic">View and audit your prior AI-generated medical reports.</p>
    </header>

    <div v-if="store.history.length === 0" class="bg-white/40 backdrop-blur-3xl p-24 rounded-[4rem] text-center border border-dashed border-gray-200">
       <div class="w-20 h-20 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-8 text-gray-300">
          <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm-6 10H6v-2h8v2zm4-4H6v-2h12v2z"/></svg>
       </div>
       <h3 class="text-3xl font-[1000] text-gray-900 mb-2">The Vault is Empty</h3>
       <p class="text-gray-400 font-bold">No clinical assessments have been registered yet.</p>
       <button @click="router.push('/predict')" class="mt-10 px-8 py-4 bg-gray-900 text-white rounded-[2rem] font-black shadow-xl hover:bg-blue-600 transition-all">Start Primary Assessment</button>
    </div>

    <div v-else class="grid gap-6">
      <div v-for="item in store.history" :key="item.id" 
           @click="router.push({ name: 'prediction-result', params: { id: item.id } })"
           class="group bg-white/60 backdrop-blur-2xl p-8 rounded-[3rem] border border-white/50 flex flex-col md:flex-row items-center justify-between cursor-pointer hover:shadow-2xl transition-all hover:-translate-y-2">
        <div class="flex items-center gap-8">
          <div class="w-20 h-20 bg-gradient-to-br from-gray-50 to-gray-100 rounded-[2rem] flex items-center justify-center text-gray-400 group-hover:bg-blue-600 group-hover:text-white transition-all shadow-inner">
            <svg class="w-10 h-10" fill="currentColor" viewBox="0 0 24 24">
              <path :d="diseaseIcons[item.disease_type] || diseaseIcons.default" />
            </svg>
          </div>
          <div>
            <h4 class="text-2xl font-[1000] text-gray-900 capitalize tracking-tight">{{ item.disease_type }} Assessment</h4>
            <div class="flex items-center gap-3 mt-1">
              <span class="text-[10px] font-black text-blue-600 uppercase tracking-widest bg-blue-50 px-2 py-0.5 rounded-full border border-blue-100">AI GEN-2</span>
              <p class="text-[10px] font-black text-gray-400 uppercase tracking-widest">
                {{ new Date(item.created_at).toLocaleDateString(undefined, { month: 'long', day: 'numeric', year: 'numeric' }) }}
              </p>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-12 mt-6 md:mt-0">
          <div class="text-right">
             <div class="text-3xl font-[1000] text-gray-900">{{ item.risk_score }}%</div>
             <div :class="['text-[9px] font-black uppercase tracking-widest px-4 py-1 rounded-full mt-2 border', getRiskColor(item.risk_level)]">
               {{ item.risk_level }} RISK LEVEL
             </div>
          </div>
          <div class="w-12 h-12 rounded-full bg-gray-50 flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition-all">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

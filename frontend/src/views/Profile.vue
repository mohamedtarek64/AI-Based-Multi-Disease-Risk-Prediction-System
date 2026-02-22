<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import { usePredictionStore } from '@/stores/prediction';

const auth = useAuthStore();
const predictions = usePredictionStore();
</script>

<template>
  <div class="p-8 lg:p-16 max-w-5xl mx-auto bg-transparent">
    <div class="bg-white/60 backdrop-blur-3xl rounded-[4rem] shadow-2xl overflow-hidden border border-white/50">
      <!-- Profile Header -->
      <div class="bg-gradient-to-br from-blue-700 via-blue-800 to-indigo-950 p-16 text-white relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
        <div class="absolute bottom-0 left-0 w-48 h-48 bg-blue-400/20 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2"></div>
        
        <div class="flex flex-col md:flex-row items-center gap-10 relative z-10">
          <div class="w-40 h-40 bg-white/20 rounded-[3rem] flex items-center justify-center text-6xl font-[1000] backdrop-blur-xl border border-white/30 shadow-2xl skew-y-3">
            {{ auth.user?.name?.charAt(0) || 'U' }}
          </div>
          <div class="text-center md:text-left">
            <h1 class="text-5xl font-[1000] tracking-tighter mb-2">{{ auth.user?.name || 'Medical User' }}</h1>
            <p class="text-blue-200 font-bold text-xl opacity-80">{{ auth.user?.email }}</p>
            <div class="flex flex-wrap gap-4 mt-8 justify-center md:justify-start">
               <span class="px-5 py-2 bg-white/10 rounded-full text-[10px] font-black uppercase tracking-widest border border-white/20 backdrop-blur-md">Verified Clinical ID</span>
               <span class="px-5 py-2 bg-emerald-500/20 rounded-full text-[10px] font-black uppercase tracking-widest border border-emerald-400/20 backdrop-blur-md text-emerald-200">System Priority: High</span>
            </div>
          </div>
        </div>
      </div>

      <div class="p-16 space-y-16">
        <!-- Account Stats -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
           <div class="p-10 bg-white/80 rounded-[3rem] border border-gray-100 shadow-sm text-center group hover:-translate-y-2 transition-all">
              <div class="w-16 h-16 bg-blue-50 rounded-2xl flex items-center justify-center mx-auto mb-6 text-blue-600 transition-colors group-hover:bg-blue-600 group-hover:text-white">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2m-2 10h-4v4h-2v-4H7v-2h4V7h2v4h4z"/></svg>
              </div>
              <div class="text-4xl font-[1000] text-gray-900">{{ predictions.history.length }}</div>
              <div class="text-[10px] font-black text-gray-400 uppercase tracking-widest mt-2">Clinical Exams</div>
           </div>
           <div class="p-10 bg-white/80 rounded-[3rem] border border-gray-100 shadow-sm text-center group hover:-translate-y-2 transition-all">
              <div class="w-16 h-16 bg-indigo-50 rounded-2xl flex items-center justify-center mx-auto mb-6 text-indigo-600 transition-colors group-hover:bg-indigo-600 group-hover:text-white">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
              </div>
              <div class="text-4xl font-[1000] text-gray-900">Elite</div>
              <div class="text-[10px] font-black text-gray-400 uppercase tracking-widest mt-2">Access Level</div>
           </div>
           <div class="p-10 bg-white/80 rounded-[3rem] border border-gray-100 shadow-sm text-center group hover:-translate-y-2 transition-all">
              <div class="w-16 h-16 bg-rose-50 rounded-2xl flex items-center justify-center mx-auto mb-6 text-rose-600 transition-colors group-hover:bg-rose-600 group-hover:text-white">
                <svg class="w-8 h-8" fill="currentColor" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg>
              </div>
              <div class="text-4xl font-[1000] text-gray-900">Active</div>
              <div class="text-[10px] font-black text-gray-400 uppercase tracking-widest mt-2">Encryption</div>
           </div>
        </div>

        <!-- Settings -->
        <div class="space-y-8">
          <h3 class="text-3xl font-[1000] text-gray-900 tracking-tight">Technical Preferences</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="p-8 bg-white border border-gray-100 rounded-[2.5rem] hover:shadow-xl transition-all cursor-pointer group">
              <div class="flex items-center gap-6">
                <div class="w-14 h-14 bg-gray-50 rounded-2xl flex items-center justify-center text-gray-400 group-hover:bg-blue-600 group-hover:text-white">
                  <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
                </div>
                <div>
                  <h4 class="font-[1000] text-gray-900 text-lg">Alert Protocols</h4>
                  <p class="text-sm text-gray-400 font-bold">Manage clinical notifications</p>
                </div>
              </div>
            </div>

            <div class="p-8 bg-white border border-gray-100 rounded-[2.5rem] hover:shadow-xl transition-all cursor-pointer group">
              <div class="flex items-center gap-6">
                <div class="w-14 h-14 bg-gray-50 rounded-2xl flex items-center justify-center text-gray-400 group-hover:bg-indigo-600 group-hover:text-white">
                  <svg class="w-7 h-7" fill="currentColor" viewBox="0 0 24 24"><path d="M18 8h-1V6c0-2.76-2.24-5-5-5S7 3.24 7 6v2H6c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V10c0-1.1-.9-2-2-2zm-6 9c-1.1 0-2-.9-2-2s.9-2 2-2 2 .9 2 2-.9 2-2 2zm3.1-9H8.9V6c0-1.71 1.39-3.1 3.1-3.1 1.71 0 3.1 1.39 3.1 3.1v2z"/></svg>
                </div>
                <div>
                  <h4 class="font-[1000] text-gray-900 text-lg">Key Management</h4>
                  <p class="text-sm text-gray-400 font-bold">Security & session control</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <button @click="auth.logout()" class="w-full py-8 bg-rose-50 text-rose-600 rounded-[3rem] font-[1000] text-xl border border-rose-100 hover:bg-rose-600 hover:text-white transition-all shadow-2xl shadow-rose-100 active:scale-95">
          Terminate Secure Session
        </button>
      </div>
    </div>
  </div>
</template>

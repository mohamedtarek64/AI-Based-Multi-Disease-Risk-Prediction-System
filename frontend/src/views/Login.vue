<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useToastStore } from '@/stores/toast';
import BrandLogo from '@/components/BrandLogo.vue';

const router = useRouter();
const authStore = useAuthStore();
const toast = useToastStore();
const email = ref('');
const password = ref('');
const error = ref('');
const isLoading = ref(false);

const handleLogin = async () => {
  isLoading.value = true;
  error.value = '';
  try {
    await authStore.login({ email: email.value, password: password.value });
    toast.show('Welcome back! Scientific analysis active.', 'success');
    router.push('/');
  } catch (err: any) {
    error.value = err.response?.data?.message || 'Login failed. Check your credentials.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-[#050505] flex items-center justify-center p-6 selection:bg-cyan-500/30 font-sans overflow-hidden relative">
    
    <!-- High-Tech Animated Background -->
    <div class="absolute inset-0 z-0">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-cyan-500/10 rounded-full blur-[120px] animate-pulse"></div>
      <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"></div>
      <!-- Decorative Grid -->
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:40px_40px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]"></div>
    </div>

    <!-- Centered Compact Terminal -->
    <div class="relative z-10 w-full max-w-[450px] animate-slide-up">
      <!-- Top Brand Accent -->
      <div class="flex flex-col items-center mb-8">
        <div class="w-16 h-16 bg-gradient-to-tr from-cyan-500 to-blue-600 rounded-2xl flex items-center justify-center shadow-[0_0_30px_rgba(6,182,212,0.4)] mb-4 group hover:rotate-12 transition-transform duration-500">
          <BrandLogo size="md" theme="dark" />
        </div>
        <h1 class="text-2xl font-black text-white tracking-[0.2em] uppercase">NEURAL<span class="text-cyan-500">CORE</span></h1>
        <p class="text-[10px] text-slate-500 font-bold tracking-[0.4em] uppercase mt-2">Medical Intelligence Systems</p>
      </div>

      <!-- Main Form Card -->
      <div class="bg-black/40 backdrop-blur-xl rounded-[2.5rem] border border-white/10 p-10 shadow-[0_40px_80px_-15px_rgba(0,0,0,0.8)] relative overflow-hidden group">
        <!-- Floating Glow -->
        <div class="absolute -top-24 -right-24 w-48 h-48 bg-cyan-500/5 rounded-full blur-3xl group-hover:bg-cyan-500/10 transition-colors duration-700"></div>

        <div class="mb-10 text-center">
          <h2 class="text-xl font-bold text-white tracking-tight mb-2">Secure Terminal Access</h2>
          <div class="flex justify-center gap-1">
            <span class="h-1 w-8 bg-cyan-500 rounded-full"></span>
            <span class="h-1 w-2 bg-white/20 rounded-full"></span>
            <span class="h-1 w-2 bg-white/20 rounded-full"></span>
          </div>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-6">
          <div v-if="error" class="p-4 bg-red-950/30 border border-red-500/20 rounded-2xl flex items-center gap-3 animate-shake">
            <div class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></div>
            <p class="text-red-400 text-xs font-black uppercase tracking-tighter">{{ error }}</p>
          </div>

          <div class="space-y-5">
            <div class="space-y-2">
              <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Authorized ID (Email)</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-6 flex items-center text-slate-500 group-focus-within/input:text-cyan-500 transition-colors">
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.206" /></svg>
                </div>
                <input 
                  v-model="email" 
                  type="email" 
                  required 
                  class="w-full pl-14 pr-8 py-5 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-cyan-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700" 
                  placeholder="name@clinical.core" 
                />
              </div>
            </div>

            <div class="space-y-2">
              <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Access Token (Password)</label>
              <div class="relative group/input">
                <div class="absolute inset-y-0 left-6 flex items-center text-slate-500 group-focus-within/input:text-cyan-500 transition-colors">
                  <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                </div>
                <input 
                  v-model="password" 
                  type="password" 
                  required 
                  class="w-full pl-14 pr-8 py-5 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-cyan-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700" 
                  placeholder="••••••••••••" 
                />
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between px-4">
            <label class="flex items-center gap-2 cursor-pointer group">
              <input type="checkbox" class="w-4 h-4 rounded-md border-white/10 bg-white/5 text-cyan-600 focus:ring-cyan-500/20" />
              <span class="text-[10px] font-bold text-slate-500 group-hover:text-slate-300 transition-colors">MAINTAIN SESSION</span>
            </label>
            <a href="#" class="text-[10px] font-black text-cyan-500 hover:text-white transition-colors uppercase tracking-widest">Forgot?</a>
          </div>

          <button 
            type="submit" 
            :disabled="isLoading" 
            class="w-full py-5 bg-white text-black font-black uppercase tracking-widest rounded-2xl shadow-[0_20px_40px_-10px_rgba(255,255,255,0.2)] hover:bg-cyan-500 hover:text-white hover:-translate-y-1 active:scale-95 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3 group/btn"
          >
            <template v-if="isLoading">
              <span class="w-4 h-4 border-2 border-black/30 border-t-black rounded-full animate-spin"></span>
              <span class="text-xs">Processing...</span>
            </template>
            <template v-else>
              <span class="text-xs">Initialize Access</span>
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
            </template>
          </button>
        </form>

        <div class="mt-10 pt-10 border-t border-white/5 text-center">
          <p class="text-slate-500 text-[11px] font-bold tracking-tight">
            New node cluster? 
            <router-link to="/register" class="text-cyan-500 hover:text-white transition-colors ml-1 uppercase tracking-widest font-black">Request Access</router-link>
          </p>
        </div>
      </div>

      <!-- Footer Micro-Info -->
      <div class="mt-8 flex justify-center gap-10 text-[8px] font-black text-slate-600 uppercase tracking-[0.4em]">
        <span>STATION: 01</span>
        <span>LAT: 30.04</span>
        <span>SECURITY: ACTIVE</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes slide-up {
  from { opacity: 0; transform: translateY(40px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-slide-up {
  animation: slide-up 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}

.animate-shake {
  animation: shake 0.4s ease-in-out;
}
</style>

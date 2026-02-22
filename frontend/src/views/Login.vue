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
  <div class="min-h-screen flex items-center justify-center p-4 lg:p-12 overflow-hidden selection:bg-blue-500/30 relative font-sans">
    
    <!-- Immersive Content Area -->
    <div class="relative z-10 w-full max-w-5xl flex flex-col items-center">
      
      <!-- Brand Header (Above Card) -->
      <div class="mb-12 flex flex-col items-center animate-fade-down">
        <BrandLogo size="xl" class="mb-6 drop-shadow-[0_0_30px_rgba(59,130,246,0.5)]" />
        <h1 class="text-4xl font-[1000] text-gray-900 tracking-[0.2em] uppercase text-center">
          Clinical <span class="text-blue-600">Core</span>
        </h1>
        <div class="h-1 w-24 bg-gradient-to-r from-transparent via-blue-500 to-transparent mt-4 opacity-50"></div>
      </div>

      <!-- Main Terminal Card -->
      <div class="w-full bg-slate-950/80 backdrop-blur-3xl rounded-[4rem] shadow-[0_80px_100px_-20px_rgba(0,0,0,0.5)] border border-white/10 flex flex-col lg:flex-row overflow-hidden relative group">
        
        <!-- Interactive Scan Sidebar (Left) -->
        <div class="lg:w-1/3 bg-blue-600/10 border-r border-white/5 p-12 flex flex-col justify-between items-center text-center relative overflow-hidden">
          <div class="absolute inset-0 bg-blue-500/5 animate-pulse"></div>
          
          <div class="relative">
            <div class="w-32 h-32 rounded-full border-2 border-dashed border-blue-400/30 flex items-center justify-center animate-[spin_20s_linear_infinite]">
              <div class="w-24 h-24 rounded-full border border-blue-400/50 flex items-center justify-center animate-[spin_10s_linear_infinite_reverse]">
                <svg class="w-12 h-12 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09a10.116 10.116 0 001.202-2.311 10.12 10.12 0 011.83-3.135m3.45-3.033A10.119 10.119 0 0112 4.903C12 2.196 10.118 0 7.803 0 5.488 0 3.606 2.196 3.606 4.903c0 2.135 1.18 3.992 2.927 4.975z" />
                </svg>
              </div>
            </div>
            <p class="mt-6 text-[10px] font-black text-blue-400 uppercase tracking-[0.3em]">Biometric ID Status</p>
            <p class="text-white font-bold text-xs mt-1">AWAITING INPUT</p>
          </div>

          <div class="space-y-4 w-full">
            <div class="h-0.5 w-full bg-slate-800 rounded-full overflow-hidden">
               <div class="h-full bg-blue-500 w-1/3 animate-[loading_2s_ease-in-out_infinite]"></div>
            </div>
            <p class="text-[8px] text-slate-500 font-black uppercase tracking-widest text-left">Encrypted Path: 0x82...7B</p>
          </div>
        </div>

        <!-- Credential Form (Right) -->
        <div class="flex-1 p-12 lg:p-20">
          <div class="mb-12">
             <h2 class="text-3xl font-[1000] text-white tracking-tighter mb-2">Secure Authentication</h2>
             <p class="text-slate-400 font-medium">Initialize institutional access to the AI cluster.</p>
          </div>

          <form @submit.prevent="handleLogin" class="space-y-8">
            <div v-if="error" class="p-4 bg-rose-500/10 border border-rose-500/20 rounded-2xl flex items-center gap-4 animate-shake">
               <div class="w-8 h-8 rounded-lg bg-rose-500/20 flex items-center justify-center text-rose-500 text-sm">⚠️</div>
               <p class="text-rose-400 font-black text-xs uppercase tracking-tight">{{ error }}</p>
            </div>

            <div class="grid gap-6">
              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-blue-400 transition-colors">Credential Access (Email)</label>
                <div class="relative">
                  <span class="absolute left-6 top-1/2 -translate-y-1/2 text-slate-600 group-focus-within/field:text-blue-400 transition-colors">📧</span>
                  <input 
                    v-model="email" 
                    type="email" 
                    required 
                    class="w-full pl-14 pr-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-blue-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                    placeholder="name@clinical.core"
                  />
                </div>
              </div>

              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-blue-400 transition-colors">Security Token (Password)</label>
                <div class="relative">
                  <span class="absolute left-6 top-1/2 -translate-y-1/2 text-slate-600 group-focus-within/field:text-blue-400 transition-colors">🔑</span>
                  <input 
                    v-model="password" 
                    type="password" 
                    required 
                    class="w-full pl-14 pr-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-blue-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                    placeholder="••••••••••••"
                  />
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between px-4">
              <label class="flex items-center gap-2 cursor-pointer group">
                <input type="checkbox" class="w-4 h-4 rounded border-slate-800 bg-slate-900 text-blue-600 focus:ring-blue-500/20" />
                <span class="text-xs font-bold text-slate-500 group-hover:text-slate-300 transition-colors">Maintain Session</span>
              </label>
              <a href="#" class="text-xs font-black text-blue-500 hover:text-blue-400 transition-colors">Reset Token</a>
            </div>

            <button 
              type="submit" 
              :disabled="isLoading" 
              class="w-full py-6 rounded-[2rem] bg-blue-600 text-white font-[1000] text-xl shadow-[0_20px_40px_-10px_rgba(37,99,235,0.4)] hover:bg-blue-500 hover:-translate-y-1 active:scale-95 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-4 group/btn"
            >
              <span v-if="isLoading" class="w-6 h-6 border-4 border-white/30 border-t-white rounded-full animate-spin"></span>
              <span class="tracking-widest uppercase">{{ isLoading ? 'Authorizing Cluster...' : 'Initialize Access' }}</span>
              <svg v-if="!isLoading" class="w-6 h-6 group-hover:translate-x-2 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
            </button>
          </form>

          <p class="mt-12 text-center text-slate-500 font-bold text-sm">
            Not registered on this station? 
            <router-link to="/register" class="text-blue-500 hover:underline decoration-2 underline-offset-8">Request Enrollment</router-link>
          </p>
        </div>
      </div>

      <!-- Station Meta Footer -->
      <div class="mt-12 flex gap-12 text-[9px] font-black text-slate-400 uppercase tracking-[0.3em]">
         <div class="flex items-center gap-2 pt-1 border-t border-slate-200/10">STATION: PRIMARY-A1</div>
         <div class="flex items-center gap-2 pt-1 border-t border-slate-200/10">ENC: AES-256-GCM</div>
         <div class="flex items-center gap-2 pt-1 border-t border-slate-200/10">LOCATION: DXB-CENTRAL</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes loading {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(300%); }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}

.animate-shake {
  animation: shake 0.4s ease-in-out;
}

@keyframes fade-down {
  from { opacity: 0; transform: translateY(-30px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-down {
  animation: fade-down 1s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useToastStore } from '@/stores/toast';
import BrandLogo from '../components/BrandLogo.vue';

const router = useRouter();
const authStore = useAuthStore();
const toast = useToastStore();
const form = ref({
  name: '',
  email: '',
  password: '',
  password_confirmation: ''
});
const error = ref('');
const isLoading = ref(false);

const handleRegister = async () => {
  isLoading.value = true;
  error.value = '';
  try {
    await authStore.register({
      ...form.value,
      password_confirmation: form.value.password
    });
    toast.show('Account created! Welcome to the AI Portal.', 'success');
    router.push('/');
  } catch (err: any) {
    error.value = err.response?.data?.message || 'Registration failed.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen flex items-center justify-center p-4 lg:p-12 overflow-hidden selection:bg-indigo-500/30 relative font-sans">
    
    <!-- Immersive Content Area -->
    <div class="relative z-10 w-full max-w-5xl flex flex-col items-center">
      
      <!-- Brand Header -->
      <div class="mb-12 flex flex-col items-center animate-fade-down">
        <BrandLogo size="xl" class="mb-6 drop-shadow-[0_0_30px_rgba(79,70,229,0.5)]" />
        <h1 class="text-4xl font-[1000] text-gray-900 tracking-[0.2em] uppercase text-center">
          Enrollment <span class="text-indigo-600">Portal</span>
        </h1>
        <div class="h-1 w-24 bg-gradient-to-r from-transparent via-indigo-500 to-transparent mt-4 opacity-50"></div>
      </div>

      <!-- Main Terminal Card -->
      <div class="w-full bg-slate-950/80 backdrop-blur-3xl rounded-[4rem] shadow-[0_80px_100px_-20px_rgba(0,0,0,0.5)] border border-white/10 flex flex-col lg:flex-row-reverse overflow-hidden relative group">
        
        <!-- Interactive DNA/Identity Sidebar (Right) -->
        <div class="lg:w-1/3 bg-indigo-600/10 border-l border-white/5 p-12 flex flex-col justify-between items-center text-center relative overflow-hidden">
          <div class="absolute inset-0 bg-indigo-500/5 animate-pulse"></div>
          
          <div class="relative">
            <div class="w-32 h-32 flex items-center justify-center relative">
               <div class="absolute inset-0 border-4 border-indigo-400/20 rounded-full animate-[ping_3s_linear_infinite]"></div>
               <div class="w-24 h-24 rounded-full border-2 border-indigo-400/40 flex items-center justify-center animate-[spin_15s_linear_infinite]">
                 <svg class="w-12 h-12 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                   <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a1 1 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z" />
                 </svg>
               </div>
            </div>
            <p class="mt-6 text-[10px] font-black text-indigo-400 uppercase tracking-[0.3em]">Identity Sync</p>
            <p class="text-white font-bold text-xs mt-1 uppercase">Awaiting Sequence</p>
          </div>

          <div class="space-y-4 w-full text-left">
            <div class="flex justify-between text-[8px] font-black text-indigo-300 uppercase tracking-widest pb-1 border-b border-indigo-500/20">
              <span>Security Level</span>
              <span>Class-A</span>
            </div>
            <p class="text-[8px] text-slate-500 font-bold leading-relaxed">System initialized. Awaiting cryptographic identity mapping for new clinical node enrollment.</p>
          </div>
        </div>

        <!-- Enrollment Form (Left) -->
        <div class="flex-1 p-12 lg:p-20">
          <div class="mb-12">
             <h2 class="text-3xl font-[1000] text-white tracking-tighter mb-2">Initialize Registry</h2>
             <p class="text-slate-400 font-medium">Provision your secure credentials for the AI network core.</p>
          </div>

          <form @submit.prevent="handleRegister" class="space-y-6">
            <div v-if="error" class="p-4 bg-rose-500/10 border border-rose-500/20 rounded-2xl flex items-center gap-4 animate-shake">
               <div class="w-8 h-8 rounded-lg bg-rose-500/20 flex items-center justify-center text-rose-500 text-sm">⚠️</div>
               <p class="text-rose-400 font-black text-xs uppercase tracking-tight">{{ error }}</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-indigo-400 transition-colors">Legal Name</label>
                <input 
                  v-model="form.name" 
                  type="text" 
                  required 
                  class="w-full px-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-indigo-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                  placeholder="John Doe"
                />
              </div>

              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-indigo-400 transition-colors">Access Email</label>
                <input 
                  v-model="form.email" 
                  type="email" 
                  required 
                  class="w-full px-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-indigo-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                  placeholder="name@clinical.core"
                />
              </div>

              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-indigo-400 transition-colors">Security Token</label>
                <input 
                  v-model="form.password" 
                  type="password" 
                  required 
                  class="w-full px-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-indigo-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                  placeholder="••••••••••••"
                />
              </div>

              <div class="space-y-2 group/field">
                <label class="block text-[10px] font-black text-slate-500 uppercase tracking-widest pl-4 group-focus-within/field:text-indigo-400 transition-colors">Token Verification</label>
                <input 
                  v-model="form.password_confirmation" 
                  type="password" 
                  required 
                  class="w-full px-8 py-5 rounded-[2rem] bg-slate-900/50 border border-white/5 focus:border-indigo-500/50 focus:bg-slate-900 outline-none transition-all font-bold text-white placeholder:text-slate-700"
                  placeholder="••••••••••••"
                />
              </div>
            </div>

            <div class="py-4">
              <label class="flex items-start gap-3 cursor-pointer group">
                <input type="checkbox" required class="mt-1 w-4 h-4 rounded border-slate-800 bg-slate-900 text-indigo-600 focus:ring-indigo-500/20" />
                <span class="text-[10px] font-bold text-slate-500 leading-relaxed uppercase tracking-wider">
                  I agree to the <span class="text-indigo-400">Privacy Protocol</span> and <span class="text-indigo-400">Clinical Terms</span>.
                </span>
              </label>
            </div>

            <button 
              type="submit" 
              :disabled="isLoading" 
              class="w-full py-6 rounded-[2rem] bg-indigo-600 text-white font-[1000] text-xl shadow-[0_20px_40px_-10px_rgba(79,70,229,0.4)] hover:bg-indigo-500 hover:-translate-y-1 active:scale-95 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-4 group/btn"
            >
              <span v-if="isLoading" class="w-6 h-6 border-4 border-white/30 border-t-white rounded-full animate-spin"></span>
              <span class="tracking-widest uppercase">{{ isLoading ? 'Processing...' : 'Register Identity' }}</span>
              <svg v-if="!isLoading" class="w-6 h-6 group-hover:translate-x-2 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M13 7l5 5m0 0l-5 5m5-5H6" /></svg>
            </button>
          </form>

          <p class="mt-10 text-center text-slate-500 font-bold text-sm">
            Already have an active identity? 
            <router-link to="/login" class="text-indigo-400 hover:underline decoration-2 underline-offset-8">Access Terminal</router-link>
          </p>
        </div>
      </div>

      <!-- Station Meta Footer -->
      <div class="mt-12 flex flex-wrap justify-center gap-8 text-[9px] font-black text-slate-400 uppercase tracking-[0.3em] opacity-50">
         <div class="flex items-center gap-2">UID_MAPPING: ACTIVE</div>
         <div class="flex items-center gap-2">NODE_HASH: F82A...92C</div>
         <div class="flex items-center gap-2">PROTO: TRON-SEC-01</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

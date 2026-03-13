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
  <div class="min-h-screen bg-[#050505] flex items-center justify-center p-6 selection:bg-indigo-500/30 font-sans overflow-hidden relative">
    
    <!-- High-Tech Animated Background -->
    <div class="absolute inset-0 z-0">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-indigo-500/10 rounded-full blur-[120px] animate-pulse"></div>
      <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20"></div>
      <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:40px_40px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_100%,#000_70%,transparent_100%)]"></div>
    </div>

    <!-- Centered Compact Terminal -->
    <div class="relative z-10 w-full max-w-[500px] animate-slide-up">
      <!-- Top Brand Accent -->
      <div class="flex flex-col items-center mb-8">
        <div class="w-16 h-16 bg-gradient-to-tr from-indigo-500 to-purple-600 rounded-2xl flex items-center justify-center shadow-[0_0_30px_rgba(99,102,241,0.4)] mb-4">
          <BrandLogo size="md" theme="dark" />
        </div>
        <h1 class="text-2xl font-black text-white tracking-[0.2em] uppercase">REGISTRY<span class="text-indigo-500">CORE</span></h1>
        <p class="text-[10px] text-slate-500 font-bold tracking-[0.4em] uppercase mt-2">Initialize Clinical Node</p>
      </div>

      <!-- Main Form Card -->
      <div class="bg-black/40 backdrop-blur-xl rounded-[2.5rem] border border-white/10 p-10 shadow-[0_40px_80px_-15px_rgba(0,0,0,0.8)] relative overflow-hidden group">
        <div class="absolute -top-24 -left-24 w-48 h-48 bg-indigo-500/5 rounded-full blur-3xl group-hover:bg-indigo-500/10 transition-colors duration-700"></div>

        <div class="mb-8 text-center">
          <h2 class="text-xl font-bold text-white tracking-tight mb-2">Node Enrollment</h2>
          <div class="flex justify-center gap-1">
            <span class="h-1 w-2 bg-white/20 rounded-full"></span>
            <span class="h-1 w-8 bg-indigo-500 rounded-full"></span>
            <span class="h-1 w-2 bg-white/20 rounded-full"></span>
          </div>
        </div>

        <form @submit.prevent="handleRegister" class="space-y-5">
          <div v-if="error" class="p-4 bg-red-950/30 border border-red-500/20 rounded-2xl flex items-center gap-3 animate-shake">
            <div class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></div>
            <p class="text-red-400 text-xs font-black uppercase tracking-tighter">{{ error }}</p>
          </div>

          <div class="grid grid-cols-1 gap-4">
            <div class="space-y-1">
              <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Full Name</label>
              <input 
                v-model="form.name" 
                type="text" 
                required 
                class="w-full px-6 py-4 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-indigo-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700 sm:text-sm" 
                placeholder="Clinical Supervisor" 
              />
            </div>

            <div class="space-y-1">
              <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Authorized Email</label>
              <input 
                v-model="form.email" 
                type="email" 
                required 
                class="w-full px-6 py-4 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-indigo-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700 sm:text-sm" 
                placeholder="name@hospital.org" 
              />
            </div>

            <div class="grid grid-cols-2 gap-4">
              <div class="space-y-1">
                <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Token</label>
                <input 
                  v-model="form.password" 
                  type="password" 
                  required 
                  class="w-full px-6 py-4 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-indigo-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700 sm:text-sm" 
                  placeholder="••••••" 
                />
              </div>
              <div class="space-y-1">
                <label class="text-[9px] font-black text-slate-500 uppercase tracking-[0.2em] ml-4">Verify</label>
                <input 
                  v-model="form.password_confirmation" 
                  type="password" 
                  required 
                  class="w-full px-6 py-4 bg-white/5 border border-white/5 rounded-2xl text-white font-bold outline-none focus:border-indigo-500/50 focus:bg-white/10 transition-all placeholder:text-slate-700 sm:text-sm" 
                  placeholder="••••••" 
                />
              </div>
            </div>
          </div>

          <div class="py-2">
            <label class="flex items-center gap-3 cursor-pointer group">
              <input type="checkbox" required class="w-4 h-4 rounded-md border-white/10 bg-white/5 text-indigo-600 focus:ring-indigo-500/20" />
              <span class="text-[10px] font-bold text-slate-500 group-hover:text-slate-300 transition-colors uppercase tracking-widest">Agree to Data Protocols</span>
            </label>
          </div>

          <button 
            type="submit" 
            :disabled="isLoading" 
            class="w-full py-5 bg-white text-black font-black uppercase tracking-widest rounded-2xl shadow-[0_20px_40px_-10px_rgba(255,255,255,0.2)] hover:bg-indigo-600 hover:text-white hover:-translate-y-1 active:scale-95 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3 group/btn"
          >
            <template v-if="isLoading">
              <span class="w-4 h-4 border-2 border-black/30 border-t-black rounded-full animate-spin"></span>
              <span class="text-xs">UPLOADING...</span>
            </template>
            <template v-else>
              <span class="text-xs">Enroll Node</span>
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M12 4v16m8-8H4" /></svg>
            </template>
          </button>
        </form>

        <div class="mt-8 pt-8 border-t border-white/5 text-center">
          <p class="text-slate-500 text-[11px] font-bold tracking-tight">
            Active identity detected? 
            <router-link to="/login" class="text-indigo-500 hover:text-white transition-colors ml-1 uppercase tracking-widest font-black">Return to Terminal</router-link>
          </p>
        </div>
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

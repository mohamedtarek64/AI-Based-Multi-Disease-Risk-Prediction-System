import { defineStore } from 'pinia';
import { ref } from 'vue';

export type ToastType = 'success' | 'error' | 'info' | 'warning';

interface Toast {
    id: number;
    message: string;
    type: ToastType;
}

export const useToastStore = defineStore('toast', () => {
    const toasts = ref<Toast[]>([]);
    let nextId = 1;

    function show(message: string, type: ToastType = 'info') {
        const id = nextId++;
        toasts.value.push({ id, message, type });
        setTimeout(() => {
            remove(id);
        }, 5000);
    }

    function remove(id: number) {
        toasts.value = toasts.value.filter(t => t.id !== id);
    }

    return { toasts, show, remove };
});

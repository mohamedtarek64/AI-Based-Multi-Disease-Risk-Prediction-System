import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'
import type { SavedPrediction } from '@/types/prediction'

export const usePredictionStore = defineStore('prediction', () => {
    const currentPrediction = ref<SavedPrediction | null>(null)
    const history = ref<SavedPrediction[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)

    const api = axios.create({
        baseURL: 'http://localhost:8000/api/v1',
    })

    async function predictDisease(disease: string, data: any) {
        loading.value = true
        error.value = null
        try {
            const response = await api.post(`/predict/${disease}`, data)
            currentPrediction.value = response.data.data
            return response.data.data
        } catch (err: any) {
            error.value = err.response?.data?.message || 'Failed to get prediction'
            throw err
        } finally {
            loading.value = false
        }
    }

    async function fetchHistory() {
        try {
            const response = await api.get('/predictions/history')
            history.value = response.data.data
        } catch (err) {
            console.error('History fetch failed')
        }
    }

    async function fetchPredictionById(id: string) {
        loading.value = true
        try {
            const response = await api.get(`/predictions/${id}`)
            currentPrediction.value = response.data.data
            return response.data.data
        } catch (err) {
            console.error('Fetch by ID failed')
        } finally {
            loading.value = false
        }
    }

    return {
        currentPrediction,
        history,
        loading,
        error,
        predictDisease,
        fetchHistory,
        fetchPredictionById
    }
})

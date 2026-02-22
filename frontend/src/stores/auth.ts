import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'
import type { User, LoginCredentials, RegisterData } from '../types/auth'

export const useAuthStore = defineStore('auth', () => {
    const user = ref<User | null>(JSON.parse(localStorage.getItem('user') || 'null'))
    const token = ref<string | null>(localStorage.getItem('token'))

    const isAuthenticated = computed(() => !!token.value)

    const api = axios.create({
        baseURL: 'http://localhost:8000/api/v1',
    })

    // Add interceptor to include token
    api.interceptors.request.use((config) => {
        if (token.value) {
            config.headers.Authorization = `Bearer ${token.value}`
        }
        return config
    })

    async function login(credentials: LoginCredentials) {
        try {
            const response = await api.post('/login', credentials)
            token.value = response.data.token
            user.value = response.data.user
            localStorage.setItem('token', token.value!)
            localStorage.setItem('user', JSON.stringify(user.value))
            return response.data
        } catch (error) {
            throw error
        }
    }

    async function register(data: RegisterData) {
        try {
            const response = await api.post('/register', data)
            token.value = response.data.token
            user.value = response.data.user
            localStorage.setItem('token', token.value!)
            localStorage.setItem('user', JSON.stringify(user.value))
            return response.data
        } catch (error) {
            throw error
        }
    }

    async function logout() {
        token.value = null
        user.value = null
        localStorage.removeItem('token')
        localStorage.removeItem('user')
    }

    return {
        user,
        token,
        isAuthenticated,
        login,
        register,
        logout
    }
})

import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'dashboard',
            component: Dashboard,
            meta: { requiresAuth: true }
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/Login.vue'),
            meta: { guest: true }
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/Register.vue'),
            meta: { guest: true }
        },
        {
            path: '/profile',
            name: 'profile',
            component: () => import('../views/Profile.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/history',
            name: 'history',
            component: () => import('../views/History.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict',
            name: 'predict-select',
            component: () => import('../views/predictions/SelectDisease.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/diabetes',
            name: 'predict-diabetes',
            component: () => import('../views/predictions/DiabetesForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/heart',
            name: 'predict-heart',
            component: () => import('../views/predictions/HeartDiseaseForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/cancer',
            name: 'predict-cancer',
            component: () => import('../views/predictions/CancerForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/digestive',
            name: 'predict-digestive',
            component: () => import('../views/predictions/DigestiveForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/respiratory',
            name: 'predict-respiratory',
            component: () => import('../views/predictions/RespiratoryForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/hypertension',
            name: 'predict-hypertension',
            component: () => import('../views/predictions/HypertensionForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/predict/kidney',
            name: 'predict-kidney',
            component: () => import('../views/predictions/KidneyDiseaseForm.vue'),
            meta: { requiresAuth: true }
        },
        {
            path: '/result/:id',
            name: 'prediction-result',
            component: () => import('../views/predictions/PredictionResult.vue'),
            meta: { requiresAuth: true }
        }
    ]
})

router.beforeEach((to, from, next) => {
    const auth = useAuthStore()

    if (to.meta.requiresAuth && !auth.isAuthenticated) {
        next('/login')
    } else if (to.meta.guest && auth.isAuthenticated) {
        next('/')
    } else {
        next()
    }
})

export default router

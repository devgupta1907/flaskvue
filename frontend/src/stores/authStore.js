import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore('auth', () => {
    const token = ref(localStorage.getItem('token') || null)
    const usertype = ref(localStorage.getItem('usertype') || null)

    const login = async (email, password, userType) => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/login/${userType}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            })

            const data = await response.json()

            if (!response.ok) {
                throw new Error(data.message)
            }
            token.value = data.access_token
            usertype.value = data.usertype

            localStorage.setItem('token', token.value)
            localStorage.setItem('usertype', usertype.value)
        } catch (error) {
            console.log('Login Failed: ', error.message)
            throw error
        }
    }

    return { token, usertype, login }
})
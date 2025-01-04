// composables/useAuth.js
import { ref } from 'vue';

const isAuthenticated = ref(false);  // Track if the user is authenticated
const userRole = ref('');  // Track the user's role (e.g., 'admin', 'user')

// A function to simulate login check
const checkAuth = () => {
  // Retrieve authentication status and role from localStorage or Vuex
  const token = localStorage.getItem('token');
  isAuthenticated.value = token ? true : false;
  userRole.value = localStorage.getItem('role') || '';  // Retrieve user role from localStorage
};

export function useAuth() {
  return {
    isAuthenticated,
    userRole,
    checkAuth,
  };
}

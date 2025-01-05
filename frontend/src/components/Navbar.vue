<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Paddu Housy</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <!-- Not Logged In -->
          <template v-if="!isLoggedIn">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'CategoriesUser' }">Categories</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'ServicesUser' }">Services</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Register' }">Register</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'Login' }">Login</router-link>
            </li>
          </template>

          <!-- Logged In as Admin -->
          <template v-else-if="role === 'admin'">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'CategoriesAdmin' }">Categories</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'ServicesAdmin' }">Services</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'CustomersAdmin' }">Customers</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'ProfessionalsAdmin' }">Professionals</router-link>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" @click.prevent="logout">Logout</a>
            </li>
          </template>

          <!-- Logged In and Not Admin -->
          <template v-else>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'CategoriesUser' }">Categories</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'ServicesUser' }">Services</router-link>
            </li>
            <li class="nav-item">
              <router-link v-if="role === 'customer'" class="nav-link" :to="{ name: 'CustomerDashboard' }">Dashboard</router-link>
              <router-link v-if="role === 'professional'" class="nav-link" :to="{ name: 'ProfessionalDashboard' }">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <span class="nav-link">{{ role }} {{ email }}</span>
            </li>
            <li class="nav-item">
              <a href="#" class="nav-link" @click.prevent="logout">Logout</a>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>


<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

// Router instance
const router = useRouter();

// Reactive state from localStorage
const email = ref(localStorage.getItem('email'));
const role = ref(localStorage.getItem('role'));

// Compute `isLoggedIn` dynamically
const isLoggedIn = computed(() => !!email.value && !!role.value);

// Sync localStorage changes
const updateLocalStorage = () => {
  email.value = localStorage.getItem('email');
  role.value = localStorage.getItem('role');

  // Redirect to login if `localStorage` is cleared
  if (!email.value || !role.value) {
    // isLoggedIn.value = false; // Ensure UI updates
    router.push('/login'); // Redirect to login
  }
};

// Add storage event listener
onMounted(() => {
  window.addEventListener('storage', updateLocalStorage);
  updateLocalStorage();
});

// Remove storage event listener on component unmount
onUnmounted(() => {
  window.removeEventListener('storage', updateLocalStorage);
});

// Logout function
const logout = () => {
  localStorage.clear();
  window.dispatchEvent(new Event('storage')); // Trigger reactive updates
  router.push('/login');
};
</script>


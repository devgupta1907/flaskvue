<template>
    <div class="container">
          <h3 class="text-center display-5 mt-2">FlaskVue Login Page</h3>
          <div class="row">
          </div>
    </div>

    <div class="container mt-5">
      <div class="row justify-content-center">
  
        <div class="col-md-6">
          <form method="post" @submit.prevent="loginUser">
  
            <div class="mb-3">
              <label for="email" class="form-label">Email address</label>
              <input type="email" v-model="email" class="form-control" name="email" required>
              <!-- <div id="emailHelp" class="form-text">This email will be required for login.</div> -->
            </div>
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" name="password" required>
            </div>
  
            <div class="mb-3">
              <label for="usertype" class="form-label">Usertype</label>
              <select v-model="userType" class="form-control" required>
                <option value="" disabled>Select Usertype</option>
                <option value="customer">Customer</option>
                <option value="professional">Professional</option>
              </select>
            </div>
  
            <div class="mb-3">
              <button type="submit" class="btn btn-warning">Register</button>
            </div>
            
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import { useAuthStore } from '@/stores/authStore';

    const authStore = useAuthStore()

    const email = ref('')
    const password = ref('')
    const userType = ref('')
  
    
    const loginUser = async () => {
      try {
        await authStore.login(email.value, password.value, userType.value)
        alert(`Login Successful as ${ userType.value }`)
      } catch (error) {
        alert(`Error: ${error.message}`)
      }
      
    }
  
    const professionalLogin = async (loginDetails) => {
      try {
        const response = await fetch('http://localhost:5000/login/professional', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(loginDetails)
        })
  
        const messageResponse = await response.json()
        if (!response.ok) {
          throw new Error(messageResponse.message)
        }
        const token = messageResponse.access_token;
        localStorage.setItem('token', token);
        console.log(token)

        alert(messageResponse.message)
      } catch (error) {
        alert(error.message)
      } finally {
        email.value = ""
        password.value = ""
        userType.value = ""
      }
    }
  
    const customerLogin = async (loginDetails) => {
      try {
        const response = await fetch('http://localhost:5000/login/customer', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(loginDetails)
        })
  
        const messageResponse = await response.json()
        if (!response.ok) {
          throw new Error(messageResponse.message)
        }
        const token = messageResponse.access_token;
        localStorage.setItem('token', token);

        alert(messageResponse.message)
      } catch (error) {
        alert(error.message)
      } finally {
        email.value = ""
        password.value = ""
        userType.value = ""
      }
    }
  </script>
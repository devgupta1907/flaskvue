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
            </div>
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input type="password" v-model="password" class="form-control" name="password" required>
            </div>
  
            <div class="mb-3">
              <button type="submit" class="btn btn-warning">Login</button>
            </div>
            
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import { useRouter } from 'vue-router';

    const router = useRouter()

    const email = ref('')
    const password = ref('')
  
    const loginUser = async () => {
      try {
        const response = await fetch('http://localhost:5000/login', {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            email: email.value,
            password: password.value
          })
        })
  
        const messageResponse = await response.json()
        if (!response.ok) {
          throw new Error(messageResponse.message)
        }

        localStorage.setItem('token', messageResponse.token);
        localStorage.setItem('role', messageResponse.role)
        localStorage.setItem('email', messageResponse.email)

        window.dispatchEvent(new Event('storage'))
        console.log(messageResponse)

        alert("Login Successful!")
        messageResponse.role === 'admin' ? 
          router.push({ name: 'AdminDashboard' }) : 
          router.push({ name: 'CategoriesUser' })

      } catch (error) {
        alert(error.message)
      } finally {
        email.value = ""
        password.value = ""
      }
    }
  
    
  </script>
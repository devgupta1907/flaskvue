<template>
  <div class="container">
        <h3 class="text-center display-5 mt-2">FlaskVue Registration Page</h3>
        <div class="row">
        </div>
  </div>
  <div class="container mt-5">
    <div class="row justify-content-center">

      <div class="col-md-6">
        <form method="post" @submit.prevent="registerUser">
          <div class="mb-3">
            <label for="name" class="form-label">Your Name</label>
            <input type="text" v-model="name" class="form-control" name="name" required>
            <div id="nameHelp" class="form-text">Please enter your full name here.</div>
          </div>

          <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" v-model="email" class="form-control" name="email" required>
            <div id="emailHelp" class="form-text">This email will be required for login.</div>
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

          <div v-if="userType === 'professional'" class="mb-3">
            <label for="workexp" class="form-label">Work Experience</label>
            <input v-model="workExp" @input="validateWorkExp"  type="number" class="form-control" min="0" max="20" required />
            <div id="workExpHelp" class="form-text text-danger">{{ workExpError }}</div>
          </div>

          <div v-if="userType === 'customer'" class="mb-3">
            <label for="pincode" class="form-label">Pincode</label>
            <input v-model="pincode" type="number" class="form-control" required>
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

  const name = ref('')
  const email = ref('')
  const password = ref('')
  const userType = ref('')
  const pincode = ref()
  const workExp = ref()
  const workExpError = ref('')

  const validateWorkExp = () => {
    if (workExp.value < 0) {
      workExpError.value = "Experience cannot be negative"
    } else if (workExp.value > 20) {
      workExpError.value = "Experience greater than 20 years is not allowed."
    } else {
      workExpError.value = ""
    }
  }

  const registerUser = async () => {
    const registrationDetails = {
      name: name.value,
      email: email.value,
      password: password.value
    }
    if (userType.value === "professional") {
      registrationDetails.work_exp = workExp.value
      await professionalRegistration(registrationDetails)
    } else if (userType.value === "customer") {
      registrationDetails.pincode = pincode.value
      await customerRegistration(registrationDetails)
    }
  }

  const professionalRegistration = async (registrationDetails) => {
    try {
      const response = await fetch('http://localhost:5000/register/professional', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(registrationDetails)
      })

      const messageResponse = await response.json()
      if (!response.ok) {
        throw new Error(messageResponse.message)
      }
      alert(messageResponse.message)
    } catch (error) {
      alert(error.message)
    } finally {
      name.value = ""
      email.value = ""
      password.value = ""
      userType.value = ""
      workExp.value = ""
    }
  }

  const customerRegistration = async (registrationDetails) => {
    try {
      const response = await fetch('http://localhost:5000/register/customer', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(registrationDetails)
      })

      const messageResponse = await response.json()
      if (!response.ok) {
        throw new Error(messageResponse.message)
      }
      alert(messageResponse.message)
    } catch (error) {
      alert(error.message)
    } finally {
      name.value = ""
      email.value = ""
      password.value = ""
      userType.value = ""
      pincode.value = ""
    }
  }
</script>
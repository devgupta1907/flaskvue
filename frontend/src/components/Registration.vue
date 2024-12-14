<template>

	<div class="container">
		<h3 class="text-center display-5 mt-2">FlaskVue Registration Page</h3>
  	</div>

    <div class="container mt-5">
        <div class="row justify-content-center">
			<div class="col-md-6">
				<form @submit.prevent="handleSubmit">
					<div class="mb-3">
						<label for="name" class="form-label">Your Name</label>
						<input type="text" v-model="name" class="form-control" required />
					</div>
  
					<div class="mb-3">
						<label for="email" class="form-label">Email address</label>
						<input type="email" v-model="email" class="form-control" required />
					</div>
  
					<div class="mb-3">
						<label for="password" class="form-label">Password</label>
						<input type="password" v-model="password" class="form-control" required />
					</div>
  
					<div class="mb-3">
						<label for="usertype" class="form-label">User Type</label>
						<select v-model="userType" class="form-control" required>
							<option value="" disabled>Select User Type</option>
							<option value="customer">Customer</option>
							<option value="professional">Professional</option>
						</select>
					</div>
  
					<!-- Render the dynamic child component -->
					<component
						:is="userComponent"
						v-model="userSpecificData"
            @validationStatus="isValid = $event"
					/>
  
        			<button type="submit" class="btn btn-warning" :disabled="!isValid">Register</button>
      			</form>
			</div>
		</div> 
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import CustomerRegistration from './CustomerRegistration.vue';
  import ProfessionalRegistration from './ProfessionalRegistration.vue';

  const name = ref('');
  const email = ref('');
  const password = ref('');
  const userType = ref('');
  const isValid = ref(false)
  const userSpecificData = ref({});
  

  const userComponent = computed(() => {
    if (userType.value === 'customer') return CustomerRegistration;
    if (userType.value === 'professional') return ProfessionalRegistration;
    return null;
  });
  
  const handleSubmit = async () => {
    const payload = {
      name: name.value,
      email: email.value,
      password: password.value,
      ...userSpecificData.value,
    };
  
    let endpoint = '';
    if (userType.value === 'customer') endpoint = '/register/customer';
    if (userType.value === 'professional') endpoint = '/register/professional';
  
    try {
      const response = await fetch(`http://localhost:5000${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
  
      const result = await response.json();
      if (!response.ok) throw new Error(result.message);
      alert(result.message);
    } catch (error) {
      alert(error.message);
    }
  };
  </script>
  
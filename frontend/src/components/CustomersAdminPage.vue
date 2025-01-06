<template>
  <div class="m-4">
    <h3 class="display-6 lead">Customers</h3>
  </div>

  <Search placeholder="Search customers" @search="filterCustomers" />

  <div class="container">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Pincode</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="customer in filteredCustomers" :key="customer.user_id">
          <th scope="row">{{ customer.user_id }}</th>
          <td>{{ customer.name }}</td>
          <td>{{ customer.email }}</td>
          <td>{{ customer.pincode }}</td>
          <td v-if="!customer.isBlocked">
            <BlockUser :userId="customer.user_id" @update="updateCustomerStatus(customer.user_id, true)"/>
          </td>
          <td v-else>
            <UnblockUser :userId="customer.user_id" @update="updateCustomerStatus(customer.user_id, false)" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import BlockUser from './BlockUser.vue';
  import Search from './Search.vue';
  import { useCustomers } from '@/composables/useCustomers';
  import UnblockUser from './UnblockUser.vue';

  const { customers, fetchCustomers } = useCustomers();

  const searchQuery = ref('');
  const filterCustomers = query => {
    searchQuery.value = query;
  }

  const filteredCustomers = computed(() =>
    customers.value.filter(customer => 
      customer.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      customer.email.toLowerCase().includes(searchQuery.value.toLowerCase())
    )
  )

  const updateCustomerStatus = (userId, isBlocked) => {
  const customer = customers.value.find(c => c.user_id === userId);
  if (customer) {
    customer.isBlocked = isBlocked;
  }}


  onMounted(() => {
    fetchCustomers();
  });
</script>

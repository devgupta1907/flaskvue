<template>
  <div class="m-4">
    <h3 class="display-6 lead">Professionals</h3>
  </div>

  <div class="container">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Work Exp</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="professional in professionals" :key="professional.user_id">
          <th scope="row">{{ professional.user_id }}</th>
          <td>{{ professional.name }}</td>
          <td>{{ professional.email }}</td>
          <td>{{ professional.work_exp }}</td>
          <td v-if="!professional.isBlocked">
            <BlockUser :userId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, true)"/>
          </td>
          <td v-else>
            <UnblockUser :userId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, false)" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue';
  import BlockUser from './BlockUser.vue';
  import { useProfessionals } from '@/composables/useProfessionals';
  import UnblockUser from './UnblockUser.vue';

  const { professionals, fetchProfessionals } = useProfessionals();
  

  const updateProfessionalstatus = (userId, isBlocked) => {
  const professional = professionals.value.find(c => c.user_id === userId);
  if (professional) {
    professional.isBlocked = isBlocked;
  }};


  onMounted(() => {
    fetchProfessionals();
  });
</script>

<template>
  <div class="m-4">
    <h3 class="display-6 lead">Professionals</h3>
  </div>

  <Search placeholder="Search professionals" @search="filterProfessionals" />

  <div class="container">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Work Exp</th>
          <th scope="col">Status</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="professional in filteredProfessionals" :key="professional.user_id">
          <th scope="row">{{ professional.user_id }}</th>
          <td>{{ professional.name }}</td>
          <td>{{ professional.email }}</td>
          <td>{{ professional.work_exp }}</td>
          <td>{{ professional.status }}</td>
          <td v-if="professional.status === 'ACTIVE'">
            <BlockUser :userId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, 'BLOCKED', true)"/>
          </td>
          <td v-if="professional.status === 'PENDING'">
            <FlagProfessional :professionalId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, 'FLAGGED', false)"/>
            <ActivateProfessional :professionalId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, 'ACTIVE', false)"/>
          </td>
          <td v-if="professional.status === 'FLAGGED'">
            <ActivateProfessional :professionalId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, 'ACTIVE', false)"/>
          </td>
          <td v-if="professional.status === 'BLOCKED'">
            <UnblockUser :userId="professional.user_id" @update="updateProfessionalstatus(professional.user_id, 'ACTIVE', false)" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import { useProfessionals } from '@/composables/useProfessionals';
  import BlockUser from './BlockUser.vue';
  import UnblockUser from './UnblockUser.vue';
  import FlagProfessional from './FlagProfessional.vue';
  import ActivateProfessional from './ActivateProfessional.vue';
  import Search from './Search.vue';

  const { professionals, fetchProfessionals } = useProfessionals();
  
  const searchQuery = ref('');
  const filterProfessionals = query => {
    searchQuery.value = query;
  }

  const filteredProfessionals = computed(() =>
    professionals.value.filter(professional => 
      professional.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      professional.email.toLowerCase().includes(searchQuery.value.toLowerCase())
    )
  )

  const updateProfessionalstatus = (userId, newStatus, wannaBlock) => {
    const professional = professionals.value.find(c => c.user_id === userId);
    if (professional) {
      professional.isBlocked = wannaBlock;
      professional.status = newStatus
    }
  }


  onMounted(() => {
    fetchProfessionals();
  });
</script>

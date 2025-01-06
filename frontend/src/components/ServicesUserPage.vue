<template>

  <div class="container mt-4">
    <h3 class="text-center display-5 my-2">MadyPro Services</h3>
    <div class="row">
      <div class="text-center">
        <p class="lead">Be It Home Decor, Laptop Repair, or Beauty & Grooming - We Provide What You Want!</p>
      </div>
    </div>
  </div>

  <Search placeholder="Search services" @search="filterServices" />
  
  <div class="container mt-4">
    <p class="lead">- found <b>{{ finalFiltered.length }}</b> service(s)</p>
    <div class="row">
      <div class="col-md-3 mb-4" v-for="service in finalFiltered" :key="service.id">
        <div class="card border border-0">
          <div class="card-body shadow rounded">
            <h5 class="card-title text-center">
              {{ service.name }}
            </h5>
            <div class="text-center">
              <router-link
                class="btn btn-warning"
                :to="{ name: 'ProfessionalsByServiceUser', 
                      params: { serviceId: service.id }}">
                Choose Professionals
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
<script setup>
  import { onMounted, ref, computed, watch } from 'vue';
  import { useRoute } from 'vue-router';
  import { useServices } from '@/composables/useServices';
  import Search from './Search.vue';
  
  const { services, fetchServices } = useServices();
  const route = useRoute();
  
  const categoryId = route.query.category

  const searchQuery = ref('');
    const filterServices = query => {
        searchQuery.value = query;
    }
  const filteredServices = computed(() => {
    if (!categoryId) return services.value;
    return services.value.filter(service => service.category_id === parseInt(categoryId))
  });

  const finalFiltered = computed(() => {
    return filteredServices.value.filter(service => 
            service.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
  })

  onMounted(() => {
    fetchServices()
  })

</script>
  
<template>

    <div class="container mt-4">
      <h3 class="text-center display-5 my-2">MadyPro Professionals</h3>
      <div class="row">
        <div class="text-center">
          <p class="lead">Be It Home Decor, Laptop Repair, or Beauty & Grooming - We Provide What You Want!</p>
        </div>
      </div>
    </div>
    
    <div class="container mt-4">
      <p class="lead">- found <b>{{ professionals.length }}</b> professionals(s)</p>
      <div class="row">
        <div class="col-md-3 mb-4" v-for="professional in professionals" :key="professional.id">
          <div class="card border border-0">
            <div class="card-body shadow rounded">
              <h5 class="card-title text-center">
                {{ professional.name }}
              </h5>
              <div class="text-center">
                <a href="#" class="btn btn-warning">Book Now</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
    import { onMounted } from 'vue';
    import { useProfessionals } from '@/composables/useProfessionals';
    import { useRoute } from 'vue-router';

    const { professionals } = useProfessionals()
    
    const route = useRoute()
    const service_id = route.params.serviceId

    onMounted(() => {
        useProfessionals().fetchProfessionalsByService(service_id)
    })
</script>
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
      <p class="lead">- found <b>{{ professionalsByService.length }}</b> professional(s)</p>
      <div class="row">
        <div class="col-md-3 mb-4" v-for="professional in professionalsByService" :key="professional.id">
          <div class="card border border-0">
            <div class="card-body shadow rounded">
              <h5 class="card-title text-center">
                {{ professional.name }}
              </h5>
              <p class="card-text text-center">
                <span v-if="professional.rating === 0">
                  Be the first to hire this professional
                </span>
                <span v-else>
                  {{ '💛'.repeat(Math.round(professional.rating)) }}
                </span>
              </p>
              <div class="text-center">
                <button class="btn btn-warning" @click="createServiceRequest(service_id, professional.id)">Book Now</button>
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
    import { useServiceRequests } from '@/composables/useServiceRequests';
    import { useRoute, useRouter } from 'vue-router';


    const { professionalsByService } = useProfessionals()
    
    const router = useRouter()
    const route = useRoute()
    const service_id = route.params.serviceId

    const createServiceRequest = async (service_id, professional_id) => {
      try {
        await useServiceRequests().createServiceRequest(service_id, professional_id)
        alert('Service request created successfully')

        router.push({ name: 'ServicesUser' })
      } catch (error) {
        alert(error.message)
      }
      

    }

    onMounted(() => {
        useProfessionals().fetchProfessionalsByService(service_id)
    })
</script>
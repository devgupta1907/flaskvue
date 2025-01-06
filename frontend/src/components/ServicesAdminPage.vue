<template>
    <div class="d-flex justify-content-between align-items-center m-4">
        <h3 class="display-6 lead">Services</h3>
        <div>
            <router-link class="btn btn-warning me-2" :to="{ name: 'CreateService' }">Add New Service</router-link>
        </div>
    </div>

    <Search placeholder="Search services" @search="filterServices" />

    <div class="container">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                    <th scope="col"># Professionals</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="service in filteredServices" :key="service.id">
                    <th scope="row">{{ service.id }}</th>
                    <td>{{ service.name }}</td>
                    <td>{{ service.price }}</td>
                    <td>{{ service.professional_count }}</td>
                    <td>
                        <router-link 
                            class="btn btn-warning me-2" 
                            :to="{ name: 'UpdateService', params: { serviceId: service.id } }">
                            Update
                        </router-link>   
                        
                        <button class="btn btn-danger" @click="deleteService(service.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
    import { onMounted, ref, computed } from 'vue';
    import { useServices } from '@/composables/useServices';
    import Search from './Search.vue';
        
    const { services, fetchServices } = useServices();

    const searchQuery = ref('');
    const filterServices = query => {
        searchQuery.value = query;
    }

    const filteredServices = computed(() =>
        services.value.filter(service => 
            service.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
    )

    const deleteService = async (serviceId) => {
        try {
            await useServices().deleteService(serviceId)
            alert('Service deleted successfully')
        } catch (error) {
            alert(error.message)
        }

    }

    onMounted(() => {
        fetchServices();
    })

    
</script>
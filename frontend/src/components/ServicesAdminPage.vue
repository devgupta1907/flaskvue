<template>
    <div class="d-flex justify-content-between align-items-center m-4">
        <h3 class="display-6 lead">Services</h3>
        <div>
            <router-link class="btn btn-warning me-2" :to="{ name: 'CreateService' }">Add New Service</router-link>
        </div>
    </div>

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
                <tr v-for="service in services" :key="service.id">
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
    import { onMounted, ref } from 'vue';
    import { useServices } from '@/composables/useServices';
        
    const { services, fetchServices } = useServices();

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
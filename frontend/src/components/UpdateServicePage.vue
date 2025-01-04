<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form @submit.prevent="updateService">

                    <div class="mb-3">
                      <label for="serviceName" class="form-label">Service Name</label>
                      <input type="text" class="form-control" v-model="newServiceName" id="serviceName" name="serviceName" required>
                      <div id="serviceHelp" class="form-text">The service name must be unique</div>
                    </div>

                    <div class="input-group mb-3">
                        <label for="servicePrice" class="form-label input-group">Base Price</label>
                        <span class="input-group-text">&#8377;</span>
                        <input type="number" class="form-control" v-model="newServicePrice" id="servicePrice" name="servicePrice" min="10" required>
                    </div>

                    <div class="mb-3">
                        <label for="serviceCategory" class="form-label">Service Category</label>
                        <select class="form-select" id="serviceCategory" v-model="newServiceCategory" name="serviceCategory" required>
                                <option v-for="category in categories" :key="category.id" :value="category.id">{{ category.name }}</option>
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="serviceDescription" class="form-label">Service Description</label>
                        <textarea class="form-control" id="serviceDescription" v-model="newServiceDescription" name="serviceDescription" rows="3" required></textarea>
                        <div id="serviceHelp" class="form-text">Tell the customers more about this service</div>
                    </div>

                    <div class="mb-3">
                        <button type="submit" class="btn btn-warning">Submit</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useServices } from '@/composables/useServices';
    import { useCategories } from '@/composables/useCategories';
    import { useRoute, useRouter } from 'vue-router';

    const route = useRoute()
    const router = useRouter()
    
    const { services, fetchServices } = useServices()
    const { categories, fetchCategories } = useCategories()

    const serviceId = route.params.serviceId
    const newServiceName = ref('')
    const newServicePrice = ref(null)
    const newServiceDescription = ref('')
    const newServiceCategory = ref(null)

    const updateService = async () => {
        try {
            const serviceName = newServiceName.value
            const servicePrice = newServicePrice.value
            const serviceDescription = newServiceDescription.value
            const serviceCategory = newServiceCategory.value
            await useServices().updateService(serviceId, serviceName, servicePrice, serviceDescription, serviceCategory);
            
            router.push({ name: 'ServicesAdmin' })
            alert('Service updated successfully')
        } catch (error) {
            alert(error.message)
        }
    };  

    onMounted(async () => {
        fetchCategories()
        await fetchServices()
        const fetchedService = services.value.find(s => s.id === parseInt(serviceId));
        if (fetchedService) {
            newServiceName.value = fetchedService.name
            newServicePrice.value = fetchedService.price
            newServiceDescription.value = fetchedService.description
            newServiceCategory.value = fetchedService.category_id
        }
    })

</script>
<template>
    <div class="d-flex justify-content-between align-items-center m-4">
        <h3 class="display-6 lead">Categories</h3>
        <div>
            <router-link class="btn btn-warning me-2" :to="{ name: 'CreateCategory' }">Add New Category</router-link>
        </div>
    </div>

    <Search placeholder="Search categories" @search="filterCategories" />

    <div class="container">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col"># Services</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>

            <tbody>
                <tr v-for="category in filteredCategories" :key="category.id">
                    <th scope="row">{{ category.id }}</th>
                    <td>{{ category.name }}</td>
                    <td>{{ category.service_count }}</td>
                    <td>
                        <router-link 
                            class="btn btn-warning me-2" 
                            :to="{ name: 'UpdateCategory', params: { categoryId: category.id } }">
                            Update
                        </router-link>                     
                    
                        <button v-if="category.service_count === 0" class="btn btn-danger" @click="deleteCategory(category.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
    import { onMounted, ref, computed } from 'vue'
    import { useCategories } from '@/composables/useCategories'
    import Search from './Search.vue';
        
    const { categories, fetchCategories } = useCategories()

    const searchQuery = ref('');
    const filterCategories = query => {
        searchQuery.value = query;
    }

    const filteredCategories = computed(() =>
        categories.value.filter(category => 
            category.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
    )

    const deleteCategory = async (categoryId) => {
        try {
            await useCategories().deleteCategory(categoryId)
            alert('Category deleted successfully')
        } catch (error) {
            alert(error.message)
        }
    }

    onMounted(() => {
        fetchCategories();
    })

    
</script>
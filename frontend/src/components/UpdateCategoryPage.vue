<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form @submit.prevent="updateCategory">

                    <div class="mb-3">
                        <label for="title" class="form-label">Category Name</label>
                        <input type="text" v-model="newCategoryName" class="form-control" name="title" required>
                        <div id="titleHelp" class="form-text">Enter category name here</div>
                    </div>

                    <div class="mb-3">
                        <button type="submit" class="btn btn-warning">Update</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useCategories } from '@/composables/useCategories';
    import { useRoute, useRouter } from 'vue-router';

    const { categories, fetchCategories } = useCategories()

    const route = useRoute()
    const router = useRouter()
    const categoryId = route.params.categoryId
    const newCategoryName = ref('')

    const updateCategory = async () => {
        try {
            await useCategories().updateCategory(categoryId, newCategoryName.value);
            newCategoryName.value = '';
            router.push({ name: 'CategoriesAdmin' })
            alert('Category updated successfully')
        } catch (error) {
            alert(error.message)
        }
    };

    onMounted(async () => {
        await fetchCategories();
        const fetchedCategory = categories.value.find(c => c.id === parseInt(categoryId));
        if (fetchedCategory) {
            newCategoryName.value = fetchedCategory.name;
        }
    });

    

</script>
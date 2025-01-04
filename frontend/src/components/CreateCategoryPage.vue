<template>
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form @submit.prevent="addCategory">

                    <div class="mb-3">
                        <label for="title" class="form-label">Category Name</label>
                        <input type="text" v-model="newCategoryName" class="form-control" name="title" required>
                        <div id="titleHelp" class="form-text">Enter category name here</div>
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
    import { ref } from 'vue';
    import { useCategories } from '@/composables/useCategories';
    import { useRouter } from 'vue-router';

    const router = useRouter()
    const newCategoryName = ref('')


    const addCategory = async () => {
        try {
            const categoryName = newCategoryName.value;
            await useCategories().addCategory(categoryName);
            newCategoryName.value = '';

            router.push({ name: 'CategoriesAdmin' })
            alert('Category added successfully')
        } catch (error) {
            alert(error.message)
        }
        
    };  

</script>
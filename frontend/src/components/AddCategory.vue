<script setup>
    import { onMounted, ref } from 'vue';
    import { useCategoryStore } from '@/stores/categoryStore';

    const categoryStore = useCategoryStore();
    const newCategoryName = ref("");

    const addCategory = async () => {
        try {
            const newCategory = await categoryStore.addCategory(newCategoryName.value);
            alert(`Category ${newCategory.name} Added Successfully!`);
        } catch (error) {
            alert(`Error: ${error.message}`)
        } finally {
            newCategoryName.value = "";
        }
    }

    onMounted(() => {
        console.log("Add Category Mounted")
    })

</script>

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
                        <button type="submit" class="btn btn-warning">Add Category</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

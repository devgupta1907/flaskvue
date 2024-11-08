<!-- <template>
    <div class="container m-4">
        <h1 class="display-5 lead">Categories API</h1>

        <form @submit.prevent="addACategory">
            <input type="text" v-model="newCategory" placeholder="Add a category" required>
            <button type="submit">Add Book</button>
        </form>

        <ul v-if="allCategories.length">
            <li v-for="item in allCategories" :key="item.id">
                {{ item.name }}
            </li>
        </ul>
        <div v-else>
            <p>No categories are available right now!</p>
        </div>
    </div>
</template>



<script setup>

    import { ref, onMounted } from 'vue';
    import { useCategoryStore } from '@/stores/categoryStore';

    const allCategories = ref([])
    const newCategory = ref("")
    const categoryStore = useCategoryStore()

    // const emit = defineEmits(['categoriesFetched'])

    // const fetchAllCategories = async () => {
    //     try {
    //         const response = await fetch('http://localhost:5000/categories');
    //         const jsonData = await response.json()
    //         allCategories.value = jsonData

            
            
    //     } catch (error) {
    //         console.log("ERROR", error.message)
    //     }
    // }


    const addACategory = async () => {
    try {
      const response = await fetch('http://localhost:5000/categories', {
        method: "POST",
        headers: {
          'Content-Type': "application/json"
        },
        body: JSON.stringify({
          name: newCategory.value
        })
      });
      
      const dataResponse = await response.json()
      if (!response.ok) {
        throw new Error(dataResponse.message)
      }

      const newCat = dataResponse
      allCategories.value.push(newCat)

      console.log("Category Added Successfully")
      
    } catch (error) {
        console.log("ERROR", error.message)
    } finally {
        newCategory.value =""
    }
  }

</script> -->

<template>
  <div class="container m-4">
    <h1 class="display-5 lead">Categories API</h1>

    <form @submit.prevent="handleAddCategory">
      <input type="text" v-model="newCategoryName" placeholder="Add a category" required>
      <button type="submit">Add a Category</button>
    </form>

    <ul v-if="categoryStore.allCategories.length">
      <li v-for="category in categoryStore.allCategories" :key="category.id">
        {{ category.name }}
      </li>
    </ul>
    <div v-else>
      <p>No categories found</p>
    </div>
  </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue';
  import { useCategoryStore } from '@/stores/categoryStore';

  const categoryStore = useCategoryStore();
  const newCategoryName = ref('');

  const handleAddCategory = async () => {
    try {
      await categoryStore.addCategory(newCategoryName.value);
      newCategoryName.value = '';
    } catch (error) {
      // Handle error (show message to user, etc.)
    }
  };

  // const handleDeleteCategory = async (categoryId) => {
  //   try {
  //     await categoryStore.deleteCategory(categoryId);
  //   } catch (error) {
  //     // Handle error
  //   }
  // };

  onMounted(categoryStore.fetchAllCategories)
</script>
<template>

  <div class="container m-4">
    
    <!-- Flash Component -->
    <Flash 
      v-if="flashStore.showFlash" 
      :message="flashStore.flashMessage" 
      :messageType="flashStore.flashMessageType"
      @close="flashStore.handleFlashClose" 
    />
    
    <h1 class="display-5 lead">Books API</h1>

    <form @submit.prevent="addABook">
      <input type="text" v-model="newBookTitle" placeholder="Enter book title" required>
      <input type="number" v-model="newBookPrice" placeholder="Enter book price" required>
      
      <select v-model="selectedCategoryId" required>
        <option v-for="cat in categoryStore.allCategories" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>

      <button type="submit">Add Book</button>
    </form>

    <ul v-if="allBooks.length">
      <li v-for="item in allBooks" :key="item.id">
        {{ item.title }}
      </li>
    </ul>

    <div v-else>
      <p>No books are available right now!</p>
    </div>
  
  </div>

</template>
  
<script setup>
  import { ref, onMounted, computed } from 'vue';
  import Flash from './Flash.vue';
  import { useCategoryStore } from '@/stores/categoryStore';
  import { useFlashStore } from '@/stores/flashStore';

  const categoryStore = useCategoryStore();
  const flashStore = useFlashStore();

  const selectedCategoryId = ref();
  
  const allBooks = ref([]);
  const newBookTitle = ref("")
  const newBookPrice = ref(null)
  
  
  const fetchAllBooks = async () => {
    try {
      const response = await fetch('http://localhost:5000/books');
      const jsonData = await response.json();
      allBooks.value = jsonData;
    } catch (error) {
      flashStore.showFlashMessage(error.message, "danger")
    }
  };

  const addABook = async () => {
    try {
      if (newBookPrice.value <= 499) {
        throw new Error("Book price is less")
      }
      const response = await fetch('http://localhost:5000/books', {
        method: "POST",
        headers: {
          'Content-Type': "application/json"
        },
        body: JSON.stringify({
          title: newBookTitle.value,
          price: newBookPrice.value,
          category_id: selectedCategoryId.value
        })
      });
      
      const dataResponse = await response.json()
      if (!response.ok) {
        throw new Error(dataResponse.message)
      }

      const newBook = dataResponse
      allBooks.value.push(newBook)

      flashStore.showFlashMessage("Book Added Successfully!", "success")
      
    } catch (error) {
      flashStore.showFlashMessage(error.message, "danger")
    } finally {
      newBookTitle.value = ""
      newBookPrice.value = ""
      selectedCategoryId.value =""
    }
  }

  onMounted(() => {
    console.log("Books Mounted")
    categoryStore.fetchAllCategories()
    fetchAllBooks()
  })
  // onMounted(fetchAllBooks)

  </script>
  
  <style scoped>
  </style>
  
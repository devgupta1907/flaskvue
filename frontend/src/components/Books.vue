<template>
  <div class="container">
        <h3 class="text-center display-5 mt-2">Books API</h3>
        <div class="row">
        </div>
  </div>
  
  <div class="container mt-5">
    <div class="row justify-content-center">

      <Flash 
        v-if="flashStore.showFlash" 
        :message="flashStore.flashMessage" 
        :messageType="flashStore.flashMessageType"
        @close="flashStore.handleFlashClose" 
      />

      <div class="col-md-6">
        <form method="post" @submit.prevent="addABook">

          <div class="mb-3">
            <label for="title" class="form-label">Book Title</label>
            <input type="text" v-model="newBookTitle" class="form-control" name="title" minlength="3" required>
            <div id="titleHelp" class="form-text">{{ titleError }}</div>
          </div>

          <div class="mb-3">
            <label for="price" class="form-label">Book Price</label>
            <input type="number" v-model="newBookPrice" class="form-control" name="price" min="50" required>
            <div id="priceHelp" :class="priceError ? 'form-text text-danger' : 'form-text'">{{ priceError }}</div>
          </div>

          <div class="mb-3">
            <label for="category" class="form-label">Book Category</label>
            <select v-model="selectedCategoryId" class="form-control" required>
              <option v-for="category in categories" :key="category.id" :value="category.id">
                {{ category.name }}
              </option>
            </select>
          </div>

          <div class="mb-3">
            <button type="submit" class="btn btn-warning" :disabled="!isFormValid">Register Book</button>
          </div>
          
        </form>
      </div>
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

  const categories = computed(() => categoryStore.categories);
  const selectedCategoryId = ref(null);
  
  const allBooks = ref([]);
  const newBookTitle = ref("")
  const newBookPrice = ref()

  const titleError = computed(() => {
    return newBookTitle.value.length < 3 ? "Book title should be longer than 3 characters." : null
  });

  const priceError = computed(() => {
    return newBookPrice.value < 50 ? "Price should not be less than 50." : null
  });

  const isFormValid = computed(() => {
    return !titleError.value && !priceError.value;
  });
  


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
      const response = await fetch('http://localhost:5000/books', {
        method: "POST",
        headers: {
          'Content-Type': "application/json"
        },
        body: JSON.stringify({
          title: newBookTitle.value,
          price: newBookPrice.value,
          category: selectedCategoryId.value
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
      newBookPrice.value = 0
      selectedCategoryId.value = null
    }
  }
  

  onMounted(() => {
    flashStore.handleFlashClose();
    console.log("Books Mounted")
    categoryStore.fetchCategories()
    fetchAllBooks()
  })

  </script>
  
  <style scoped>
  </style>
  
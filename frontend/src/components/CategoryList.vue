<script setup>
  import { computed, onMounted } from 'vue';
  import { useCategoryStore } from '@/stores/categoryStore';
  
  const categoryStore = useCategoryStore();
  const categories = computed(() => categoryStore.categories);

  onMounted(() => {
    console.log("Category List Mounted"),
    categoryStore.fetchCategories() 
  })

</script>

<template>
  <div class="container mt-4">
    <p class="lead">- found <b>{{ categories.length }}</b> category(s)</p>
    <div class="row">
      <div class="col-md-3 mb-4" v-for="category in categories" :key="category.id">
        <div class="card border border-0">
          <div class="card-body shadow rounded">
            <h5 class="card-title text-center">
              {{ category.name }}
            </h5>
            <div class="text-center">
              <a href="#" class="btn btn-warning">Choose Service</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
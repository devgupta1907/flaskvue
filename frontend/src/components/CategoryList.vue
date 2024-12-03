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
  <ul>
    <li v-for="category in categories" :key="category.id">
      {{ category.name }}
    </li>
  </ul>
</template>
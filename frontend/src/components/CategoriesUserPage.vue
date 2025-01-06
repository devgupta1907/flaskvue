<template>

  <div class="container mt-4">
    <h3 class="text-center display-5 my-2">MadyPro Categories</h3>
    <div class="row">
      <div class="text-center">
        <p class="lead">Be It Home Decor, Laptop Repair, or Beauty & Grooming - We Provide What You Want!</p>
      </div>
    </div>
  </div>

  <Search placeholder="Search categories" @search="filterCategories" />
  
  <div class="container mt-4">
    <p class="lead">- found <b>{{ filteredCategories.length }}</b> category(s)</p>
    <div class="row">
      <div class="col-md-3 mb-4" v-for="category in filteredCategories" :key="category.id">
        <div class="card border border-0">
          <div class="card-body shadow rounded">
            <h5 class="card-title text-center">
              {{ category.name }}
            </h5>
            <div class="text-center">
              <router-link
                class="btn btn-warning"
                :to="{ name: 'ServicesUser', 
                      query: { category: category.id }}">
                View Services
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
<script setup>
  import { ref, computed, onMounted } from 'vue';
  import { useCategories } from '@/composables/useCategories';
  import Search from './Search.vue';
  
  const { categories, fetchCategories } = useCategories();

  const searchQuery = ref('');
    const filterCategories = query => {
        searchQuery.value = query;
    }

    const filteredCategories = computed(() =>
        categories.value.filter(category => 
            category.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
    )

  onMounted(() => {
    fetchCategories();
  });
</script>
  
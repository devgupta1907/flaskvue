<template>

  <div class="container mt-4">
    <h3 class="text-center display-5 my-2">MadyPro Categories</h3>
    <div class="row">
      <div class="text-center">
        <p class="lead">Be It Home Decor, Laptop Repair, or Beauty & Grooming - We Provide What You Want!</p>
      </div>
    </div>
  </div>
  
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
  import { onMounted } from 'vue';
  import { useCategories } from '@/composables/useCategories';
  
  const { categories, fetchCategories } = useCategories();

  onMounted(() => {
    fetchCategories();
  });
</script>
  
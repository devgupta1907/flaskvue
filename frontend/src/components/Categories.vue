<template>

  <div class="container mt-4">
    <h3 class="text-center display-5 my-2">MadyPro Categories</h3>
    <div class="row">
      <div class="text-center">
        <p class="lead">Be It Home Decor, Laptop Repair, or Beauty & Grooming - We Provide What You Want!</p>
      </div>
    </div>
  </div>
    <AddCategory />
    <CategoryList />
  </template>
  
  <script setup>
  import AddCategory from './AddCategory.vue';
  import CategoryList from './CategoryList.vue';
  </script>
  
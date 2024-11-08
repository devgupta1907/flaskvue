<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">MyApp</a>
        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">

            <li class="nav-item">
              <router-link class="nav-link" to="/books">Books</router-link>
            </li>

            <li class="nav-item">
              <router-link class="nav-link" to="/category">Categories</router-link>
            </li>

            <li class="nav-item">
              <router-link class="nav-link" to="/register">Register</router-link>
            </li>

            <li class="nav-item">
              <router-link class="nav-link" to="/login">Login</router-link>
            </li>

          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  </script>
  
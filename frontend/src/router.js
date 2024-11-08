
import { createRouter, createWebHistory } from 'vue-router';
import Books from './components/Books.vue';
import Category from './components/Category.vue';
import Register from './components/Register.vue';
import Login from './components/Login.vue';

const routes = [
    { path: '/books', component: Books, name: 'Books'},
    { path: '/category', component: Category, name: 'Category'},
    { path: '/register', component: Register, name: 'Register'},
    { path: '/login', component: Login, name: 'Login' }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;
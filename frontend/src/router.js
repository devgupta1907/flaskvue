
import { createRouter, createWebHistory } from 'vue-router';
import Books from './components/Books.vue';
import Categories from './components/Categories.vue';
import Register from './components/Register.vue';
import Login from './components/Login.vue';
import Registration from './components/Registration.vue';

const routes = [
    { path: '/books', component: Books, name: 'Books'},
    { path: '/category', component: Categories, name: 'Category'},
    { path: '/register', component: Registration, name: 'Register'},
    { path: '/login', component: Login, name: 'Login' }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;
import { createRouter, createWebHistory } from 'vue-router';

// Registration and Login Pages
import Register from './components/Register.vue';
import Login from './components/Login.vue';

// Admin Pages
import CustomersAdminPage from './components/CustomersAdminPage.vue';
import ProfessionalsAdminPage from './components/ProfessionalsAdminPage.vue';
import CategoriesAdminPage from './components/CategoriesAdminPage.vue';
import ServicesAdminPage from './components/ServicesAdminPage.vue';

// Entity Creaton Pages
import CreateCategoryPage from './components/CreateCategoryPage.vue';
import CreateServicePage from './components/CreateServicePage.vue';

// Update Pages
import UpdateCategoryPage from './components/UpdateCategoryPage.vue';
import UpdateServicePage from './components/UpdateServicePage.vue';

// /User Pages
import CategoriesUserPage from './components/CategoriesUserPage.vue';
import ServicesUserPage from './components/ServicesUserPage.vue';
import ProfessionalsByServicePage from './components/ProfessionalsByServicePage.vue';

// Dashboards
import CustomerDashboard from './components/CustomerDashboard.vue';
import ProfessionalDashboard from './components/ProfessionalDashboard.vue';
import AdminDashboardPage from './components/AdminDashboardPage.vue';


const routes = [
    { path: '/category', 
      component: CategoriesUserPage, 
      name: 'CategoriesUser'
    },
    { path: '/service', 
      component: ServicesUserPage, 
      name: 'ServicesUser'
    },
    { path: '/service/:serviceId/professionals', 
      component: ProfessionalsByServicePage, 
      name: 'ProfessionalsByServiceUser',
      meta: { requiresAuth: true, requiresRole: 'customer' }
    },
    { path: '/register', 
      component: Register, 
      name: 'Register'
    },
    { path: '/login', 
      component: Login, 
      name: 'Login' 
    },
    { path: '/customer_dashboard', 
      component: CustomerDashboard, 
      name: 'CustomerDashboard', 
      meta: { requiresAuth: true, requiresRole: 'customer' }
    },
    { path: '/professional_dashboard', 
      component: ProfessionalDashboard, 
      name: 'ProfessionalDashboard', 
      meta: { requiresAuth: true, requiresRole: 'professional' }
    },
    { path: '/admin-dashboard', 
      component: AdminDashboardPage, 
      name: 'AdminDashboard', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    { path: '/admin-customers', 
      component: CustomersAdminPage, 
      name: 'CustomersAdmin', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    { path: '/admin-professionals', 
      component: ProfessionalsAdminPage, 
      name: 'ProfessionalsAdmin', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },

    { path: '/admin-services', 
      component: ServicesAdminPage, 
      name: 'ServicesAdmin', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    { path: '/admin-services/add', 
      component: CreateServicePage, 
      name: 'CreateService', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    { path: '/admin-services/:serviceId/update', 
      component: UpdateServicePage, 
      name: 'UpdateService', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },

    { path: '/admin-categories', 
      component: CategoriesAdminPage, 
      name: 'CategoriesAdmin', 
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    {
      path: '/admin-categories/add', 
      component: CreateCategoryPage, 
      name: 'CreateCategory',
      meta: { requiresAuth: true, requiresRole: 'admin' }
    },
    {
      path: '/admin-categories/:categoryId/update', 
      component: UpdateCategoryPage, 
      name: 'UpdateCategory',
      meta: { requiresAuth: true, requiresRole: 'admin' }
    }

]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  const userRole = localStorage.getItem('role')
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const requiresRole = to.meta.requiresRole;

  // If already logged in and accessing login page, redirect to category
  if (to.name === 'Login' && token) return next({ name: 'Category' });

  // If route requires auth and user is not authenticated, redirect to login
  if (requiresAuth && !token) {
    alert('Please login to access this page');
    return next({ name: 'Login' });
  }

  // If route requires specific role and user does not match, redirect
  if (requiresRole && userRole !== requiresRole) {
    alert(`Access restricted to ${requiresRole}s`);
    return next({ name: 'CategoriesUser' });
  }

  next();  // Proceed if no issues
});

export default router;
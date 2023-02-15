import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import Login  from '../views/Login'
import Registration from '../views/Registration'
import Catalog from '../views/Catalog'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/registration',
    name: 'registration',
    component: Registration
  },
  {
    path: '/catalog',
    name: 'catalog',
    component: Catalog
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

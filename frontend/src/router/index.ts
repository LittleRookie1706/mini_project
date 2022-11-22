import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from '../views/App.vue'
import Abc from '../views/Abc.vue'

const routes: Array<RouteRecordRaw> = [
  { path: '/', component: Home } ,
  { path: '/abc', component: Abc } ,
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

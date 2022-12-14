import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from '@/views/Home.vue'
import NewsPost from '@/views/NewsPost.vue'

import Admin from '@/views/Admin.vue'
import AdminStatistic from '@/views/AdminStatistic.vue'
import AdminNewsPost from '@/views/AdminNewsPost.vue'


const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'home', component: Home } ,
  { path: '/page/:pageNumber', name: 'page', component: Home } ,
  { path: '/:newsId', name: 'newspost', component: NewsPost } ,

  { path: '/admin/manage-content', name: 'ad-content', component: Admin },
  { path: '/admin/manage-content/page/:pageNumber', name: 'ad-page', component: Admin },
  { path: '/admin/manage-content/:newsId', name: 'ad-newspost', component: AdminNewsPost },
  { path: '/admin/statistic', name: 'ad-statistic', component: AdminStatistic },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

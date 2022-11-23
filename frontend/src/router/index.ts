import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

import Home from '@/views/Home.vue'
import NewsPost from '@/views/NewsPost.vue'
import Admin from '@/views/Admin.vue'
import AdminNews from '@/views/AdminNews.vue'


const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'home', component: Home } ,
  { path: '/page/:pageNumber', name: 'page', component: Home } ,
  { path: '/:newsId', name: 'newspost', component: NewsPost } ,

  { path: '/admin/manage-content', name: 'ad-content', component: Admin },
  { path: '/admin/manage-content/page/:pageNumber', name: 'ad-news', props: true, component: AdminNews }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

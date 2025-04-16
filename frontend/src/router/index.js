import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import RandomBlog from '../views/RandomBlog.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/random'
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/random',
    name: 'RandomBlog',
    component: RandomBlog
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router 
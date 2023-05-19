import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MoviesView from '@/views/MoviesView'
import LoginView from '@/views/LoginView'
import SignupView from '@/views/SignupView'
import ProfileView from '@/views/ProfileView'
import LikeMovieChooseView from '@/views/LikeMovieChooseView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MoviesView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/likemoviechoose',
    name: 'likemoviechoose',
    component: LikeMovieChooseView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

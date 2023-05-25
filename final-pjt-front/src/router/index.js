import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import MoviesView from '@/views/MoviesView'
import MovieDetailView from '@/views/MovieDetailView'
import ReviewDetailView from '@/views/ReviewDetailView'
import ProfileView from '@/views/ProfileView'
import RecommendView from '@/views/RecommendView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MoviesView
  },
  {
    path: '/movies/:id',
    name: 'detail',
    component: MovieDetailView
  },
  {
    path: '/movies/:movie_id/:review_id',
    name: 'review_detail',
    component: ReviewDetailView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

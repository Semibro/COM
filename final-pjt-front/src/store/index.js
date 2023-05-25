import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    popularMovies: null,
    detail_movie: null,
    user_info: null, // 현재 로그인한 유저 정보
    recommendMovies: null,
  },
  getters: {
  },
  mutations: {
    SIGN_UP(state, token) {
      state.token = token
      router.push({name: 'login'})
    },
    GET_POPULAR_MOVIES(state, movies) {
      state.popularMovies = movies
    },
    TO_DETAIL(state, id) {
      let count = 0
      state.popularMovies.forEach(movie => {
        if (movie.id === id) {
          state.detail_movie = state.popularMovies[count]
        } else {
          count ++
        }
      })
    },
    GET_USER_INFO(state, info) {
      state.user_info = info
    },
    LIKE_MOVIE(state, id) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${id}/likes/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    GET_RECOMMEND_MOVIES(state, recommends) {
      console.log(recommends)
      state.recommendMovies = recommends
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          context.commit('SIGN_UP', res.data.key)
        })
        .catch(err => console.log(err))
    },
    getPopularMovies(context) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/`,
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(res => {
          context.commit('GET_POPULAR_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },
    toDetail(context, id) {
      context.commit('TO_DETAIL', id)
    },
    getUserInfo(context) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(res => {
          context.commit('GET_USER_INFO', res.data)
        })
        .catch(err => console.log(err))
    },
    likeMovie(context, id) {
      context.commit('LIKE_MOVIE', id)
    },
    getRecommendMovies(context, movieId) {
      const token = localStorage.getItem('jwt')

      axios({
        method: 'get',
        url: `${API_URL}/movies/recommend/${movieId}`,
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(res => {
          context.commit('GET_RECOMMEND_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})

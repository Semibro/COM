import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
// import _ from 'lodash'

const API_URL = 'http://127.0.0.1:8000'
const API_KEY = 'b87676597510090177f5217ea5f4d280'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    likeMovieList: [],
    recommendMovies: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    SIGN_UP(state, token) {
      state.token = token
      router.push({name: 'likemoviechoose'})
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name: 'home'})
    },
    ADD_LIKE_MOVIE(state, movie) {
      let flag = false
      for (let i = 0; i < state.likeMovieList.length; i++) {
        if (movie.id === state.likeMovieList[i].id) {
          flag = true
          break
        }
      }
      if (!flag) {
        state.likeMovieList.push(movie)
        console.log(state.likeMovieList)
      }
    },
    RECOMMEND_MOVIES(state, randommovie) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${randommovie}/recommendations?language=ko-KR&page=1&api_key=${API_KEY}`
      })
        .then(res => {
          state.recommendMovies.push(res)
          console.log(state.recommendMovies)
        })
        .catch(err => console.log(err))
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
    logIn(context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
    },
    addLikeMovie(context, movie) {
      context.commit('ADD_LIKE_MOVIE', movie)
    },
    recommendMovies(context, randommovie) {
      context.commit('RECOMMEND_MOVIES', randommovie)
    } 
  },
  modules: {
  }
})

<template>
  <div>
    <h1> {{ user_info.username }} 님의 프로필 </h1>
    <div v-for="(movie, index) in like_movie_list" :key="index">
      {{ movie }}
      <br><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      like_movie_list: [],
    }
  },
  computed: {
    user_info() {
      return this.$store.state.user_info
    },
    liked_movies() {
      return this.$store.state.liked_movies
    },
    popularMovies() {
      return this.$store.state.popularMovies
    }
  },
  methods: {
    getProfile() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/profile/${this.$route.params.username}`,
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
    findUserLike() {
      const lst = []
      // like_movie_list = this.popularMovies.filter(movie => {
      //   // console.log(Object.values(movie.like_users))
      //   Object.values(movie.like_users).includes(this.user_info.pk)
      // })
      // console.log(like_movie_list)


      this.popularMovies.forEach(movie => {
        movie.like_users.forEach(userId => {
          if (userId === this.user_info.pk) {
            lst.push(movie)
            // this.like_movie_list.push(movie)
          }
        })
      })
      this.like_movie_list = lst
    }
  },
  created() {
    // this.findUserLike()
    this.$store.dispatch('getPopularMovies')
  },
  // updated() {
  //   this.$store.dispatch('getPopularMovies')
  // }
}
</script>

<style>

</style>
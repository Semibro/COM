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
          this.like_movie_list = res.data.like_movies
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>
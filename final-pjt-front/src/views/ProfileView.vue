<template>
  <div>
    <h1> {{ user_info.username }} 님의 프로필 </h1>
    {{ like_movie_list }}
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
      this.liked_movies.forEach(movie => {
       if (movie.like_users[0] === this.user_info.id) {
        this.like_movie_list.push(movie)
       }
      })
    }
  },
  created() {
    this.getProfile()
  }
}
</script>

<style>

</style>
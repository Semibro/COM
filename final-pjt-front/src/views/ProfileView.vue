<template>
  <div>
    <h1> {{ masterOfProfile }} 님의 프로필</h1>
    <button @click="followUser(masterOfProfile)">팔로우/언팔로우</button>
    <p>팔로워: {{ real_user_info.followings.length }} 명 </p>
    <br><br>
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
      real_user_info: null,
      masterOfProfile: this.$route.params.username
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
          // console.log(res)
          this.real_user_info = res.data
          this.like_movie_list = res.data.like_movies
        })
        .catch(err => {
          console.log(err)
        })
    },
    followUser(username) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/profile/${username}/follow/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(() => {
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
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
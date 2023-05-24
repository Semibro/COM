<template>
  <div>
    <h1> {{ masterOfProfile }} 님의 프로필</h1>
    <div v-if="follow_check">
      <button @click="followUser(masterOfProfile)">언팔로우</button>
    </div>
    <div v-else>
      <button @click="followUser(masterOfProfile)">팔로우</button>
    </div>
    <p>팔로워: {{ getFollowingsCount }} 명 </p>
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
      real_user_info: [],
      masterOfProfile: this.$route.params.username,
      profile_data: [],
      follow_check: null,
    }
  },
  computed: {
    user_info() {
      return this.$store.state.user_info
    },
    popularMovies() {
      return this.$store.state.popularMovies
    },
    getFollowingsCount() {
      if (this.real_user_info && this.real_user_info.followings) {
        return this.real_user_info.followings.length;
      }
      return 0;
    },
  },
  methods: {
    is_follow() {
      const user = this.$store.state.user_info
      console.log(user)
      let flag = 1
      this.profile_data.followings.forEach(follower => {
        if (follower === user.pk) {
          this.follow_check = true
          flag = 2
        }
      })
      if (flag === 1) {
        this.follow_check = false
      }
    },
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
          this.real_user_info = res.data
          this.like_movie_list = res.data.like_movies
          this.is_follow()
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
        .then(res => {
          console.log(res)
          this.profile_data = res.data
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getProfile()
    this.$store.dispatch('getUserInfo')
    const followCheck = localStorage.getItem('follow_check')
    this.follow_check = followCheck === 'true'
  },
  mounted() {
    this.getProfile()
  },
  watch: {
    follow_check(newVal) {
      localStorage.setItem('follow_check', newVal)
    }
  }
}
</script>

<style>

</style>
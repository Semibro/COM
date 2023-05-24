<template>
  <div>
    <MovieDetailPage :detail_movie="detail_movie"/>
    <br>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
     <input type="text" v-model="inputdata">
    </form>
    <br>
    <div v-for="(review, index) in reviews" :key="index">
      <span class="username" @click="toProfile(review.user)">{{ review.user }}</span> : {{ review.content }}
      <button @click="toReviewDetail(review.id, review.user_id)">DETAIL</button>
    </div>
  </div>
</template>

<script>
import MovieDetailPage from '@/components/MovieDetailPage'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailPage,
  },
  data() {
    return {
      inputdata: null,
      reviews: [],
      written_user: null,
    }
  },
  computed: {
    detail_movie() {
      return this.$store.state.detail_movie
    },
  },
  methods: {
    createReview() {
      const content = this.inputdata
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/`,
        data: { content },
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(() => {
            this.getReviewDetail()
            this.inputdata = null
        })
        .catch(err => console.log(err))
    },
    getReviewDetail() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    toReviewDetail(id, user_id) {
      // console.log(this.$route.params.id)
      const movie = this.$route.params.id
      // console.log(id)
      const params_id = {movie_id: movie, review_id: id, user_id: user_id,}
      this.$router.push({ name: 'review_detail', params: params_id })
    },
    toProfile(username) {
      this.$router.push({ name: 'profile', params: {username} })
    }
  },
  created() {
    this.$store.dispatch('toDetail', this.$route.params.id)
    this.getReviewDetail()
  }
}
</script>

<style>
.username {
  cursor: pointer;
}
</style>
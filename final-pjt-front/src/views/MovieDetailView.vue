<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    {{ detail_movie }}
    <br>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
     <input type="text" v-model="inputdata">
    </form>
    <br>
    <div v-for="(review, index) in reviews" :key="index">
      {{ review.user }} : {{ review.content }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailView',
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
    user_info() {
      return this.$store.state.user_info
    }
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
    }
  },
  created() {
    this.$store.dispatch('toDetail', this.$route.params.id)
    this.getReviewDetail()
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style>

</style>
<template>
  <div>
    <span class="pointer" @click="toProfile(review.user)">{{ review.user }}</span>
    {{ review.content }}
    <div v-if="this.$route.params.user_id === this.user_info.pk">
      <button @click="deleteReview(review.id)">DELETE</button>
    </div>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <input type="text" v-model="inputdata">
    </form>
    <div v-for="(comment, index) in comments" :key="index">
      <span class="pointer" @click="toProfile(comment.user)">{{ comment.user }}</span> : {{ comment.content }}
      <button @click="deleteComment(comment.id)">DELETE</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewDetailView',
  data() {
    return {
      review: null,
      inputdata: null,
      comments: null,
    }
  },
  computed: {
    user_info() {
      return this.$store.state.user_info
    }
  },
  methods: {
    getReviewDetail() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment() {
      const content = this.inputdata
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/`,
        data: { content },
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(() => {
            this.getCommentList()
            this.inputdata = null
        })
        .catch(err => console.log(err))
    },
    getCommentList() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment(id) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/${id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(() => {
          this.getCommentList()
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReview(id) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(() => {
          const movie_id = {id: this.$route.params.movie_id}
          this.$router.push({name: 'detail', params: movie_id})
        })
        .catch(err => {
          console.log(err)
        })
    },
    toProfile(username) {
      this.$router.push({ name: 'profile', params: {username} })  // 프로필 이동
    }
  },
  created() {
    this.getReviewDetail()
    this.getCommentList()
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style>
.pointer {
  cursor: pointer;
}
</style>
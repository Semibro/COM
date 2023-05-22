<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    {{ detail_movie }}
    <br>
    <form @submit.prevent="createReview">
      <label for="content">내용 : </label>
     <input type="text" v-model="inputdata">
    </form>
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
    }
  },
  computed: {
    detail_movie() {
      return this.$store.state.detail_movie
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
        .then(res => {
            console.log(res)
        })
        .catch(err => console.log(err))
    }
  },
  created() {
    this.$store.dispatch('toDetail', this.$route.params.id)
  }
}
</script>

<style>

</style>
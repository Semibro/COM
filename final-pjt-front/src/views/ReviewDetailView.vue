<template>
  <div>

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
          console.log(res)
        //   this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created() {
    this.getReviewDetail()
  }
}
</script>

<style>

</style>
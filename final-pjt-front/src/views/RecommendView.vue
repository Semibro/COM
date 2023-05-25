<template>
  <div>
    <h1>영화 추천 페이지</h1>
    {{ getRecommendMovies }}
    {{ userinfo }}
  </div>
</template>

<script>
export default {
  name: 'RecommendView',
  data() {
    return {

    }
  },
  computed: {
    getRecommendMovies() {
      return this.$store.state.recommendMovies
    },
    userinfo() {
      return this.$store.state.user_info
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
    this.$store.dispatch('getRecommendMovies')
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style>

</style>
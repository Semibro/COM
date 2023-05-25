<template>
  <div>
    <h1>영화 추천 페이지</h1>
    {{ getRecommendMovies }}
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
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
    this.$store.dispatch('getRecommendMovies')
  }
}
</script>

<style>

</style>
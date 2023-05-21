<template>
  <div>
    {{ popularMovieList }}
  </div>
</template>

<script>


export default {
  name: 'MoviesView',
  components: {
  },
  computed: {
    popularMovieList() {
      return this.$store.state.popularMovies
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
  }
}
</script>

<style>

</style>
<template>
  <div>
    <h1>지금 인기있는 영화:</h1>
    <PopularMovieList 
      v-for="(movie, index) in popularMovies" :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import PopularMovieList from '@/components/PopularMovieList'

export default {
  name: 'MoviesView',
  components: {
    PopularMovieList,
  },
  computed: {
    popularMovies() {
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
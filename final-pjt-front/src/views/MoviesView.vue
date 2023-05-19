<template>
  <div>
    
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MoviesView',
  computed: {
    likeMovieList() {
      return this.$store.state.likeMovieList
    },
    // recommendMovies() {
    //   return this.$store.state.recommendMovies
    // }
  },
  methods: {
    recommendMovies() {
      const randomMovieId = _.sample(this.likeMovieList, 1).id
      // console.log(randomMovieId)
      this.$store.dispatch('recommendMovies', randomMovieId)
    }
  },
  created() {
    this.recommendMovies()
  }
}
</script>

<style>

</style>
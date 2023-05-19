<template>
  <div>
    취향저격 콘텐츠:
    <RecommendMovieCard
      v-for="(movie, index) in recommendMoviesList" :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import RecommendMovieCard from '@/components/RecommendMovieCard'
import _ from 'lodash'

export default {
  name: 'MoviesView',
  components: {
    RecommendMovieCard,
  },
  data() {
    return {
      randomMovieTitle: null,
    }
  },
  computed: {
    likeMovieList() {
      return this.$store.state.likeMovieList
    },
    recommendMoviesList() {
      return this.$store.state.recommendMovies
    }
  },
  methods: {
    recommendMovies() {
      const randomMovie = _.sample(this.likeMovieList, 1)
      // console.log(randomMovieId)
      const randomMovieItem = [randomMovie.id, randomMovie.title]
      this.randomMovieTitle = randomMovieItem[1]
      this.$store.dispatch('recommendMovies', randomMovieItem)
    }
  },
  created() {
    this.recommendMovies()
  }
}
</script>

<style>

</style>
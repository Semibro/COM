<template>
  <div>
    당신이 좋아하는 "{{ randomMovieTitle }}" 과 비슷한 영화를 준비했어요!
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
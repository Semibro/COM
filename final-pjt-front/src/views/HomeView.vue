<template>
  <div class="home">
    <h1>지금 핫한 영화!</h1>
    <RecommendMovies
      v-for="(movie, index) in recommendMovie" :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import RecommendMovies from '../components/RecommendMovies.vue'

import _ from 'lodash'

export default {
  name: 'HomeView',
  components: {
    RecommendMovies,
  },
  data() {
    return {
      recommendMovie: [],
    }
  },
  computed: {
    popularMovies() {
      return this.$store.state.popularMovies
    }
  },
  methods: {
    getRecommendMovie() {
      this.recommendMovie = _.sampleSize(this.popularMovies, 3)
    },
  },
  created() {
    this.getRecommendMovie()
  }
}
</script>

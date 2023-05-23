<template>
  <div class="home">
    <h1>지금 핫한 영화!</h1>
    <div v-for="(movie, index) in recommendMovie" :key="index">
      {{ movie }}
      <br><br>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'HomeView',
  components: {
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
      this.recommendMovie.push(_.sample(this.popularMovies, 1))
      this.recommendMovie.push(_.sample(this.popularMovies, 1))
      this.recommendMovie.push(_.sample(this.popularMovies, 1))
    }
  },
  created() {
    this.getRecommendMovie()
  }
}
</script>

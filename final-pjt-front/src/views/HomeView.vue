<template>
  <div class="home">
    <h1>지금 핫한 영화!</h1>
    <div v-for="(movie, index) in recommendMovie" :key="index"
      @click="toDetail(movie.id)"
    >
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
    },
    toDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  },
  created() {
    this.getRecommendMovie()
  }
}
</script>

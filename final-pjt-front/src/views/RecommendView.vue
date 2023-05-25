<template>
  <div>
    <h1>영화 추천 페이지</h1>
    <p>{{ userinfo.username }}님이 좋아할 만한 영화를 골라봤어요!</p>
    <br>
    <div v-for="(movie, index) in recm_movie" :key="index">
      {{ movie.poster_path }}
      {{ movie.title }}
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'RecommendView',
  data() {
    return {
      recm_movie: [],
      like_movie: [],
      movieId: null,
    }
  },
  computed: {
    recommendMovies() {
      return this.$store.state.recommendMovies
    },
    userinfo() {
      return this.$store.state.user_info
    },
    getPopularMovies() {
      return this.$store.state.popularMovies
    },
  },
  methods: {
    randomMovie() {
      this.recm_movie = _.sampleSize(this.recommendMovies, 20)
    },
    like_movies() {
      const movielist = this.$store.state.popularMovies
      const lst = []
      movielist.forEach(movie => {
        Object.values(movie.like_users).forEach(ele => {
          if (this.userinfo.pk === ele) {
            lst.push(movie)
          }
        })
      })
      const selected_movie = _.sampleSize(lst, 1)
      console.log(selected_movie[0].id)
      return selected_movie[0].id
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
    this.$store.dispatch('getUserInfo')
    this.$store.dispatch('getRecommendMovies', this.like_movies())
  },
  mounted() {
    this.randomMovie()
  }
}
</script>

<style>

</style>
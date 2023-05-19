<template>
  <div>
    <div>
      <div class="movieCard">
        <div class="movieimgbox" @click="addLikeMovie(movie)">
          <img :src="imgurl" class="movieimg">
        </div>
        <div class="text">
          <div class="title">
            {{ movie.title }}
          </div>
          <div v-if="movie.overview">
            {{ movie.overview }}
          </div>
          <div v-else>
            <p> 등록된 줄거리가 없습니다🙏 </p>
          </div>
          <div>
            평점: {{ movie_rate }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.movie.poster_path}`
    },
    movie_rate() {
      return Math.round(this.movie.vote_average / 2)
    }
  },
  methods: {
    addLikeMovie(movie) {
      this.$store.dispatch('addLikeMovie', movie)
    }
  }
}
</script>

<style>

</style>
<template>
  <div>
    <div>
      <div class="movieCard">
        <div class="movieimgbox" @click="toDetail(movie.id)">
          <img :src="imgurl" class="movieimg">
        </div>
        <div class="text">
          <div class="title">
            {{ movie.title }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendMovies',
  props: {
    movie: Object,
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.movie.poster_path}`
    },
  },
}
</script>

<style>

</style>
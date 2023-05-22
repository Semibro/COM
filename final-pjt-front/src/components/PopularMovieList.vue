<template>
  <div>
    <div>
      <div class="movieCard">
        <div class="movieimgbox">
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
  name: 'PopularMovieList',
  props: {
    movie: Object,
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.movie.poster_path}`
    },
  }
}
</script>

<style>

</style>
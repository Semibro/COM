<template>
  <div class="PopularMovieList">
    <div class="movieCard">
      <img :src="imgurl" class="movieimg" @click="toDetail(movie.id)">
      {{ movie.title }}
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
  },
  methods: {
    toDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  }
}
</script>

<style>
.PopularMovieList {
  display: flex;
  flex-direction: row;
}

.movieCard {
  display: flex;
  flex-direction: column;
}

.movieimg {
  cursor: pointer;
}
</style>
<template>
  <div class="PopularMovieList">
      <div class="movieCard">
        <img :src="imgurl" class="movieimg" @click="toDetail(movie.id)">
        <div class="pptitle">
          {{ movie.title }}
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
  },
  methods: {
    toDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    }
  }
}
</script>

<style scoped>
.movieCard {
  display: flex;
  flex-direction: column;
  padding: 20px 70px;
  margin-top: 20px;
  /* margin-left: 27%; */
  width: 200px;
  height: 400px;
}

.movieimg {
  cursor: pointer;
  border-radius: 0.5rem;
  margin-bottom: 10px;
  height: 300px;
}

.movieimg:hover {
  transform: scale(1.21);
  transition: .4s;
}

.pptitle {
  font-size: 17px;
  font-weight: 800;
}
</style>
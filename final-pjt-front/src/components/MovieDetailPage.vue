<template>
  <div>
     <div>
      <div class="movieCard">
        <div class="movieimgbox">
          <img :src="imgurl" class="movieimg">
        </div>
        <div class="text">
          <div class="title">
            <button @click="likeMovie(detail_movie.id)">좋아요</button>
            <h3>{{ detail_movie.title }}</h3>
            {{ detail_movie.vote_average }} / {{ detail_movie.vote_count }}
            <br>
            {{ detail_movie.release_date }}
            <br>
            {{ detail_movie.overview }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetailPage',
  props: {
    detail_movie: Object,
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.detail_movie.poster_path}`
    },
  },
  methods: {
    likeMovie(id) {
      this.$store.dispatch('likeMovie', id)
    },
  }
}
</script>

<style>

</style>
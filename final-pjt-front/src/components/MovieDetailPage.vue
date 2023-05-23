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
        <iframe width="1000px" height="700px" :src="youtubesrc"></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
const API_KEY = 'cab515bc24cb97ee07d658f5fd0aa1a7'

export default {
  name: 'MovieDetailPage',
  props: {
    detail_movie: Object,
  },
  data() {
    return {
      youtubeId: null,
      youtubesrc: null,
    }
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
    getYoutube(id) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${id}/videos?&api_key=${API_KEY}`
      })
        .then(res => {
          // console.log(res.data.results[0].key)
          this.youtubeId = res.data.results[0].key
          const youtubesrc = `https://www.youtube.com/embed/${this.youtubeId}?autoplay=1&playlist=${this.youtubeId}`
          this.youtubesrc = youtubesrc
        })
        .catch(err => console.log(err))
    }
  },
  created() {
    this.getYoutube(this.detail_movie.id)
  }
}
</script>

<style>

</style>
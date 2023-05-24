<template>
  <div class="MovieDetailPage">
    <div class="movieCard">
      <div class="movieimgbox">
        <img :src="imgurl" class="movieimg">
        <img src="@/assets/icon/full_heart.png" @click="likeMovie(detail_movie.id)"
          class="heart" v-if="isLike"
        >
        <img src="@/assets/icon/bin_heart.png" @click="likeMovie(detail_movie.id)"
          class="heart" v-else
        >
      </div>
      <div class="title_text">
          <h3>{{ detail_movie.title }}</h3>
          {{ star_point }} / {{ detail_movie.vote_count }}
      </div>
    </div>
    <div class="movie_content">
      {{ detail_movie.release_date }}
      {{ detail_movie.overview }}
      <iframe width="1000px" height="700px" :src="youtubesrc"></iframe>
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
      star_point: null,
      isLike: false,
    }
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.detail_movie.poster_path}`
    },
    user_info() {
      return this.$store.state.user_info
    }
  },
  methods: {
    likeMovie(id) {
      this.$store.dispatch('likeMovie', id)
      this.isLike = !this.isLike
      console.log(this.isLike)
    },
    getYoutube(id) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${id}/videos?&api_key=${API_KEY}`
      })
        .then(res => {
          // console.log(res.data.results[0].key)
          this.youtubeId = res.data.results[0].key
          const youtubesrc = `https://www.youtube.com/embed/${this.youtubeId}?autoplay=1&mute=1&playlist=${this.youtubeId}`
          this.youtubesrc = youtubesrc
        })
        .catch(err => console.log(err))
    },
    star() {
      this.star_point = Math.round(this.detail_movie.vote_average / 2)
    },
  },
  created() {
    this.getYoutube(this.detail_movie.id)
    this.star()
  }
}
</script>

<style>
.MovieDetailPage {
  display: flex;
}

.movieCard {
  margin: 7%;
}

.movieimgbox {
  position: relative;
}

.movieimg {
  border-radius: 0.5rem;
}

.heart {
  position: absolute;
  top: 2%;
  right: 3%;
  cursor: pointer;
}
</style>
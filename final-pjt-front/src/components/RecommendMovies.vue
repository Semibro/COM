<template>
  <div>
    <div class="RecommendMovies">
      <h2> {{ user_info.username }} 님의 취향저격 콘텐츠 </h2>
      <div class="wrapper">
        <div class="text">
          <p style="font-size: 30px; margin-right: 50px"> {{ movie.title }} </p>
          <!-- <span :data-text="movie.title" style="font-size: 30px;"></span> -->
        </div>
        <input type="checkbox">
        <div class="video">
          <iframe width="1000px" height="500px" :src="youtubesrc" loop muted autoplay></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = 'cab515bc24cb97ee07d658f5fd0aa1a7'

export default {
  name: 'RecommendMovies',
  props: {
    movie: Object,
  },
  data() {
    return {
      youtubeId: null,
      youtubesrc: null,
    }
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.movie.poster_path}`
    },
    user_info() {
      return this.$store.state.user_info
    }
  },
  methods: {
    toDetail(id) {
      this.$router.push({ name: 'detail', params: {id} })
    },
    getYoutube(id) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${id}/videos?&api_key=${API_KEY}`
      })
        .then(res => {
          // console.log(res.data.results[0].key)
          this.youtubeId = res.data.results[0].key
          const youtubesrc = `https://www.youtube.com/embed/${this.youtubeId}?autoplay=1&mute=1&controls=0&playlist=${this.youtubeId}`
          this.youtubesrc = youtubesrc
        })
        .catch(err => console.log(err))
    }
  },
  created() {
    this.getYoutube(this.movie.id)
  }
}
</script>

<style>
.RecommendMovies {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.RecommendMovies h2 {
  margin: 20px 0 0 70%;
}

.wrapper {
  margin: 0 0 0 20%;
  --color: white;
  --color-invert: rgb(64, 64, 64);
  --clip-path: circle(25px at right);
  --clip-path-hover: circle(300px at right);
  --clip-path-clicked: circle(800px at right);
  --duration: .4s;
  --timing-function: ease;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 500px;
}
.wrapper .video {
  height: 100vh;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 15px;
  -webkit-clip-path: var(--clip-path);
          clip-path: var(--clip-path);
  transition: -webkit-clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function), -webkit-clip-path var(--duration) var(--timing-function);
}
.wrapper .video iframe {
  position: fixed;
  background: #c4cbde;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}
.wrapper .text {
  position: relative;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: .2px;
  opacity: var(--opacity, 1);
  transition: opacity 0.3s var(--timing-function) 0.2s;
}
/* .wrapper .text::before, .wrapper .text::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: -1px;
  right: 25px;
  height: 0;
}
.wrapper .text::before {
  box-shadow: 26px 0 0 1px var(--color);
  right: var(--r, 100%);
  opacity: var(--opacity, 0);
  transition: right .5s ease-in, opacity .1s linear;
}
.wrapper .text::after {
  box-shadow: 26px 0 0 1px var(--color-invert);
  -webkit-clip-path: var(--clip-path);
          clip-path: var(--clip-path);
  transition: -webkit-clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function), -webkit-clip-path var(--duration) var(--timing-function);
}
.wrapper .text > span::before, .wrapper .text > span::after {
  content: attr(data-text);
  padding-left: 26px;
}
.wrapper .text > span::before {
  color: var(--color);
}
.wrapper .text > span::after {
  color: var(--color-invert);
  -webkit-clip-path: var(--clip-path);
          clip-path: var(--clip-path);
  transition: -webkit-clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function), -webkit-clip-path var(--duration) var(--timing-function);
  position: absolute;
  left: 0;
} */
.wrapper input {
  width: 400px;
  height: 100px;
  margin: auto;
  position: absolute;
  left: 0;
  right: 0;
  border-radius: 40px;
  z-index: 2;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
  cursor: pointer;
}
.wrapper input:focus {
  outline: 0;
}
.wrapper input:hover ~ .video {
  -webkit-clip-path: var(--clip-path-hover);
          clip-path: var(--clip-path-hover);
}
.wrapper input:hover ~ .text::before {
  --r: 25px;
  --opacity: 1;
}
.wrapper input:hover ~ .text::after {
  -webkit-clip-path: var(--clip-path-hover);
          clip-path: var(--clip-path-hover);
}
.wrapper input:hover ~ .text > span::after {
  -webkit-clip-path: var(--clip-path-hover);
          clip-path: var(--clip-path-hover);
}
.wrapper input:checked {
  width: 100%;
  height: 100%;
  border-radius: 0;
}
.wrapper input:checked ~ .video {
  -webkit-clip-path: var(--clip-path-clicked);
          clip-path: var(--clip-path-clicked);
}
.wrapper input:checked ~ .text {
  --opacity: 0;
  transition: opacity 0.3s var(--timing-function);
}
.wrapper input:checked ~ .text::after {
  -webkit-clip-path: var(--clip-path-clicked);
          clip-path: var(--clip-path-clicked);
}
.wrapper input:checked ~ .text > span::after {
  -webkit-clip-path: var(--clip-path-clicked);
          clip-path: var(--clip-path-clicked);
}
</style>
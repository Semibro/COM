<template>
  <div class="MoviesView">
    <div class="mermaid_video">
      <video src="@/assets/The_Little_Mermaid.mp4"
        autoplay muted loop
      ></video>
    </div>
    <div class="none"></div>
    
    <div class="content_box">
      <h1>취향저격 콘텐츠</h1>
      <div class="ppmovie">
        <PopularMovieList 
          v-for="(movie, index) in movie_list" :key="index"
          :movie="movie"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PopularMovieList from '@/components/PopularMovieList'

import _ from 'lodash'

export default {
  name: 'MoviesView',
  components: {
    PopularMovieList,
  },
  data() {
    return {
      movie_list: [],
    }
  },
  computed: {
    popularMovies() {
      return this.$store.state.popularMovies
    }
  },
  methods: {
    randomPick() {
      this.movie_list = _.sampleSize(this.popularMovies, 5)
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
    this.randomPick()
  },
}
</script>

<style scoped>
@keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translate3d(0, 100%, 0);
        }
        to {
            opacity: 1;
            transform: translateZ(0);
        }
    }

.MoviesView {
  position: relative;
}

.MoviesView h1 {
  color: rgba(255, 255, 255, 0.9);
  text-align: start;
  margin-left: 9%;
  width: 85vw;
  padding-bottom: 10px;
  /* border-bottom: 2px solid rgba(255, 255, 255, 0.2); */
}

.mermaid_video {
  /* margin-top: 50px; */
  position: absolute;
  top: -200px;
  height: 100%;
  overflow: hidden;
}

.mermaid_video video {
  width: 100vw;
  object-fit: cover;
  height: 100vh;
  opacity: 70%;
}

.none {
  visibility: hidden;
  height: 375px;
}

.ppmovie {
  display: flex;
  justify-content: center;
}

.content_box {
  z-index: 1;
  position: relative;
  animation: fadeInUp 1s;
}
</style>
<template>
  <div class="MoviesView">
    <div class="mermaid_video">
      <video src="@/assets/The_Little_Mermaid.mp4"
        autoplay muted loop
      ></video>
    </div>
    <div class="none"></div>
    <h1>취향저격 콘텐츠 :</h1>
    <div class="ppmovie">
      <PopularMovieList 
        v-for="(movie, index) in popularMovies" :key="index"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import PopularMovieList from '@/components/PopularMovieList'

export default {
  name: 'MoviesView',
  components: {
    PopularMovieList,
  },
  computed: {
    popularMovies() {
      return this.$store.state.popularMovies
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
  }
}
</script>

<style>
.MoviesView {
  position: relative;
}

.MoviesView h1 {
  text-align: start;
  margin-left: 7%;
}

.mermaid_video {
  /* margin-top: 50px; */
  position: absolute;
  top: -110px;
  height: 510px;
  overflow: hidden;
}

.mermaid_video video {
  width: 100vw;
  object-fit: cover;
  height: 100%;
  opacity: 70%;
}

.none {
  visibility: hidden;
  height: 390px;
}

.ppmovie {
  display: flex;
}
</style>
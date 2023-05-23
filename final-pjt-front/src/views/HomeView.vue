<template>
  <div class="home">
    <p class="hero">
      <img src="@/assets/background_img/hero.png">
    </p>
    <div class="hometext">
      <h1>{{ user_info.username }} 님의 취향저격 베스트 콘텐츠</h1>
      <p> {{ user_info.username }} 님이 좋아할만한 영화를 준비했어요 </p>
    </div>
    <RecommendMovies
      v-for="(movie, index) in recommendMovie" :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import RecommendMovies from '../components/RecommendMovies.vue'

import _ from 'lodash'

export default {
  name: 'HomeView',
  components: {
    RecommendMovies,
  },
  data() {
    return {
      recommendMovie: [],
    }
  },
  computed: {
    popularMovies() {
      return this.$store.state.popularMovies
    },
    user_info() {
      return this.$store.state.user_info
    }
  },
  methods: {
    getRecommendMovie() {
      this.recommendMovie = _.sampleSize(this.popularMovies, 1)
      // this.recommendMovie = _.sample(this.popularMovies)
    },
  },
  created() {
    this.getRecommendMovie()
  }
}
</script>

<style>
.hero {
  position: absolute; top: 0; left: 0;
  animation: shake 2.5s;
  animation-iteration-count: infinite;
  z-index: 0;
  width: 45%;
  overflow: hidden;
}

.hero img {
  max-width: 100%;
  height: auto;
  display: block;
}

@keyframes shake {
  0% { transform: translate(0px, 10px) rotate(0deg); }
  
  50% { transform: translate(0px, 0px) rotate(0deg); }
  
  100% { transform: translate(0px, 10px) rotate(0deg); }
}

.hometext {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin: 0 5% 0 0;
}

.hometext h1 {
  margin: 50px 0 0 0;
}
</style>
<template>
  <div class="home">
    <p class="hero">
      <img src="@/assets/background_img/hero.png">
    </p>
    <span class="recommend_title">
      <h1>%%% 님의 취향저격 베스트 콘텐츠</h1>
    </span>
    <span class="recommend_title" style="margin-bottom: 20px">
      당신이 좋아하는 "{{ randomMovieTitle }}" 과 비슷한 영화를 준비했어요!
    </span>
    <div class="recommend_content">
      <RecommendMovieCard
        v-for="(movie, index) in recommendMoviesList" :key="index"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import RecommendMovieCard from '../components/RecommendMovieCard.vue'
import _ from 'lodash'

export default {
  name: 'HomeView',
  components: {
    RecommendMovieCard
  },
  data() {
    return {
      randomMovieTitle: null,
    }
  },
  computed: {
    likeMovieList() {
      return this.$store.state.likeMovieList
    },
    recommendMoviesList() {
      return this.$store.state.recommendMovies
    }
  },
  methods: {
    recommendMovies() {
      const randomMovie = _.sample(this.likeMovieList, 1)
      // console.log(randomMovieId)
      const randomMovieItem = [randomMovie.id, randomMovie.title]
      this.randomMovieTitle = randomMovieItem[1]
      this.$store.dispatch('recommendMovies', randomMovieItem)
    }
  },
  created() {
    this.recommendMovies()
  }
}
</script>

<style>
.hero {
  position: absolute; top: 0; left: 0;
  animation: shake 2.5s;
  animation-iteration-count: infinite;
  z-index: 0;
}

@keyframes shake {
  0% { transform: translate(0px, 10px) rotate(0deg); }
  
  50% { transform: translate(0px, 0px) rotate(0deg); }
  
  100% { transform: translate(0px, 10px) rotate(0deg); }
}

.recommend_title {
  display: flex;
  justify-content: flex-end;
  margin: 0 10% 0 0;
}

.recommend_content {
  display: flex;
  justify-content: flex-end;
}
</style>
<template>
  <div class="RecommendView">
    <div class="titlewrap">
      <h2>{{ userinfo.username }} 님이 좋아한 </h2>
      <h1>"{{ selected_movie[0].title }}" 과 비슷한 영화를 골라봤어요!</h1>  
    </div>
    <br>
    <div class="movie_list">
      <PopularMovieList
        v-for="(movie, index) in recm_movie" :key="index"
        :movie="movie"
      />
    </div>
    <!-- <div v-for="(movie, index) in recm_movie" :key="index">
      {{ movie.poster_path }}
      {{ movie.title }}
    </div> -->
  </div>
</template>

<script>
import PopularMovieList from '../components/PopularMovieList.vue'

import _ from 'lodash'

export default {
  name: 'RecommendView',
  components: {
    PopularMovieList,
  },
  data() {
    return {
      recm_movie: [],
      like_movie: [],
      movieId: null,
      selected_movie: [],
    }
  },
  computed: {
    recommendMovies() {
      return this.$store.state.recommendMovies
    },
    userinfo() {
      return this.$store.state.user_info
    },
    getPopularMovies() {
      return this.$store.state.popularMovies
    },
  },
  methods: {
    randomMovie() {
      this.recm_movie = _.sampleSize(this.recommendMovies, 5)
    },
    like_movies() {
      const movielist = this.$store.state.popularMovies
      const lst = []
      movielist.forEach(movie => {
        Object.values(movie.like_users).forEach(ele => {
          if (this.userinfo.pk === ele) {
            lst.push(movie)
          }
        })
      })
      this.selected_movie = _.sampleSize(lst, 1)
      return this.selected_movie[0].id
    }
  },
  created() {
    this.$store.dispatch('getPopularMovies')
    this.$store.dispatch('getUserInfo')
    this.$store.dispatch('getRecommendMovies', this.like_movies())
  },
  mounted() {
    this.randomMovie()
  }
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

.RecommendView {
  margin-top: 3%;
  height: 100vh;
  /* animation: fadeInUp 1s; */
}

.titlewrap {
  animation: fadeInUp 1s;
}

.movie_list {
  margin-top: 2%;
  margin-left: 7%;
  display: flex;
  overflow: scroll;
  animation: fadeInUp 2s;
}
</style>
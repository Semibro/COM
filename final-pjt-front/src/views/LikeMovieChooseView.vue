<template>
  <div>
    <h1>좋아하는 영화를 고르세요.</h1>
    <MovieCard
      v-for="(movie, index) in movieList" :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const API_KEY = 'b87676597510090177f5217ea5f4d280'

export default {
  name: 'LikeMovieChooseView',
  data() {
    return {
      movieList: null,
    }
  },
  components: {
    MovieCard,
  },
  created() {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/popular?language=ko-KR&page=1&api_key=${API_KEY}`
    })
      .then(res => {
        this.movieList = res.data.results
        console.log(this.movieList)
      })
      .catch(err => console.log(err))
  },
}
</script>

<style>

</style>
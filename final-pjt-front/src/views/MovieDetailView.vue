<template>
  <div>
    <MovieDetailPage :detail_movie="detail_movie"/>
  </div>
</template>

<script>
import MovieDetailPage from '@/components/MovieDetailPage'

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetailPage,
  },
  computed: {
    detail_movie() {
      return this.$store.state.detail_movie
    },
  },
}
</script>
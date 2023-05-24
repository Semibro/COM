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
  created() {
    this.$store.dispatch('toDetail', this.$route.params.id)
  }
}
</script>
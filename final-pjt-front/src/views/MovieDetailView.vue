<template>
  <div>
    <h1>영화 디테일 페이지</h1>
    {{ detail_movie }}
  </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
  computed: {
    detail_movie() {
      return this.$store.state.detail_movie
    }
  },
  created() {
    this.$store.dispatch('toDetail', this.$route.params.id)
  }
}
</script>

<style>

</style>
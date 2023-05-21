<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'MovieDetailView',
  created() {
    this.$store.dispatch('getCreditList', this.$route.params.id)
  }
}
</script>

<style>

</style>
<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  created() {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movie_id}/recommendations?language=ko-KR&page=1&api_key=b87676597510090177f5217ea5f4d280`
    })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>
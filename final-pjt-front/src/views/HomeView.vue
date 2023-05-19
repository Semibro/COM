<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <HelloWorld msg="모든 인류 구성원의 천부의"/>
  </div>
</template>

<script>
import axios from 'axios'

// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
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

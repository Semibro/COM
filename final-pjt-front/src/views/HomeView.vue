<template>
  <div class="home">
    <p class="hero">
      <img src="@/assets/background_img/hero.png">
    </p>
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <HelloWorld msg="모든 인류 구성원의 천부의"/>
  </div>
</template>

<script>
import axios from 'axios'

API_URL = 'http://127.0.0.1:8000/'

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

<style>
.home {
}

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
</style>

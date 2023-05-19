<template>
  <div id="app">
    <nav>
      <img src="@/assets/logo.png" class="logo" @click="toHome">
      <div class="menu">
        <router-link to="/">Home</router-link>
        <router-link to="/movies">Movies</router-link>
        <router-link to="/profile">Profile</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import fullscreen from 'vue-fullscreen'
import Vue from 'vue'

Vue.use(fullscreen)

export default {
  name: 'App',
  methods: {
    toHome() {
      console.log(1)
      this.$router.push({ name: 'home' }).catch(()=>{})
    }
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
#app {
  /* font-family: 'Varela Round', sans-serif; */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url('@/assets/background_img/home_bg.png');
  height: 100vh;
  width: 100vw;
}

body {
  margin: 0;
}

.logo {
  margin-left: 80px;
  width: 255px;
  cursor: pointer;
}

nav {
  padding: 30px;
  display: flex;
  justify-content: space-between;

}

nav a {
  font-weight: bold;
  color: white;
  opacity: 50%;
  text-underline-offset: 7px;
  padding: 0 30px;
}

nav a:hover {
  opacity: 100%;
}

nav a.router-link-exact-active {
  opacity: 100%;
}
</style>

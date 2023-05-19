<template>
  <div id="app">
    <p class="hero">
      <img src="@/assets/background_img/hero.png">
    </p>
    <nav>
      <img src="@/assets/logo.png" class="logo" @click="toHome">
      <div class="menu">
        <router-link to="/">Home</router-link>
        <router-link to="/movies">Movies</router-link>
        <router-link to="/profile">Profile</router-link>
        <button class="language">KOR</button> |
        <button class="language" style="opacity: 50%" @click="clickENG">ENG</button>
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
    },
    clickENG() {
      alert('준비 중입니다🙏🏼')
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
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@300&display=swap');

#app {
  font-family: 'IBM Plex Sans KR', sans-serif;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-image: url('@/assets/background_img/home_bg.png');
  height: 100vh;
  width: 100vw;
  position: relative;
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
  z-index: 2;
  letter-spacing: 1.5px;
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

.menu {
  color: white;
}

.language {
  cursor: pointer;
  border: 0;
  background-color: transparent;
  color: white; 
}
</style>

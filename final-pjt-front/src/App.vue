<template>
  <div id="app">
    <nav>
      <img src="@/assets/logo.png" class="logo">
      <div class="menu">
        <router-link to="/">Home</router-link>
        <router-link to="/movies">Movies</router-link>
        <router-link to="/login">Login</router-link>
        <router-link to="/signup">Signup</router-link>
        <router-link to="/profile">Profile</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
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
  height: 100%;
  width: 100%;
  position: relative;
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
  padding: 0 25px;
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

<template>
  <div id="app">
    <nav>
      <span v-if="isLogin">
        <router-link to="/">Home</router-link> |
        <router-link to="/movies">Movies</router-link> |
        <router-link :to="{ name: 'profile', params: { username: username } }">Profile</router-link> |
        <router-link to="/#" @click.native="logout">Logout</router-link> |
      </span>

      <span v-else>
        <router-link to="/">Home</router-link> |
        <router-link to="/movies">Movies</router-link> |
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">Signup</router-link>
      </span>
    </nav>
    <router-view @login="isLogin=true" />
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      isLogin: false,
    }
  },
  computed: {
    username() {
      return this.$store.state.user_info.username
    }
  },
  methods: {
    logout() {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'login' })
    }
  },
  created() {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
    this.$store.dispatch('getUserInfo')
  },
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
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

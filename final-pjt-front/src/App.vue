<template>
  <div id="app">
    <div class="navwrap">
      <img src="@/assets/logo.png" class="logo">
      <nav>
        <span v-if="isLogin" class="menu">
          <router-link to="/">Home</router-link>
          <router-link to="/movies">Movies</router-link>
          <router-link :to="{ name: 'profile', params: { username: username } }">Profile</router-link>
          <router-link to="/#" @click.native="logout">Logout</router-link>
        </span>

        <span v-else>
          <router-link to="/">Home</router-link>
          <router-link to="/movies">Movies</router-link>
          <router-link to="/login">Login</router-link>
          <router-link to="/signup">Signup</router-link>
        </span>
      </nav>
    </div>
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

        console.log(
        '%c\n' +
        '                                                                        ,,\n' +
        '                                                                       /  ,\n' +
        '                                                                      /   /\n' +
        '                                                                     /   /\n' +
        '                                                                    /   /\n' +
        '     _______________________________                               /   /\n' +
        '    ⎢                               ⎥                              /   /\n' +
        '    ⎢  우리 집에서 영화 보고 갈래?   ⎥                            /   /\n' +
        '    ⎢____    _______________________⎥                            /   /\n' +
        '          \\/    ,      ,,                                      /   /\n' +
        '               /'+'%c@'+'%c\\____/'+'%c@'+'%c \\                                ____/   /\n' +
        '              /           \\                         _____/        /__\n' +
        '        /" \\ / •    •      \\                     __/             /  '+'%c@@'+'%c"\\\n' +
        '        \\    '+'%c@@'+'%c  ㅅ  '+'%c@@'+'%c     /___             ___/                /    _/\n' +
        '       /" \\   \\                 \\__________/                    |__/ "\\\n' +
        '       \\   \\                                                   /      /\n' +
        '        \\    \\  __                                                  _/\n' +
        '         \\                                                       __/\n' +
        '           \\_                                             ______/\n' +
        '              \\ ___                                    __/\n' +
        '                    \\__                             __/\n' +
        '                        \\_____                _____/\n' +
        '                              \\______________/\n' +
        '\n',

        'font-weight: bold;',
        'font-weight: bold; color: #ff7777',
        'font-weight: bold;',
        'font-weight: bold; color: #ff7777',
        'font-weight: bold;',
        'font-weight: bold; color: #ff7777',
        'font-weight: bold;',
        'font-weight: bold; color: #ff7777',
        'font-weight: bold;',
        'font-weight: bold; color: #ff7777',
        'font-weight: bold;'
    );
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

.navwrap {
  display: flex;
  justify-content: space-between;
}

.logo {
  margin-left: 7%;
  width: 13vw;
  cursor: pointer;
  margin-top: 10px;
}

nav {
  padding: 30px 5% 30px 30px;
  display: flex;
  z-index: 2;
  letter-spacing: 1.2px;
}

nav a {
  font-weight: bold;
  color: white;
  opacity: 50%;
  text-underline-offset: 7px;
  padding: 0 0 0 60px;
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
</style>

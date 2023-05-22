<template>
  <div>
    <h1>LogIn Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/api/token/',
        data: payload,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.access)
        this.$emit('login')
        this.$router.push({name: 'home'})
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

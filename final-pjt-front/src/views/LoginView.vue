<template>
  <div class="LoginView">
    <div class="loginform">
      <h1>LogIn</h1>
      <form @submit.prevent="logIn">
        <label for="username"></label>
        <input class="login_input" type="text" id="username"
          v-model="username" placeholder="ID"
        >
        <br>

        <label for="password"></label>
        <input class="login_input" type="password" id="password"
          v-model="password" placeholder="PASSWORD"
        >
        <br>

        <input type="submit" value="LogIn" class="submit">
      </form>
    </div>
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

<style scoped>
@keyframes fadeInUp {
        0% {
            opacity: 0;
            transform: translate3d(0, 100%, 0);
        }
        to {
            opacity: 1;
            transform: translateZ(0);
        }
    }

.LoginView {
  background-image: url('@/assets/background_img/Background1.png');
  height: 100vh;
  display: flex;
  justify-content: center;
  animation: fadeInUp 1s;
}

.loginform {
  animation: fadeInUp 1.5s;
  padding-top: 9%;
  text-align: start;
}

.login_input {
  border: 0;
  border-radius: 0.5rem;
  height: 35px;
  width: 250px;
  padding-left: 15px;
}

#username {
  border-bottom: 1px solid lightgray;
}

.submit {
  margin-top: 10px;
  border: 0;
  border-radius: 0.5rem;
  height: 35px;
  width: 267px;
  background-color: rgba(199, 51, 51, 0.65);
  color: white;
  cursor: pointer;
}

.submit:hover {
  background-color: rgba(199, 51, 51);
}
</style>
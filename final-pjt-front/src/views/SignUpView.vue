<template>
  <div class="SignUpView">
    <div class="loginform">
      <h1>Sign Up</h1>
      <form @submit.prevent="signUp">
        <label for="username"></label>
        <input class="login_input" type="text" id="username"
          v-model="username" placeholder="ID"
        >
        <br>

        <label for="password1"></label>
        <input class="login_input" type="password" id="password1"
          v-model="password1" placeholder="PASSWORD"
        >
        <br>

        <label for="password2"></label>
        <input class="login_input" type="password" id="password2"
          v-model="password2" placeholder="CONFIRM PASSWORD"
        >
        <br>
        <input type="submit" value="SignUp" class="submit">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload)
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

.SignUpView {
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

#password1 {
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
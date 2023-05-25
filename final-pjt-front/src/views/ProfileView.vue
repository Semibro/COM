<template>
  <div>
    <div class="userinfo_box">
      <img src="@/assets/gamsung.png" class="profile_pic">
      <div class="user_info">

        <div class="user_title">
          <h1> {{ masterOfProfile }} 님</h1>
          <!-- 팔로우 버튼 -->
          <span v-if="user_info.username != masterOfProfile">
            <span v-if="follow_check">
              <button @click="followUser(masterOfProfile)">
                <span class="iconbox">
                  <img src="@/assets/icon/cancel.png" class="icon_sm">
                  <img src="@/assets/icon/cancel_black.png" class="icon_sm follow">
                </span>
              </button>
            </span>
            <span v-else>
              <button @click="followUser(masterOfProfile)">
                <span class="iconbox">
                  <img src="@/assets/icon/follow.png" class="icon">
                  <img src="@/assets/icon/follow_black.png" class="icon follow">
                </span>
              </button>
            </span>
          </span>
          <!-- 팔로우 버튼 끝 -->
        </div>

        <div class="insta_st">
          <div class="tap">
            <p class="no_margin bold">{{ like_movie_list.length }}</p>
            <p class="no_margin">좋아요</p>
          </div>
          <div class="tap">
            <p class="no_margin bold">{{ getFollowingsCount }}</p>
            <p class="no_margin">팔로워</p>
          </div>
          <div class="tap">
            <p class="no_margin bold">{{ getFollowersCount }}</p>
            <p class="no_margin">팔로잉</p>
          </div>
          
        </div>

      </div>
    </div>


    <br><br>
    <div v-for="(movie, index) in like_movie_list" :key="index">
      {{ movie }}
      <br><br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      like_movie_list: [],
      real_user_info: [],
      masterOfProfile: this.$route.params.username,
      profile_data: [],
      follow_check: null,
    }
  },
  computed: {
    user_info() {
      return this.$store.state.user_info
    },
    popularMovies() {
      return this.$store.state.popularMovies
    },
    getFollowingsCount() {
      if (this.real_user_info && this.real_user_info.followings) {
        return this.real_user_info.followings.length;
      }
      return 0;
    },
    getFollowersCount() {
      if (this.real_user_info && this.real_user_info.followers) {
        return this.real_user_info.followers.length;
      }
      return 0;
    },
  },
  methods: {
    is_follow() {
      const user = this.$store.state.user_info
      let flag = 1
      this.real_user_info.followings.forEach(follower => {
        if (follower.id === user.pk) {
          this.follow_check = true
          flag = 2
        }
      })
      if (flag === 1) {
        this.follow_check = false
      }
    },
    getProfile() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/profile/${this.$route.params.username}`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.real_user_info = res.data
          this.like_movie_list = res.data.like_movies
          this.is_follow()
        })
        .catch(err => {
          console.log(err)
        })
    },
    followUser(username) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/profile/${username}/follow/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.profile_data = res.data
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getProfile()
    this.$store.dispatch('getUserInfo')
  },
  mounted() {
    this.is_follow()
  },
}
</script>

<style>
.userinfo_box {
  margin-top: 30px;
  display: flex;
  align-items: center;
  height: 50vh;
  background-color: rgba(255, 255, 255, 0.2);
}

.profile_pic {
  border-radius: 0.5rem;
  width: 300px;
  height: 300px;
  margin-left: 7%;
}

.user_title {
  margin-left: 50px;
  display: flex;
  align-items: center;
}

button {
  cursor: pointer;
  color: white;
  font-weight: bold;
  margin-left: 15px;
  padding-left: 10px;
  padding-right: 10px;
  height: 30px;
  background-color: rgba(255, 255, 255, 0.4);
  border: none;
  border-radius: 0.5rem;
  width: 40px;
}

.iconbox {
  position: relative;
}

.icon {
  width: 20px;
  height: 20px;
}

.icon_sm {
  width: 13px;
}

.follow {
  position: absolute;
  right: 0;
  opacity: 0;
}

.follow:hover {
  opacity: 70%;
}

.insta_st {
  display: flex;
  margin-left: 30px;
}

.tap {
  margin: 0 15px;
}

.no_margin {
  margin: 0;
}

.bold {
  font-weight: bold;
}
</style>
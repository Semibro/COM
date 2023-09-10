<template>
  <div class="MovieDetailPage">
    <div class="movieCard">
      <div class="movieimgbox">
        <img :src="imgurl" class="movieimg">
        <img src="@/assets/icon/full_heart.png" @click="likeMovie(detail_movie.id)"
          class="heart" v-if="isLike"
        >
        <div class="heart" v-else>
          <img src="@/assets/icon/bin_heart.png" @click="likeMovie(detail_movie.id)"
            class="bin_heart"
          >
          <img src="@/assets/icon/full_heart.png" @click="likeMovie(detail_movie.id)"
            class="full_heart"
          >
        </div>
      </div>
      <div class="title_text">
        <div class="only_title">
          <h3 class="real_title">{{ detail_movie.title }}</h3>
          <div class="video">
            <iframe width="1000px" height="500px" :src="youtubesrc" loop muted autoplay></iframe>
          </div>
        </div>
        <div class="point_5" v-if="star_point===5">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
        <div class="point_4" v-if="star_point===4">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
        <div class="point_3" v-if="star_point===3">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
        <div class="point_2" v-if="star_point===2">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
        <div class="point_1" v-if="star_point===1">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
        <div class="point_0" v-if="star_point===0">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ detail_movie.vote_count }})
        </div>
      </div>
    </div>
    <div class="movie_content_wrap">
      <div class="movie_content">
        <div class="datewrap">
          <img src="@/assets/icon/calendar.png" class="icon">
          <div class="date">
            개봉 : {{ detail_movie.release_date }}
          </div>
        </div>
        <div class="overview">
          {{ detail_movie.overview }}
        </div>
        <div class="createReviewForm">
          <h2>
            <img src="@/assets/icon/pencil.png" class="icon">
            리뷰쓰기
          </h2>
          <form @submit.prevent="createReview">
            <label for="content"></label>
            <div class="review_form_box">
              <select name="user_rate" id="user_rate" v-model="rate_data">
                <option class="option" value="1">⭐</option>
                <option class="option" value="2">⭐⭐</option>
                <option class="option" value="3">⭐⭐⭐</option>
                <option class="option" value="4">⭐⭐⭐⭐</option>
                <option class="option" value="5">⭐⭐⭐⭐⭐</option>
              </select>
              <input type="text" v-model="inputdata"
                placeholder="영화와 무관한 댓글이나 스포일러, 악플은 경고조치 없이 삭제되며 징계 대상이 될 수 있습니다."
              >
            </div>
            <!-- <input type="number" v-model="rate_data"> -->
            <input type="submit" style="display: none">
          </form>
          <br>
          <div v-for="(review, index) in reviews" :key="index" class="reviewbox">
            <span class="username" @click="toProfile(review.user)">{{ review.user }}</span> :
            <span @click="toReviewDetail(review.id, review.user_id)" class="review_content">
              {{ review.content }}
              <span class="point_5" v-if="review.rate===5">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
              </span>
              <span class="point_4" v-if="review.rate===4">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
              </span>
              <span class="point_3" v-if="review.rate===3">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
              </span>
              <span class="point_2" v-if="review.rate===2">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
              </span>
              <span class="point_1" v-if="review.rate===1">
                <img src="@/assets/icon/full_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
              </span>
              <span class="point_0" v-if="review.rate===0">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
                <img src="@/assets/icon/bin_star.png" class="star_user">
              </span>
              <!-- {{ review.rate }} -->
            </span>
            <span class="created_at">
              {{ review.created_at.substr(0, 10) }}
            </span>
            <!-- <button @click="toReviewDetail(review.id, review.user_id)">DETAIL</button> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const API_KEY = 'api_key'

export default {
  name: 'MovieDetailPage',
  props: {
    detail_movie: Object,
  },
  data() {
    return {
      youtubeId: null,
      youtubesrc: null,
      star_point: null,
      isLike: false,
      inputdata: null,
      rate_data: 1,
      reviews: [],
      written_user: null,
    }
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.detail_movie.poster_path}`
    },
    user_info() {
      return this.$store.state.user_info
    },
  },
  methods: {
    likeMovie(id) {
      this.$store.dispatch('likeMovie', id)
      this.isLike = !this.isLike
      console.log(this.isLike)
    },
    getYoutube(id) {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${id}/videos?&api_key=${API_KEY}`
      })
        .then(res => {
          console.log(res.data.results[0].key)
          this.youtubeId = res.data.results[0].key
          const youtubesrc = `https://www.youtube.com/embed/${this.youtubeId}?autoplay=1&mute=1&controls=0&playlist=${this.youtubeId}`
          this.youtubesrc = youtubesrc
        })
        .catch(err => console.log(err))
    },
    star() {
      this.star_point = Math.round(this.detail_movie.vote_average / 2)
    },
    heart() {
      const user = this.user_info.pk
      let flag = 1
      this.detail_movie.like_users.forEach(user_id => {
        if (user_id === user) {
          flag = 2
          this.isLike = true
        }
      })
      if (flag === 1) {
        this.isLike = false
      }
    },
    createReview() {
      const content = this.inputdata
      const rate = Number(this.rate_data)
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/`,
        data: { content, rate },
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(res => {
            console.log(res)
            this.getReviewDetail()
            this.inputdata = null
            this.rate_data = 1
        })
        .catch(err => console.log(err))
    },
    getReviewDetail() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.id}/reviews/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.reviews = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    toReviewDetail(id, user_id) {
      // console.log(this.$route.params.id)
      const movie = this.$route.params.id
      // console.log(id)
      const params_id = {movie_id: movie, review_id: id, user_id: user_id,}
      this.$router.push({ name: 'review_detail', params: params_id })
    },
    toProfile(username) {
      this.$router.push({ name: 'profile', params: {username} })
    },
  },
  created() {
    this.getYoutube(this.detail_movie.id)
    this.star()
    this.heart()
    this.$store.dispatch('getUserInfo')
    this.$store.dispatch('toDetail', this.$route.params.id)
    this.getReviewDetail()
  }
}
</script>

<style scoped>
.MovieDetailPage {
  display: flex;
  height: 100vh;
}

.movieCard {
  margin: 7%;
}

.movieimgbox {
  position: relative;
}

.movieimg {
  border-radius: 0.5rem;
}

.only_title {
  --clip-path: circle(0.1px);
  --clip-path-hover: circle(50vw);
  --clip-path-clicked: circle(50vw);
  --timing-function: ease;
}

.only_title .video {
  width: 10vw;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 15px;
  -webkit-clip-path: var(--clip-path);
          clip-path: var(--clip-path);
  transition: -webkit-clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function);
  transition: clip-path var(--duration) var(--timing-function), -webkit-clip-path var(--duration) var(--timing-function);
}

.only_title .video iframe {
  position: fixed;
  background: #c4cbde;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}

.real_title {
  border-radius: 0.5rem;
  -webkit-appearance: none;
     -moz-appearance: none;
          appearance: none;
  cursor: pointer;
}

.real_title:focus {
  outline: 0;
}

.real_title:hover ~ .video {
  -webkit-clip-path: var(--clip-path-hover);
          clip-path: var(--clip-path-hover);
}

.heart {
  position: absolute;
  top: 2%;
  right: 3%;
  cursor: pointer;
}

.bin_heart {
  position: relative;
}

.full_heart {
  position: absolute;
  top: 2%;
  right: 3%;
  opacity: 0;
}

.heart:hover > .full_heart {
  opacity: 1;
  transition: opacity 0.3s;
}

.star {
  margin: 0 2px;
  width: 30px;
}

.star_user {
  margin: 0 2px;
  width: 16px;
}

.movie_content_wrap {
  width: 65%;
  height: 80vh;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 0.5rem;
}

.video {
  z-index: 10;
  position: relative;
}

.movie_content {
  font-weight: bold;
  text-align: start;
  color: white;
  opacity: 100%;
  margin: 4% 5%;
}

.datewrap {
  display: flex;
  border-bottom: 1px solid rgba(255, 255, 255, 0.4);
  padding-bottom: 15px;
  margin-bottom: 3%;
  padding-left: 2%;
}

.date {
  font-size: 20px;
  margin-left: 7px;
}

.overview {
  padding-left: 2%;
  line-height: 35px;
  font-size: 17px;
  margin-bottom: 5%;
}

.username {
  cursor: pointer;
}

.username:hover {
  color: rgb(48, 48, 48);
}

.createReviewForm {
  padding-left: 2%;
}

.createReviewForm h2 {
  margin-bottom: 10px;
}

.icon {
  width: 27px;
  height: 27px;
}

input {
  width: 100%;
  height: 35px;
  opacity: 50%;
  border-radius: 0.5rem;
  border: transparent;
  padding-left: 15px;
}

select {
  width: 115px;
  height: 35px;
  opacity: 50%;
  border-radius: 0.5rem;
  border: transparent;
  margin-right: 10px;
}

.reviewbox {
  margin-bottom: 10px;
}

.created_at {
  opacity: 40%;
}

.review_content:hover {
  color: rgb(48, 48, 48);
  cursor: pointer;
  font-weight: bold;
}

.review_form_box {
  display: flex;
}
</style>
<template>
  <div class="ReviewDetailView">
    <div class="movieCard">
      <div class="movieimgbox">
        <img :src="imgurl" class="movieimg">
      </div>
      <div class="title_text">
        <div class="only_title">
          <h3 class="real_title">{{ movie.title }}</h3>
        </div>
        <div class="point_5" v-if="star_point===5">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
        <div class="point_4" v-if="star_point===4">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
        <div class="point_3" v-if="star_point===3">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
        <div class="point_2" v-if="star_point===2">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
        <div class="point_1" v-if="star_point===1">
          <img src="@/assets/icon/full_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
        <div class="point_0" v-if="star_point===0">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          <img src="@/assets/icon/bin_star.png" class="star">
          ({{ movie.vote_count }})
        </div>
      </div>
    </div>
    <div class="movie_content_wrap">
      <div class="movie_content">
        <h2> {{ review.content }} </h2>
        <div v-if="this.$route.params.user_id === this.user_info.pk">
          <button @click="deleteReview(review.id)">DELETE</button>
        </div>
        <div class="createReviewForm">
          <h2>
            <img src="@/assets/icon/pencil.png" class="icon">
            댓글쓰기
          </h2>
          <form @submit.prevent="createComment">
            <label for="content"></label>
            <div class="review_form_box">
              <input type="text" v-model="inputdata"
                placeholder="영화와 무관한 댓글이나 스포일러, 악플은 경고조치 없이 삭제되며 징계 대상이 될 수 있습니다."
              >
            </div>
          </form>
          <br>
          <div v-for="(comment, index) in comments" :key="index" class="reviewbox">
            <span class="username" @click="toProfile(comment.user)">{{ comment.user }}</span> :
            <span @click="toReviewDetail(review.id, review.user_id)" class="review_content">
              {{ comment.content }}
            </span>
            <button @click="deleteComment(comment.id)">DELETE</button>
            <span class="created_at">
              {{ review.created_at.substr(0, 10) }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewDetailView',
  data() {
    return {
      review: null,
      inputdata: null,
      comments: null,
      movie: null,
      star_point: null,
    }
  },
  computed: {
    user_info() {
      return this.$store.state.user_info
    },
    popularMovies() {
      return this.$store.state.popularMovies
    },
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.movie.poster_path}`
    },
  },
  methods: {
    getReviewDetail() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.review = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createComment() {
      const content = this.inputdata
      if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/`,
        data: { content },
        headers: {
          Authorization: `Bearer ${ token }`
        }
      })
        .then(() => {
            this.getCommentList()
            this.inputdata = null
        })
        .catch(err => console.log(err))
    },
    getCommentList() {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(res => {
          this.comments = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment(id) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${this.$route.params.review_id}/comment/${id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(() => {
          this.getCommentList()
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteReview(id) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'delete',
        url: `${API_URL}/movies/${this.$route.params.movie_id}/${id}/`,
        headers: {
          Authorization: `Bearer ${ token }`
        },
      })
        .then(() => {
          const movie_id = {id: this.$route.params.movie_id}
          this.$router.push({name: 'detail', params: movie_id})
        })
        .catch(err => {
          console.log(err)
        })
    },
    toProfile(username) {
      this.$router.push({ name: 'profile', params: {username} })  // 프로필 이동
    },
    getMovie() {
      const movie_id = this.$route.params.movie_id
      this.popularMovies.forEach(movie => {
        if (movie.id == movie_id) {
          this.movie = movie
          return
        }
      })
    },
    star() {
      this.star_point = Math.round(this.movie.vote_average / 2)
    },
  },
  created() {
    this.getReviewDetail()
    this.getCommentList()
    this.$store.dispatch('getUserInfo')
    this.getMovie()
    this.star()
  }
}
</script>

<style scoped>
.pointer {
  cursor: pointer;
}

.ReviewDetailView {
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
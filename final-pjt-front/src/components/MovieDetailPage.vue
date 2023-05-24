<template>
  <div class="MovieDetailPage">
    <div class="movieCard">
      <div class="movieimgbox">
        <img :src="imgurl" class="movieimg">
        <!-- <div class="video">
          <iframe width="1000px" height="500px" :src="youtubesrc" loop muted autoplay></iframe>
        </div> -->
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
        {{ detail_movie.release_date }}
        {{ detail_movie.overview }}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'
const API_KEY = 'cab515bc24cb97ee07d658f5fd0aa1a7'

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
    }
  },
  computed: {
    imgurl() {
      return `https://image.tmdb.org/t/p/w300/${this.detail_movie.poster_path}`
    },
    user_info() {
      return this.$store.state.user_info
    }
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
          // console.log(res.data.results[0].key)
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
  },
  created() {
    this.getYoutube(this.detail_movie.id)
    this.star()
    this.heart()
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style scoped>
.MovieDetailPage {
  display: flex;
}

.movieCard {
  margin: 7%;
}

.movieimgbox {
  position: relative;
  /* --clip-path: circle(0.1px);
  --clip-path-hover: circle(50vw);
  --clip-path-clicked: circle(50vw);
  --timing-function: ease; */
}

.only_title {
  --clip-path: circle(0.1px);
  --clip-path-hover: circle(50vw);
  --clip-path-clicked: circle(50vw);
  --timing-function: ease;
}

/* .movieimgbox:hover .heart {
  opacity: 0;
} */

.only_title .video {
  width: 10vw;
  /* height: 100vh; */
  /* overflow: hidden; */
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
  color: white;
  opacity: 100%;
}
</style>
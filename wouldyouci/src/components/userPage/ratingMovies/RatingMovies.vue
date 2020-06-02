<template>
  <div>
    <div v-if="CinemaList" class="ratingMovies">
      <div class="chip">
        <v-chip
          color="#998DE8"
          text-color="#FFFFFF"
        >
          <v-avatar tile>
            <v-icon>
              fas fa-film
            </v-icon>
          </v-avatar>
          내가 평가한 영화 - {{CinemaList.length}} 편
        </v-chip>
      </div>
      <v-container class="moviesContainer">
        <v-row dense>
          <v-col cols="12">
            <v-card
              class="movieCard"
              color="#385F73"
              dark
              v-for="(movie, idx) in CinemaList"
              :key="idx"
            >
              <v-list-item>
                <v-avatar
                  class="ma-3"
                  size="auto"
                  tile
                >
                  <v-img :src="movie.movie.poster">
                  </v-img>
                </v-avatar>
                <div>
                  <v-card-subtitle>
                    {{ movie.movie.name }}
                  </v-card-subtitle>
                  <v-card-actions>
                    <v-rating
                      v-model="movie.score"
                      small
                      half-increments
                      @input="changeRating({'ratingId': movie.id,'movieId': movie.movie.id, 'rating':movie.score})">
                    </v-rating>
                  </v-card-actions>
                </div>
              </v-list-item>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <div class="noReco" v-else>
      아직 평가한 영화가 없습니다.
    </div>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: 'RatingMovies',
  props: ["CinemaList"],
  methods: {
    goDetail() {
      router.push('/movieDetail')
    },
    changeRating(info) {
      const axios = require("axios");
      const HOST = process.env.VUE_APP_SERVER_HOST;
      const token = sessionStorage.getItem('jwt');
      const options = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      const data = {
        score: info.rating,
        movie: info.movieId
      }
      axios.patch(`${HOST}/movie/rating/${info.ratingId}/`, data, options)
        .then(res => res)
        .catch(err => err)
    }
  }
}
</script>

<style src="./RatingMovies.css" scoped></style>
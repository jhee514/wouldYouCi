<template>
  <div class="ratingMovies">
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
                    @click="changeRating">
                  </v-rating>
                </v-card-actions>
              </div>
            </v-list-item>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
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
    changeRating() {
      console.log('???')
    }
  }
}
</script>

<style src="./RatingMovies.css" scoped></style>
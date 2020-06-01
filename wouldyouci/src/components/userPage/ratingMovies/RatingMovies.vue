<template>
  <div class="ratingMovies">
    <v-container>
      <v-row dense>
        <v-col cols="12">
          <v-card
            color="#385F73"
            dark
          >
            <v-list-item>
              <v-avatar
                class="ma-3"
                size="auto"
                tile
              >
                <v-img src="https://movie-phinf.pstatic.net/20161123_188/1479862185516tYkKO_JPEG/movie_image.jpg">
                </v-img>
              </v-avatar>
              <div>
                <v-card-title>
                  라라랜드
                </v-card-title>
                <v-card-actions>
                  <v-rating
                    small
                    half-increments>
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
    }
  }
}
</script>

<style src="./RatingMovies.css" scoped></style>
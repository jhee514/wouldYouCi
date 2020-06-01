<template>
  <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="90vw"
    style="margin-top:2vh; margin-bottom: 2vh;"
  >
    <v-slide-group
      dark
      class="pa-4"
      active-class="success"
      v-if="CinemaList && CinemaList.length"
    >
      <v-slide-item
        v-for="(title, idx) in CinemaList"
        :key="idx"
      >
        <v-card
          class="ma-4"
          height="auto"
          width="38vw"
          style="margin-right:2vh"
          @click="goDetail"
        >
          <v-img 
            src="https://movie-phinf.pstatic.net/20161123_188/1479862185516tYkKO_JPEG/movie_image.jpg"
            height="25vh"
            width="38vw"
          >
          </v-img>
          <v-card-text>{{ title }}</v-card-text>
        </v-card>
      </v-slide-item>
    </v-slide-group>
    <v-card
      v-else
      class="ma-4"
      height="20vh"
      width="90vw"
      style="margin-right:2vh"
    >
      <div>
        해당 콘텐츠가 없습니다.
      </div>
    </v-card>
  </v-sheet>
</template>

<script>
import router from "@/router";

export default {
  name: 'MovieList',
  props: ["CinemaList"],
  methods: {
    goDetail() {
      router.push('/movieDetail')
    }
  }
}
</script>

<style src="./MovieList.css" scoped></style>
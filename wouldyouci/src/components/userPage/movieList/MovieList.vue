<template>
  <div>
    <v-slide-group
      dark
      class="pa-4"
      active-class="success"
      v-if="CinemaList && CinemaList.length"
    >
      <v-slide-item
        v-for="(cinema, idx) in CinemaList"
        :key="idx"
      >
        <v-card
          height="auto"
          width="40vw"
          style="margin-right:2vh"
          @click="goDetail(cinema.id)"
        >
          <v-img 
            :src="cinema.poster"
            height="30vh"
            width="40vw"
          >
          </v-img>
          <v-card-text>{{ getMovieName(cinema.name) }}</v-card-text>
        </v-card>
      </v-slide-item>
    </v-slide-group>
    <v-card
      v-else
      class="noContent"
      height="20vh"
      width="90vw"
      style="margin-right:2vh"
    >
      <div class="noContentExp">
        해당 콘텐츠가 없습니다.
      </div>
    </v-card>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: 'MovieList',
  props: ["CinemaList"],
  methods: {
    goDetail(movieId) {
      router.push(`/movie/${movieId}`);
    },
    getMovieName(name) {
      if (name.length > 8) {
        return `${name.slice(0, 8)}...`;
      } else {
        return name;
      }
    }
  }
}
</script>

<style src="./MovieList.css" scoped></style>
<template>
  <div>
    <div>
      {{ Label }}
    </div>
    <v-slide-group
      class="pa-4 cinemaList"
      active-class="success"
    >
      <v-slide-item
        v-for="(cinema, idx) in CinemaList"
        :key="idx"
      >
        <v-card
          class="ma-4"
          height="45vh"
          width="45vw"
          style="margin-right:2vh"
          @click="goDetail(cinema.id)"
          dark
        >
          <v-img 
            :src=cinema.poster
            height="40vh"
            width="45vw"
          >
          </v-img>
          <v-card-text>{{ cinema.name }}</v-card-text>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </div>
</template>

<script>
import router from '../../../router';
export default {
  name: 'TheaterMovie',
  props: ['CinemaList', 'Label'],
  methods: {
    goDetail(movieId) {
      router.push(`/movie/${movieId}`);
    }
  }
}
</script>

<style src="./CinemaList.css" scoped></style>
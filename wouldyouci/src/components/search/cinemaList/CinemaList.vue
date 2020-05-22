<template>
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
        height="20vh"
        width="50vw"
        style="margin-right:2vh"
        @click="goDetail"
      >
        <v-img 
          :src=cinema.src
          height="15vh"
          width="50vw"
        >
        </v-img>
        <v-card-text>{{ cinema.title }}</v-card-text>
      </v-card>
    </v-slide-item>
  </v-slide-group>
</template>

<script>
import router from '../../../router';
export default {
  name: 'TheaterMovie',
  props: ['CinemaList'],
  methods: {
    goDetail() {
      router.push('/movieDetail')
    }
  }
}
</script>

<style src="./CinemaList.css" scoped></style>
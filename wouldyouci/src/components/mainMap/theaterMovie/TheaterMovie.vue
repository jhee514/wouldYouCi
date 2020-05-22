<template>
  <v-slide-group
    class="pa-4"
    active-class="success"
  >
    <v-slide-item
      v-for="(title, idx) in theaterMovieList"
      :key="idx"
    >
      <v-card
        class="ma-4"
        height="25vh"
        width="50vw"
        style="margin-right:2vh"
        @click="goSite('https://www.lottecinema.co.kr/NLCHS/ticketing?movieCd=15834&movieName=%EB%8D%94%20%ED%94%8C%EB%9E%AB%ED%8F%BC')"
      >
        <v-img 
          src="https://image.edaily.co.kr/images/Photo/files/NP/S/2019/05/PS19051301305.jpg"
          height="15vh"
          width="50vw"
        >
        </v-img>
        <v-card-text>{{ title }}</v-card-text>
      </v-card>
    </v-slide-item>
  </v-slide-group>
</template>

<script>
export default {
  name: 'TheaterMovie',
  props: ['theaterMovieList'],
  methods: {
    goSite(url) {
      window.open(url, "예매창", "fullscreen=yes");
    }
  }
}
</script>

<style src="./TheaterMovie.css" scoped></style>
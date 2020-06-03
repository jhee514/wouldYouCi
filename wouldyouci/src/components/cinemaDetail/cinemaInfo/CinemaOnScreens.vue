<template>
  <v-card
    max-width="400"
    class="mx-auto"
  >
    <v-container>
      <v-row dense>
        <v-col
          v-for="(movie, index) in movies"
          :key="index"
          cols="12"
        >
          <v-card>
            <div class="d-flex flex-no-wrap justify-space-between">
              <v-card-title class="headline"> 
                {{ movie.movie.name }}
              </v-card-title>
              <v-card-subtitle>
                {{ formatDate(movie.date) }}  ||  {{ formatTime(movie.start_time)}} ~ {{ formatTime(movie.end_time) }}
              </v-card-subtitle>
              <v-card-subtitle>
                {{ movie.info }}  |  잔여 {{ movie.seats }} / {{movie.total_seats}}
              </v-card-subtitle>
              <v-btn>
                영화상세정보
              </v-btn>
              <v-btn>
                영화관 홈페이지
              </v-btn>


            

              <v-avatar
                class="ma-3"
                height="20vh"
                tile
                right
              >
                <v-img :src="movie.movie.poster"></v-img>
              </v-avatar>

            </div>
          </v-card>
        
        </v-col>
      </v-row>
      <v-row>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeMe">Close</v-btn>
      </v-row>
    </v-container>
  </v-card>
</template>










<script>
import { mapGetters, } from 'vuex';

  export default {
    name: 'CinemaOnScreens',
    props: ["movies"],
    data () {
      return {

      }
    },
    computed: {
      ...mapGetters({
      details: 'getCinemaDetail',
      }),


    },

    methods: {
      closeMe() {
      this.$emit("close");
      },
      formatDate(date) {
      var moment = require('moment');
      return moment(date).format('YYYY.MM.DD')
      },
      formatTime(time) {
      var moment = require('moment');
      return moment(time, 'kk:mm:ss').format('h:mm')
      },
      toggleOrder () {
        this.sortDesc = !this.sortDesc
      },
      nextSort () {
        let index = this.headers.findIndex(h => h.value === this.sortBy)
        index = (index + 1) % this.headers.length
        this.sortBy = this.headers[index].value
      },
    },
  }
</script>


<style src="./CinemaInfo.css" scoped></style>
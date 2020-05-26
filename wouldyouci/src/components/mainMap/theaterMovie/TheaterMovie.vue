<template>
  <div>
    <v-slide-group
      class="pa-4"
      active-class="success"
      v-if="theaterMovieList && theaterMovieList.length"
    >
      <v-slide-item
        v-for="(movie, idx) in theaterMovieList"
        :key="idx"
      >
        <v-card
          class="ma-4"
          height="30vh"
          width="85vw"
          style="margin-right:2vh"
          @click="goSite(movie.url)"
        >
          <v-row>
            <v-col>
              <v-img 
                :src="movie.movie.poster"
                height="30vh"
                width="40vw"
              >
              </v-img>
            </v-col>
            <v-col>
              <v-card-text>
                <h4>{{ movie.movie.name }}</h4><br />
                <div>
                  {{ movie.seats }} / {{ movie.total_seats }}<br/>
                  잔여 좌석 / 전체 좌석
                </div><br />
                <div>
                  {{ movie.start_time }} ~ {{ movie.end_time }}
                </div>
              </v-card-text>
            </v-col>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  <v-card
    class="ma-4 noItem"
    height="30vh"
    width="95vw"
    style="margin-right:2vh"
    v-else
  >
    <div class="noMovie">
      예매 가능한 영화가 없습니다.
    </div>
  </v-card>
</div>
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
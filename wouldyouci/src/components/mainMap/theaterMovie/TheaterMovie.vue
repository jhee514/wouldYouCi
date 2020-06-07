<template>
  <div>

    <v-chip
            class="ml-2 mb-2 mychip"
            color="mypink"
            label
            text-color="white"
    >
      <v-icon left>mdi-theater</v-icon>
      <span>{{ theaterName }}</span>
    </v-chip>
    <v-slide-group
      active-class="success"
      v-if="theaterMovieList && theaterMovieList.length"
    >
      <v-slide-item
        v-for="(movie, idx) in theaterMovieList"
        :key="idx"
      >
        <v-card
          class="ml-2 mr-2 mb-1 mycard"
          @click="goSite(movie.url)"
        >
          <v-row>
            <v-col class="col-5">
              <v-img
                :src="movie.movie.poster"
                class="card_image"
              >
              </v-img>
            </v-col>
            <v-col class="pl-1 ml-1">
              <v-list-item two-line>
                <v-list-item-content>
                  <v-list-item-title>{{ movie.movie.name }}</v-list-item-title>
                  <v-list-item-subtitle>{{ movie.movie.name_eng }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
<!--              <v-list-item two-line>-->
<!--                <v-list-item-content>-->
<!--                  <v-list-item-subtitle>{{ movie.info }}</v-list-item-subtitle>-->
<!--                  <v-list-item-subtitle>{{ movie.start_time }} ~ {{ movie.end_time }}</v-list-item-subtitle>-->
<!--                </v-list-item-content>-->
<!--              </v-list-item>-->
              <v-card-text class="mb-1">
                <div class="divfont mb-0">
                  {{ movie.info }}
                </div>
                <div class="divfont mb-0">
                  {{ movie.start_time }} ~ {{ movie.end_time }}
                </div>
                <div class="divseat">
                  {{ movie.seats }}/{{ movie.total_seats }} 석
                </div>

<!--                <v-list-item-subtitle>{{ movie.start_time }} ~ {{ movie.end_time }}</v-list-item-subtitle>-->

                <v-chip x-small v-if="movie.movie.watch_grade==='15세 관람가'"
                        label color="#FCB5C7"
                >15+</v-chip>
                  <v-chip x-small v-else-if="movie.movie.watch_grade==='12세 관람가'"
                         label color="#E9EA72"
                  >12+</v-chip>
                  <v-chip x-small v-else-if="movie.movie.watch_grade==='전체 관람가'"
                         label color="#C9EBF4"
                  >All</v-chip>
                  <v-chip x-small v-else-if="movie.movie.watch_grade==='청소년 관람불가'"
                         label color="#BF3952" text-color="white"
                  >18+</v-chip>
                  <v-chip x-small v-else
                          label color="lightpink"
                  >{{ movie.movie.watch_grade }}</v-chip>
                <v-chip label class="chipfortime" x-small color="#86D0EC">{{ movie.movie.running_time }}</v-chip>

              </v-card-text>
            </v-col>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>
  <v-card
    class="ml-2 mr-2 mb-3 moItem"
    v-else
  >
    <div class="noMovie">
      <p class="mytitle text--primary">예매 가능한 영화가 없습니다.</p>
    </div>
  </v-card>
</div>
</template>

<script>
export default {
  name: 'TheaterMovie',
  props: ['theaterMovieList', 'theaterName'],
  methods: {
    goSite(url) {
      window.open(url, "예매창", "fullscreen=yes");
    }
  }
}
</script>

<style src="./TheaterMovie.css" scoped></style>
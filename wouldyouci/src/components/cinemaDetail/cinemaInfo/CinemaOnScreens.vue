<template>
  <v-container class="grey lighten-5">
    <!-- 기존의 카드 레이아웃 -->
    <!-- <v-row 
      v-for="(movie, index) in movies"
      :key="index"
      >
      <v-col cols="9">
        <v-card-title> 
          {{ movie.movie.name }}
        </v-card-title>
        <v-card-subtitle>
          <p>{{ formatDate(movie.date) }}  ||  {{ formatTime(movie.start_time)}} ~ {{ formatTime(movie.end_time) }}</p>
          <p>{{ movie.info }}</p>
          <p>잔여 {{ movie.seats }}석 / {{movie.total_seats}}석</p>
        </v-card-subtitle>

        <router-link :to="{ name: 'MovieDetail', params: {id: movie.movie.id}}">
        <v-btn 
          small
          @click="toMovieDetail(movie.movie.id)"
          >
          영화상세정보
        </v-btn>
        </router-link>
        <v-btn
          target="_blank"
          :href="details.url"
          small
          >
          영화관 홈페이지
        </v-btn>
      </v-col>

      <v-col cols="3">
        <v-img width="auto" :src="movie.movie.poster" />
      </v-col>
    </v-row> -->

    <!-- 정렬 테이블 레이아웃 -->
    <!-- <v-data-table
      :headers="headers"
      :items="movies"
      :sort-by="['movie.id', 'info', 'start_time',]"
      :sort-desc="[false, true]"
      multi-sort
      class="elevation-1"
    ></v-data-table> -->
    
        <v-tabs
          v-model="tab"
          background-color="pink lighten-2"
          color="white"
          light
          right
        >
          <v-tab
            v-for="(item, idx) in items"
            v-show="item.content.length"
            :key="idx"
          >
            {{ item.tab }}
          </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item
            v-for="(item, idx) in items"
            :key="idx"
          >
            <v-timeline
              align-top
              dense
            >
              <v-timeline-item
                v-for="(movie, idx) in item.content"
                :key="idx"
                small
              >
              <template v-slot:icon>
                <router-link :to="{ name: 'MovieDetail', params: {id: movie.movie.id}}">
                <v-avatar>
                  <v-img
                    :src="movie.movie.poster"
                  ></v-img>
                </v-avatar>
                </router-link>
              </template>
                <v-row class="pt-1">
                  <v-col cols="3">
                    <strong>{{ formatTime(movie.start_time)}}</strong> ~{{ formatTime(movie.end_time) }}
                  </v-col>
                  <v-col>
                    <strong>{{ movie.movie.name }}</strong>
                    <div class="caption mb-2">{{ movie.info }} | {{ movie.seats }} / {{movie.total_seats}}석</div>

                  </v-col>
                </v-row>
              
              
              
              </v-timeline-item>
            </v-timeline>
          </v-tab-item>
        </v-tabs-items>
      <v-row>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeMe">Close</v-btn>
      </v-row>

  </v-container>
</template>


<script>
import { mapGetters, } from 'vuex';

  export default {
    name: 'CinemaOnScreens',
    props: ["onscreens"],
    data () {
      return {
        headers: [
          {
            text: '영화',
            align: 'start',
            sortable: false,
            value: 'movie.name',
          },
          { text: '날짜', value: 'date' },
          { text: '시작 시간', value: 'start_time' },
          { text: '종료 시간', value: 'end_time' },
          { text: '잔여 좌석수', value: 'seats' },
          { text: '전체 좌석수', value: 'total_seats' },
          { text: '상영관', value: 'info' },
          { text: 'movid id', value: 'movie.id' },
        ],
        tab: null,
        items: [
        ],

      }
    },

    created() {
      var dayjs = require('dayjs')
      var dates = this.onscreens.map(function(movie) {
        return dayjs(movie.date)
      });

      var minMax = require('dayjs/plugin/minMax')
      dayjs.extend(minMax)
      var recentDate = dayjs.min(dates);
      var latestDate = dayjs.max(dates);

      var j = 0;
      var newDate = dayjs(recentDate).clone().add(j, 'days');
      var isSameOrBefore = require('dayjs/plugin/isSameOrBefore')
      dayjs.extend(isSameOrBefore)
      while ( newDate.isSameOrBefore(latestDate)) {
        this.items.push({tab: dayjs(newDate).format('YYYY.MM.DD'), content: []});
        j++;
        newDate = recentDate.clone().add(j, 'd');
      }

      for ( var i in this.items ) {
        const item = this.items[i]
        const date = dayjs(item.tab).format('YYYY-MM-DD')
        item.content = this .onscreens.filter(movie => movie.date == date)
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
      return moment(time, 'kk:mm:ss').format('hh:mm')
      },

      toggleOrder () {
        this.sortDesc = !this.sortDesc
      },
      nextSort () {
        let index = this.headers.findIndex(h => h.value === this.sortBy)
        index = (index + 1) % this.headers.length
        this.sortBy = this.headers[index].value
      },

      getMoviesByDate(date) {
        var moviesOnTheDay = []
        for ( var movie in this.onscreens ) {
          if (movie.date == date) {
            moviesOnTheDay.push(movie)
          }
        }
        return moviesOnTheDay
      },
      

    },
  }
</script>


<style src="./CinemaInfo.css" scoped></style>
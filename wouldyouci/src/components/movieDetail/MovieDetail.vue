<template>
  <v-app>
    <Title />
    <div class="body">

      <iframe 
        id="player"
        type="text/html" 
        width="auto" 
        height="auto"
        allow="autoplay"
        allowfullscreen
        frameborder= 0;
        :src=details.trailer
        ></iframe>

      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ details.name_eng }}</v-list-item-subtitle>
          <v-list-item-subtitle>{{ details.watch_grade }}</v-list-item-subtitle>
          <v-list-item-subtitle>
            <Score :score="avgRating"/>
          </v-list-item-subtitle>
          {{ details.summary }}
        </v-list-item-content>
      </v-list-item>

      <v-card>
        <v-tabs
          fixed-tabs
          v-model="tab"
          background-color="orange lighten-3"
          dark
          centered
        >
          <v-tab
            v-for="item in items"
            :key="item.tab"
          >
            {{ item.tab }}
          </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab">
          <v-tab-item
            v-for="item in items"
            :key="item.tab"
          >
            <v-card flat>
              <v-card-text>
                <component v-bind:is="item.component" :details="details"></component>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </div>
    <Nav />
  </v-app>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import MovieInfo from './movieInfo/MovieInfo';
import Ratings from './ratings/Ratings';
import Score from './score/Score';
import { fetchMovie } from '@/api/index';

export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
    MovieInfo,
    Ratings,
    Score,
  },
   
  data() {
      return {
        tab: null,
        items: [
          {tab: 'Info', component: "MovieInfo"},
          {tab: 'Reviews', component: "Ratings"}
        ],
        avgRating: null,
        details: [],
      }
  },

  methods: {
    async fetchData() {
      try {
        const { data } = await fetchMovie(this.$route.params.id);
        this.details = data
      } catch (err) {
        console.log("errrrrrrrrrr");
        console.log(err);
        console.log(err.response);
      }
    },
    getAvgRating() {
      let sum = 0;
      for (let i = 0; i <= this.details.reviews.length; i++) {
        sum += this.details.reviews[i].score
        console.log(sum)
      } 
      this.avgRating = sum / this.details.reviews.length
    }
  },

  created() {
      this.fetchData();
      this.getAvgRating;
    },
  
  computed: {
  }
  

}
</script>

<style src="./MovieDetail.css" scoped></style>
<template>
  <v-app>
    <Title />
    <div class="body">
      <v-card elevation=0>
        <div class="trailer">
          <iframe 
            id="player"
            type="text/html" 
            width="auto" 
            height="auto"
            allow="autoplay"
            allowfullscreen
            frameborder=0;
            :src=details.trailer
            ></iframe>
        </div>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ details.name_eng }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ details.watch_grade }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        
        <v-card-actions>
          <!-- TODO 평점 구하는 함수 -->
          <Score :score="avgScore"/>
          <v-spacer></v-spacer>

          <!-- TODO 찜/예매 함수 -->
          <!-- TODO 상영중 표시 -->
          <v-btn icon @submit.prevent="toggleWish">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn v-if="details.is_showing" icon>
            <v-icon @submit.prevent="getTicket">mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>

        <v-card-text>
        {{ details.summary }}
        </v-card-text>

        <v-tabs
          v-model="tab"
          background-color="white"
          color="orange dark-3"
          centered
          fixed-tabs
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
import Score from './ratings/Score';
import { mapGetters, mapActions } from 'vuex';


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
      avgScore: 0,
    }
  },

  computed: {
    ...mapGetters({
      details: 'getMovieDetail'
      }
    ),
  },

  methods: {
    ...mapActions(['fetchMovieDetail']),
    

  },
  async created() {
    try {
      await this.fetchMovieDetail(this.$route.params.id)
      .then(()=> {
          // 평점 구하기
          let sum = 0;
          for (let i=0; i < this.details.ratings.length; i++) {
            sum += (this.details.ratings[i].score)
          }
          this.avgScore = sum / this.details.ratings.length;
         }
        )
      } catch (err) {
        console.log(err);
    }
  },


}
</script>

<style src="./MovieDetail.css" scoped></style>
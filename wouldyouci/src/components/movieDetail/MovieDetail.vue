<template>
  <v-app>
    <Title />
    <div class="body">
      <v-card elevation=0>
        <div 
          v-if="details.trailer"
          class="trailer"
          >
            <iframe 
              id="player"
              type="text/html" 
              width="auto" 
              height="auto"
              allow="autoplay"
              allowfullscreen
              frameborder=0
              :src=details.trailer
              ></iframe>
        </div>
        <div v-else>
           <v-img 
            center
            width="auto"
            :src="details.poster" />
        </div>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ details.name_eng }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ details.watch_grade }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        
        <v-card-actions>
          <Score :score="details.score"/>
          <v-spacer></v-spacer>

          <v-btn 
            icon 
            :color="(isPicked) ? 'pink' : 'grey'"
            @click.prevent="togglePickMovie">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn v-if="details.is_showing" icon>
            <v-icon @submit.prevent="getTicket">mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>

        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>줄거리</v-expansion-panel-header>
            <v-expansion-panel-content>{{ details.summary }}</v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>


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
                <component 
                  v-bind:is="item.component" 
                  :details="details" 
                  :user="user" 
                  ></component>
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
import Score from '../ratingForm/Score';
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
      expand: false,
      isPicked: false,

    }
  },

  computed: {
    ...mapGetters({
      details: 'getMovieDetail',
      user: 'getUserInfo',
      }),
  },

  methods: {
    ...mapActions(['fetchMovieDetail', 'bringUserInfo', 'togglePick', ]),
    async togglePickMovie() {
      const item = 'movie'
      const itemId = this.details.id
      await this.togglePick({item, itemId})
      if ( this.isPicked ){
        this.isPicked = false
      } else {
        this.isPicked = true
      }
    },
  },
  async created() {
    await this.fetchMovieDetail(this.$route.params.id);
    await this.bringUserInfo()
    if (this.user.pick_movies && this.user.pick_movies.includes(this.details.id)) {
      this.isPicked = true
    } else {
      this.isPicked = false
    }
  },

}
</script>


<style src="./MovieDetail.css" scoped></style>
<template>
  <div>
    <Title />
    <div class="body">
      <v-card elevation=0>

        <MovieTrailer class="trailer" :details="details" />

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ details.name_eng }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ details.watch_grade }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>

        <v-card-actions class="links">

          <div>
            {{ details.predicted_score }} %
          </div>

          <v-spacer></v-spacer>
          <v-btn
            class="button"
            icon 
            :color="(isPicked) ? 'pink' : 'grey'"
            @click.prevent="togglePickMovie">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
    
    




          <!-- 상영중인 영화관 모달 -->
          <v-dialog v-if="details.is_showing" v-model="dialog">
            <template v-slot:activator="{ on }">
              <v-btn
                v-on="on"
                class="button"
                color="pink"
                icon 
                >
                <v-icon>mdi-video-vintage</v-icon>
              </v-btn>
            </template>
            <ShowingCinemas @close="closeModal" />
          </v-dialog>


    














        </v-card-actions>
      
        <div class="summary">
          <div v-bind:style="lineClamp">
            {{ details.summary }}
          </div>
          <v-btn class="button" icon absolute right @click.prevent="toggleSummaryClamp()">
            <v-icon v-if="isHidden">mdi-arrow-down</v-icon>
            <v-icon v-else>mdi-arrow-up</v-icon>
          </v-btn>
        </div>

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
                  ></component>
              </v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items>

      </v-card>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import MovieTrailer from './movieTrailer/MovieTrailer';
import ShowingCinemas from './movieInfo/ShowingCinemas';
import MovieInfo from './movieInfo/MovieInfo';
import MovieRatings from './movieRatings/MovieRatings';
import Score from '../ratingForm/Score';
import { mapGetters, mapActions } from 'vuex';


export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
    MovieTrailer,
    ShowingCinemas,
    MovieInfo,
    MovieRatings,
    Score,
  },

  async created() {
    await this.fetchMovieDetail(this.$route.params.id);
    this.isPicked = this.details.pick_movies
  },

  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "MovieInfo"},
        {tab: 'Reviews', component: "MovieRatings"}
      ],
      expand: false,
      isPicked: false,
      dialog: false,
      isHidden: true,
      lineClamp: {
        overflow: 'hidden',
        display: '-webkit-box',
        height: 'auto',
        '-webkit-box-orient': 'vertical',
        '-webkit-line-clamp': 3,
      }
    }
  },

  computed: {
    ...mapGetters({
      details: 'getMovieDetail',
      }),

  },

  methods: {
    ...mapActions(['fetchMovieDetail', 'togglePick', ]),
    closeModal() {
      this.dialog = false;
    },

    toggleSummaryClamp() {
      console.log(this.summary)
      if ( this.isHidden == false) {
        this.isHidden = true;
        this.lineClamp = {
          overflow: 'hidden',
          display: '-webkit-box',
          height: 'auto',
          '-webkit-box-orient': 'vertical',
          '-webkit-line-clamp': 3,
        }
      } else {
        this.isHidden = false;
        this.lineClamp = {
          display: 'block',
          height: 'auto',
          '-webkit-box-orient': 'vertical',
          '-webkit-line-clamp': 'none',
        }
      }
    },

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


}
</script>


<style src="./MovieDetail.css" scoped></style>
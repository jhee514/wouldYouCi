<template>
  <v-app>
    <Title />
    <div class="body">
      <v-card elevation=0>
        <div>
          <img 
            width="370vw" 
            height="auto"
            :src="details.img" />
        </div>

        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ details.address }}</v-list-item-subtitle>
            <v-list-item-subtitle>{{ details.tel }}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        
        <v-card-actions>
          <Score :score="details.score"/>
          <v-spacer></v-spacer>

          <v-btn 
            icon 
            :color="(isPicked) ? 'pink' : 'grey'"
            @click.prevent="togglePick()">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          <v-btn icon>
            <v-icon :href="details.url">mdi-share-variant</v-icon>
          </v-btn>
        </v-card-actions>

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
import CinemaInfo from './cinemaInfo/CinemaInfo';
import Ratings from './ratings/Ratings';
import Score from '../movieDetail/ratings/Score';
import { mapGetters, mapActions } from 'vuex';


export default {
  name: 'MovieDetail',
  components: {
    Nav,
    Title,
    CinemaInfo,
    Ratings,
    Score,
  },

  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "CinemaInfo"},
        {tab: 'Reviews', component: "Ratings"}
      ],
      expand: false,
      isPicked: false,

    }
  },

  computed: {
    ...mapGetters({
      details: 'getCinemaDetail',
      user: 'getUserInfo',
      }),
  },

  methods: {
    ...mapActions(['fetchCinemaDetail', 'bringUserInfo', 'togglePickMovie', ]),
    async togglePick() {
      await this.togglePickMovie(this.details.id)
      if ( this.isPicked ){
        this.isPicked = false
      } else {
        this.isPicked = true
      }
    },
  },

  async created() {
    await this.fetchCinemaDetail(this.$route.params.id);
    await this.bringUserInfo()
    if (this.user.pick_cinemas && this.user.pick_cinemas.includes(this.details.id)) {
      this.isPicked = true
    } else {
      this.isPicked = false
    }
  },

}
</script>


<style src="./CinemaDetail.css" scoped></style>
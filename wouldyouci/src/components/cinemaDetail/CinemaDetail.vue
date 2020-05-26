<template>
  <v-app>
    <Title />
    <div class="cinemaInfo">
      <v-list-item two-line>
        <v-list-item-content>
          <v-img :src=details.image />
          <v-list-item-title class="headline">{{ details.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ details.address }}</v-list-item-subtitle>
          <v-list-item-subtitle>
            <Rating :rating="avgRating"/>
          </v-list-item-subtitle>

          <v-card>
            <v-tabs
              fixed-tabs
              v-model="tab"
              background-color="orange lighten-3"
              dark>
              <v-tab
                v-for="item in items"
                :key="item.tab">
                {{ item.tab }}
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
              <v-tab-item
                v-for="item in items"
                :key="item.tab">
                <v-card flat>
                  <v-card-text>
                    <component v-bind:is="item.component" :details="details"></component>
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </div>

    <Nav />
  </v-app>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import CinemaInfo from './cinemaInfo/CinemaInfo';
import CinemaRatings from './cinemaRatings/CinemaRatings';
import Rating from '../movieDetail/rating/Rating';
import { fetchCinema } from '@/api/index';

export default {
  name: 'CinemaDetail',
  components: {
    Nav,
    Title,
    CinemaInfo,
    CinemaRatings,
    Rating,
  },
  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "CinemaInfo"},
        {tab: 'Reviews', component: "CinemaRatings"}
      ],
      details: []
    }
  },

  methods: {
    async fetchData() {
      const { data } = await fetchCinema(this.$route.params.id);
      this.details = data 
    }
  },

  created() {
      this.fetchData();
    },
}
</script>

<style src="./CinemaDetail.css" scoped></style>
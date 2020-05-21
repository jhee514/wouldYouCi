<template>
  <div class="cinemaInfo">
    <v-list-item two-line>
      <v-list-item-content>
        <v-img></v-img>
        
        <v-list-item-title class="headline">{{ infos.fields.name }}</v-list-item-title>
        
        <v-list-item-subtitle>{{ infos.fields.name_eng }}</v-list-item-subtitle>
        
        <v-list-item-subtitle>{{ infos.fields.watch_grade }}</v-list-item-subtitle>
        
        <v-list-item-subtitle>
          <v-rating
            :value=rating
            background-color="orange lighten-3"
            color="amber"
            dense
            half-increments
            readonly
            size="14" />
        </v-list-item-subtitle>

        {{ infos.fields.summary }}

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
                  <component v-bind:is="item.component" :infos="movie"></component>
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-list-item-content>
    </v-list-item>
  </div>
</template>
<script>
import MovieInfo from '../../movieDetail/movieInfo/MovieInfo';
import MovieReview from '../../movieDetail/movieReview/MovieReview';
export default {
  name: 'CinemaDetail',
  props: ["infos"],
  components: {
    MovieInfo,
    MovieReview,
  },
  data() {
    return {
      tab: null,
      items: [
        {tab: 'Info', component: "MovieInfo"},
        {tab: 'Reviews', component: "MovieReview"}
      ],
      rating: 1.5,
    }
  },
}
</script>

<style src="./CinemaInfo.css" scoped></style>
<template>
  <div class="cinemaRatings">
    <v-list three-line>
      <template v-for="(rating, index) in details.ratings">
        <v-subheader
          v-if="rating.score"
          :key="rating.score"
          v-text="rating.score"
        ></v-subheader>

        <v-list-item :key="rating.comment">
          <v-list-item-avatar class="avatar">
            <span class="white--text headline">{{ rating.user.username[0] }}</span>          
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>
              <Score :score="rating.score" />
              <span align-end>{{ rating.user.username }}</span>
            </v-list-item-title>
              {{ rating.comment}}
          </v-list-item-content>
        </v-list-item>

        <v-divider :key="index"></v-divider>
      </template>
    </v-list>
  </div>
</template>

<script>
import Score from '../../movieDetail/score/Score';

export default {
  name: 'CinemaRatings',
  props:["details"],
  components: {
    Score,
  },

  data() {
    return {
    }
  }
}
</script>

<style src="./CinemaRatings.css" scoped></style>
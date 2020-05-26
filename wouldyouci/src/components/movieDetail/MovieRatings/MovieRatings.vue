<template>
  <div class="movieRatings">
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
              <Rating :rating="rating.score" />
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
import Rating from '../rating/Rating'

export default {
  name: 'MovieRatings',
  props:["details"],
  components: {
    Rating,
  },

  data() {
    return {
    }
  }
}
</script>

<style src="./MovieRatings.css" scoped></style>
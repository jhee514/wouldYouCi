<template>
  <div class="ratings">
    <RatingForm />

    <v-list v-if="isRatings">
      <template v-for="(rating, index) in details.ratings">
        <v-list-item :key="rating.comment">
          <v-list-item-avatar class="avatar">
            <span class="white--text headline">{{ rating.user.username[0] }}</span>          
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title>
              <Score :score="rating.score" />
            </v-list-item-title>
              {{ rating.comment}}
            <v-list-item-subtitle>
              <span align-end>{{ rating.user.username }} | {{ formatDate(rating.updated_at) }}</span>
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-divider :key="index"></v-divider>
      </template>
    </v-list>

    <p v-else>
      리뷰를 남겨주세요 :)
    </p>
  </div>
</template>

<script>
import Score from '../score/Score';
import RatingForm from '../ratings/RatingForm';

export default {
  name: 'Ratings',
  props:["details"],
  components: {
    Score,
    RatingForm,
  },

  data() {
    return {
      isRatings: this.details.ratings.length
    }
  },
  methods: {
    formatDate(date) {
      var moment = require('moment');
      return moment(date).format('YYYY.MM.DD')
    }
  }
}
</script>

<style src="./Ratings.css" scoped></style>
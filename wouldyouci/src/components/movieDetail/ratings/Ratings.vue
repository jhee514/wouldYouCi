<template>
  <div 
    class="ratings"
    >
    <RatingForm :id="details.id" @submitRating="addRating"/>

    <v-list v-if="isRatings">
      <template v-for="(rating, index) in ratings">
        <v-list-item :key="index">
          <v-list-item-avatar class="avatar">
            <span class="white--text headline">{{ rating.user.username[0] }}</span>          
          </v-list-item-avatar>
          <v-list-item-content>
              <div class="infos">
                <div class="user">
                 {{ rating.user.username }} | {{ formatDate(rating.updated_at) }}
                </div>
                <div class="score">
                  <Score :score="rating.score" />
                </div>
              </div>
              <div class="content">
                <p class="comment">{{ rating.comment}}</p>
                
                <div v-if="rating.user.username == user.username" class="button">
                  <v-btn icon @click.prevent="deleteRating(index, rating, details.id)">
                    <i class="fas fa-times fa-xs"></i>
                  </v-btn>
                </div>

              </div>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>

    <p v-else>
      리뷰를 남겨주세요 :)
    </p>
  </div>
</template>

<script>
import Score from './Score';
import RatingForm from './RatingForm';
import { mapActions } from 'vuex';

export default {
  name: 'Ratings',
  props:["details", "user"],
  components: {
    Score,
    RatingForm,

  },

  data() {
    return {
      loading: true,
      isRatings: this.details.ratings.length,
      buttons: [
        {method:"delete", icon:"fas fa-times fa-xs"},
        {method:"edit", icon:"far fa-edit fa-xs"},
      ],
    }
  },
  computed: {
    ratings() {
      return this.details.ratings
    },
  },

  methods: {
    ...mapActions(['postRating', 'delRating', ]),

    formatDate(date) {
      var moment = require('moment');
      return moment(date).format('YYYY.MM.DD')
    },
    async deleteRating(index, rating, movieId) {
      const ratingId = rating.id;
      const params = {ratingId, movieId};
      await this.delRating(params);
    },
    async addRating(rating){
      await this.postRating(rating);

    },
  }
}
</script>

<style src="./Ratings.css" scoped></style>
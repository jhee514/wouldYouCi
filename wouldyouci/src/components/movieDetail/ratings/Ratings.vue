<template>
  <div class="ratings">
    <RatingForm :id="details.id" />

    <v-list v-if="isRatings">
      <template v-for="(rating, index) in details.ratings">
        <v-list-item :key="rating.comment">
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
                
                <div v-if="rating.user.username == userName" class="button">
                  <v-btn icon @click.prevent="deleteRating(rating.id)">
                    <i class="fas fa-times fa-xs"></i>
                  </v-btn>
                </div>

              </div>
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
import Score from './Score';
import RatingForm from './RatingForm';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Ratings',
  props:["details"],
  components: {
    Score,
    RatingForm,
  },

  data() {
    return {
      isRatings: this.details.ratings.length,
      buttons: [
        {method:"delete", icon:"fas fa-times fa-xs"},
        {method:"edit", icon:"far fa-edit fa-xs"},
      ]
    }
  },
  computed: {
    ...mapGetters({
      userName: 'getUserName',
      }
    ),
  },
  methods: {
    ...mapActions(['delRating']),

    formatDate(date) {
      var moment = require('moment');
      return moment(date).format('YYYY.MM.DD')
    },
    async deleteRating(ratingId) {
      await this.delRating(ratingId);
      console.log("deletedd")
    }
  }
}
</script>

<style src="./Ratings.css" scoped></style>
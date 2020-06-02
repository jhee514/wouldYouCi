<template>
  <div 
    class="ratings"
    v-infinite-scroll="loadMore"
    infinite-scroll-disabled="busy"
    infinite-scroll-distance="200"
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
                  <v-dialog v-model="dialog" persistent>
                    <template v-slot:activator="{ on }">
                      <v-btn
                        v-on="on"
                        icon 
                        color="grey"
                        x-small
                        >
                        <v-icon>mdi-pencil</v-icon>
                      </v-btn>
                    </template>
                    <RatingEditForm :id="details.id" :rating="rating" @close="closeModal" @editRating="editRating"/>
                  </v-dialog>

                  <v-btn 
                    icon 
                    @click.prevent="deleteRating(index, rating, details.id)">
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
import RatingEditForm from './RatingEditForm';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Ratings',
  props:["details", "user", "firstRatings", ],
  components: {
    Score,
    RatingForm,
    RatingEditForm,
  },

  data() {
    return {
      data: [],
      busy: false,
      page: 1,
      dialog: false,
      isRatings: this.details.ratings.length,
      ratings: this.firstRatings,
    }
  },
  computed: {
    ...mapGetters(['getRatings']),

  },
  methods: {
    ...mapActions(['fetchRatings', 'postRating', 'delRating', 'patchRating' ]),

    async loadMore() {
      this.busy = true;
      const params = { 
        movie: this.details.id, 
        page: this.page++
      };
      await this.fetchRatings(params)
      this.busy = false;
      console.log(this.ratings)
      for ( const rating of this.getRatings) {
        this.ratings.push(rating);
      }
    },

    formatDate(date) {
      var moment = require('moment');
      return moment(date).format('YYYY.MM.DD')
    },
    
    closeModal() {
      this.dialog = false;
    },

    deleteRating(index, rating, detailId) {
      const ratingId = rating.id;
      const params = {ratingId, detailId};
      if(confirm('삭제하시겠습니까?')){
        this.delRating(params);
      }
    },
    
    async addRating(rating){
      await this.postRating(rating);
    },
    
    async editRating(editedRating) {
      this.dialog = false;
      await this.patchRating(editedRating);
    },

  },
}
</script>

<style src="./Ratings.css" scoped></style>
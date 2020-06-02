<template>
  <div 
    class="ratings"
    >
    <RatingForm :id="details.id" @submitRating="addRating"/>

    <v-list 
      v-if="isRatings"
      v-infinite-scroll="loadMore"
      infinite-scroll-disabled="busy"
      infinite-scroll-distance="250"
      >
      <template v-for="(rating, index) in ratings" track-by="$index">
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
                <v-dialog v-model="dialog">
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
                    <RatingEditForm :rating="rating" @close="closeModal" @editRating="editRating"/>
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
      <v-btn
        color="amber"
        small
        dark
        bottom
        fixed
        right
        fab
        @click="goTop"
      ><v-icon>mdi-arrow-up</v-icon></v-btn>
    </v-list>

    <p v-else>
      리뷰를 남겨주세요 :)
    </p>
  </div>
</template>

<script>
import Score from '../../ratingForm/Score';
import RatingForm from '../../ratingForm/RatingForm';
import RatingEditForm from '../../ratingForm/RatingEditForm';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'CinemaRatings',
  props:["details", "user", ],
  components: {
    Score,
    RatingForm,
    RatingEditForm,
  },

  data() {
    return {
      busy: false,
      page: 1,
      dialog: false,
      isRatings: this.details.cinema_ratings.length,
      ratings: [],
    }
  },
  computed: {
    ...mapGetters(['getCinemaRatings']),

  },
  methods: {
    
    //delCinemaRating patchCinemaRating
    ...mapActions(['fetchRatings', 'postRating', 'delRating', 'patchRating' ]),

    async loadMore() {
      this.busy = true;
      const item = 'cinema'
      const params = { 
        cinema: this.details.id, 
        page: this.page++,
        };
      const res = await this.fetchRatings({item, params})
      this.busy = false;
      for ( const rating of res) {
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

    deleteRating(index, rating) {
      const item = 'cinema'
      const ratingId = rating.id;
      if(confirm('삭제하시겠습니까?')){
        this.delRating({item, ratingId});
        this.$delete(this.ratings, index)
      }
    },
    
    async addRating(rating){
      const item = 'cinema'
      rating[item] = this.details.id;
      const res = await this.postRating({item, rating});
      res.data["user"] = this.user;
      if ( this.isRatings ) {
        this.ratings.unshift(res.data)
      } else {
        this.ratings.push(res.data)
      }
    },
    
    async editRating(editedRating) {
      this.dialog = false;
      const item = 'cinema';
      editedRating[item] = this.details.id;
      const res = await this.patchRating({item, editedRating});

      res.data["user"] = this.user;
      const formerIndex = this.ratings.indexOf(this.ratings.find(el => {
        el.id === editedRating.id 
        }))
      this.ratings.splice(formerIndex, 1, res.data)
    },

    goTop() {
      window.scrollTo(0, 0);
    },

  },
}
</script>

<style src="./CinemaRatings.css" scoped></style>
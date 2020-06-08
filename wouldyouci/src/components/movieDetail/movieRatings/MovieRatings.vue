<template>
  <div 
    class="ratings"      
    v-infinite-scroll="loadMore"
    infinite-scroll-disabled="busy"
    infinite-scroll-distance="0"
    >
    
    <RatingForm class="rating-form" v-if="!scored" @submitRating="addRating"/>
    <div v-else>
      <div class="notification">
        리뷰를 작성한 영화입니다.
      </div>
    </div>

    <div class="movie-score">
      <div>{{ Number(this.details.score.toFixed(2)) }} </div>
      <v-rating
        class="score"
        :value="details.score"
        background-color="amber lighten-3"
        half-increments
        readonly
        size=20
        ></v-rating>
    </div>

    <v-list 
      v-if="isRatings"
      >
      <v-list-item
        v-for="(rating, index) in ratings"
        :key="index"
        class="rating"
        >
        <v-list-item-avatar
          color="primary" 
          x-small
          >
          <img 
            v-if="rating.user.file.length"
            :src="getUserProfile(rating.user)"
            />
          <span 
            v-else 
            class="white--text headline">
            {{ rating.user.username[0] }}
          </span>
        </v-list-item-avatar>

        <v-list-item-content>
          <div class="infos">
            <div class="user">
              {{ rating.user.username }} | {{ formatDate(rating.updated_at) }}
            </div>
            <div class="score">
              <v-rating
                class="score"
                :value="rating.score"
                background-color="amber lighten-3"
                color="amber"
                dense
                half-increments
                readonly
                size=14
                ></v-rating>
            </div>
          </div>
          <div class="content">
            <div class="comment">{{ rating.comment}}</div>
            <div v-if="rating.user.username == currentUser.username" class="button">
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
                <RatingEditForm :rating="rating" :index="index" @close="closeModal" @editRating="editRating"/>
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
      <v-btn
        class="upbutton"
        color="primary"
        small
        bottom
        fixed
        right
        fab
        @click="goTop"
        ><v-icon dark>mdi-arrow-up</v-icon></v-btn>
    </v-list>

    <div v-else>
      <div class="notification">
        첫번째 리뷰를 남겨주세요 :)
      </div>
    </div>
  </div>
</template>

<script>
import RatingForm from '../../ratingForm/RatingForm';
import RatingEditForm from '../../ratingForm/RatingEditForm';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'MovieRatings',
  props:["details", ],
  components: {
    RatingForm,
    RatingEditForm,
  },

  data() {
    return {
      busy: false,
      page: 1,
      dialog: false,
      isRatings: false,
      ratings: [],
      currentUser: '',
      scored: false,
      total: 0,

    }
  },
  
  created() {
    var jwt = require('jsonwebtoken');
    const token = sessionStorage.getItem('jwt');
    var decoded = jwt.decode(token, {complete: true});
    this.currentUser = decoded.payload
    if (this.details.has_score) {
      this.scored = true
    }
  },

  computed: {
    ...mapGetters(['getMovieRatings']),
 
  },

  methods: {
    ...mapActions(['fetchRatings', 'postRating', 'delRating', 'patchRating' ]),

    // async loadMore() {
    //   this.busy = true;
    //   const item = 'movie'
    //   const params = { 
    //     movie: this.details.id, 
    //     page: this.page++,
    //     };

    //   const resData = await this.fetchRatings({item, params})
    //   this.busy = false;
    //   if ( resData.count > 0 ) {
    //     this.isRatings = true;
    //     for ( const rating of resData.results) {
    //       this.ratings.push(rating);
    //     }
    //   }
    // },

    async loadMore() {
      this.busy = true;
      const item = 'movie'
      const params = { 
        movie: this.details.id, 
        page: this.page++,
        };

      const resData = await this.fetchRatings({item, params})
      if ( resData.results.length > 0 ) {
        this.isRatings = true;
        for ( const rating of resData.results) {
          this.ratings.push(rating);
        }
      }
      setTimeout(function () {
        this.busy = false;
        }, 1000)
      },

    // loadMore() {
    //   this.busy = true;
    //   console.log('loading... ' + new Date());
    //   setTimeout(function () {
    //     for (var i = 0, j = 10; i < j; i++) {
    //         console.log(this.total + i)
    //       }
    //       console.log('NOT BUSY')
    //       this.busy = false
    //     }, 10000)
    //   },

    formatDate(date) {
      var dayjs = require('dayjs')
      return dayjs(date).format('YYYY.MM.DD')
    },
    
    closeModal() {
      this.dialog = false;
    },

    getUserProfile(user) {
      const HOST = process.env.VUE_APP_SERVER_HOST;
      const profileURL = `${HOST}/${user.file[0]}`;
      return profileURL
    },

    deleteRating(index, rating) {
      const item = 'movie'
      const ratingId = rating.id;
      if(confirm('삭제하시겠습니까?')){
        this.delRating({item, ratingId});
        this.$delete(this.ratings, index)
        if ( index === 0 ) {
          this.isRatings = false
        }
      }
      this.scored = false
    },
    
    async addRating(rating){
      const item = 'movie'
      rating[item] = this.details.id;
      const res = await this.postRating({item, rating});
      res.data["user"] = this.currentUser;
      if ( this.isRatings ) {
        this.ratings.unshift(res.data)
      } else {
        this.isRatings = true
        this.ratings.push(res.data)
      }
      this.scored = true

    },
    
    async editRating(editedRating) {
      this.dialog = false;
      const item = 'movie';
      editedRating[item] = this.details.id;
      await this.patchRating({item, editedRating});
      this.ratings = [];
      this.page = 1;
      this.loadMore();

    },

    goTop() {
      window.scrollTo(0, 0);
    },

  },
}
</script>

<style src="./MovieRatings.css" scoped></style>
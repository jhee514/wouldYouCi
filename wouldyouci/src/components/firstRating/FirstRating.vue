<template>
  <div>
    <Title />
    <div 
      class="firstRating"
      v-infinite-scroll="loadMore" 
      infinite-scroll-disabled="Flag"
      infinite-scroll-distance="50vh"
    >
      <v-card class="explanation">
        <v-card-text>
          아래의 영화 중 본 영화에 대해 1~5점 사이의 평점을 남겨주시면
          당신의 취향에 맞는 영화를 추천해드립니다.
          <h4>단, 최소 10개 이상의 영화를 평가해주셔서 추천이 가능합니다.</h4>
        </v-card-text>
      </v-card>
      <v-container fluid>
        <v-row justify="end">
          <v-spacer></v-spacer>
          <v-btn @click="submitRating" text>제출</v-btn>
          <v-btn class="next" text @click="goMap">
            다음에 하기<v-icon small>fas fa-arrow-right</v-icon>
          </v-btn>
        </v-row>
        <v-row dense justify="center">
          <v-col
            v-for="card in cards"
            :key="card.name"
            cols="6"
            sm="4"
          >
            <v-card 
              class="movieCard"
            >
              <v-img
                :src="card.poster"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                height="40vh"
              >
              </v-img>

              <v-rating
                @input="addRating(card.id)"
                v-model="card.rating"
                color="#F7FE2E"
                background-color="#F2F2F2"
                half-increments
                small
              ></v-rating>
            </v-card>
          </v-col>
        </v-row>
        <!-- <v-row justify="end">
          <v-spacer></v-spacer>
          <v-btn text>제출</v-btn>
          <v-btn class="next" text @click="goMap">다음에 하기</v-btn>
        </v-row> -->
        <v-avatar class="cntA" size="6vh" color="#AD8BE8">
          <span>{{ cnt }}</span>
        </v-avatar>
        <v-btn
          text
          large
          rounded
          fab
          retain-focus-on-click 
          class="upBtn"
          @click="goTop"
        >
          <v-icon large>fas fa-arrow-circle-up</v-icon>
        </v-btn>
      </v-container>
    </div>
    <Nav />
  </div>
</template>

<script>
import Nav from '../nav/Nav.vue';
import Title from '../nav/Title.vue';
import router from '../../router';
import { mapActions } from 'vuex';

export default {
  name: 'UserPage',
  components: {
    Nav,
    Title
  },
  data() {
    return {
      cards: [],
      next: 1,
      Flag: false,
      check: {},
      ratedId: {},
      cnt: 0
    }
  },
  methods: {
    ...mapActions(['bringRatingMovies', 'submitRatings']),
    goMap() {
      router.push('/');
    },
    async loadMore() {
      console.log('rebring')
      this.Flag = true;
      const res = await this.bringRatingMovies(this.next);
      this.Flag = false;
      this.next += 1;
      console.log(res);
      this.cards = this.cards.concat(res.results);
    },
    submitRating() {
      console.log('submit');
      this.submitRatings(this.cards);
    },
    goTop() {
      window.scrollTo(0, 0);
    },
    addRating(cardId) {
      if (!this.ratedId[cardId]) {
        this.cnt += 1;
        this.ratedId[cardId] = 1;
      }
    }
  }
}
</script>

<style src="./FirstRating.css" scoped></style>
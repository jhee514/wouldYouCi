<template>
  <form class="ratingForm" @submit.prevent="submitRating">
    <div class="score">
      <v-rating
        :value=score
        background-color="orange lighten-3"
        color="amber"
        dense
        half-increments
        size="20"></v-rating>
      <v-slider
        v-model="score"
        dense
        min="0"
        max="5"
        step="0.5"
        :thumb-size="24"
        thumb-label="always"
        color="orange darken-3"
        track-color="orange lighten-3"
        ></v-slider>
    </div>
    <div class="comment">
      <v-textarea
        v-model="comment"
        clearable
        clear-icon="fas fa-times small"
        label="관람평"
        rows="1"
        auto-grow
        hide-details="auto"
        color="orange darken-3"
        dense
      ></v-textarea>
    </div>
    <v-btn 
      color="orange darken-3" 
      text 
      type="submit"
      right-alignment
      >Submit</v-btn>

  </form>
</template>

<script>

import { postRating } from '@/api/index';

export default {
  name: "RatingForm",
  components: {
    },
  data() {
    return {
      rules: [
        value => !!value || '점수를 입력해주세요.',
        value => ( value <= 5 ) || '최대 점수는 5점입니다.',
      ],
      score: null,
      comment: '',

    }
  },
  methods: {
    async submitRating() {
      const rating = {
        score: this.score,
        comment: this.comment,
      };
      const { data } = await postRating(rating);
      console.log("form 제출 !!!!", data);
      
    }
  },


}
</script>
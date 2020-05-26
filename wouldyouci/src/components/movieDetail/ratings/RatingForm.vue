<template>
  <form class="ratingForm" @submit.prevent="postRating(rating)">
    <div class="score">
      <v-rating
        :value=rating.score
        background-color="orange lighten-3"
        color="amber"
        dense
        half-increments
        size="20"></v-rating>
    </div>
    <div class="comment">
      <v-textarea
        v-model="rating.comment"
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

import { mapActions } from 'vuex';

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
      rating: {
        score: null,
        comment: '',
      },
    }
  },
  methods: {
    ...mapActions(['postRating']),
      
  },
}
</script>
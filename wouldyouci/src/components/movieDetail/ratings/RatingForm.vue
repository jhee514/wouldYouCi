<template>
  <form class="ratingForm" @submit="submitForm()">
    <div class="score">
      <v-rating
        v-model="rating.score"
        background-color="orange lighten-3"
        color="amber"
        half-increments
        size="18"></v-rating>
    </div>
    <div class="comment">
      <v-textarea
        v-model="rating.comment"
        clearable
        clear-icon="fas fa-times xsmall"
        label="관람평"
        rows="1"
        auto-grow
        hide-details="auto"
        color="orange darken-3"
        dense
      ></v-textarea>
      <v-btn 
        class="button"
        color="orange darken-3" 
        icon
        text 
        type="submit"
      >등록</v-btn>
    </div>

  </form>
</template>

<script>

import { mapActions } from 'vuex';

export default {
  name: "RatingForm",
  props:["id"],
  components: {
    },
  data() {
    return {
      rules: [
        value => !!value || '점수를 입력해주세요.',
        value => ( value <= 5 ) || '최대 점수는 5점입니다.',
      ],
      rating: {
        score: 0,
        comment: '',
        movie: this.id,
      },
    }
  },
  methods: {
    ...mapActions(['postRating']),
    async submitForm() {
      try {
        await this.postRating(this.rating);
        this.rating = {
          score: 0,
          comment: '',
          movie: this.id,
        }
      } catch (err) {
        console.log(err);
      }
    },    
  },
}
</script>
<style src="./RatingForm.css" scoped></style>
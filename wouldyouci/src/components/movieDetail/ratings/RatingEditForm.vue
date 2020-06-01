<template>
  <div class="ratingForm">
    <v-card>
      <v-card-title>
        <div class="score">
          <v-rating
            v-model="editedRating.score"
            color="amber"
            background-color="orange lighten-3"
            half-increments
            hover
            size="18">
            </v-rating>
        </div>
      </v-card-title>

      <v-card-text>
        <div class="comment">
          <v-textarea
            v-model="editedRating.comment"
            clearable
            clear-icon="fas fa-times xsmall"
            label="관람평"
            rows="1"
            auto-grow
            hide-details="auto"
            color="orange darken-3"
            dense
          ></v-textarea>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeMe()">Close</v-btn>
        <v-btn color="blue darken-1" text @click="submit(editedRating)">Save</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>


export default {
  name: "RatingEditForm",
  props:["rating", "id"],
  components: {
    },
  data() {
    return {
      rules: [
        value => !!value || '점수를 입력해주세요.',
        value => ( value <= 5 ) || '최고 점수는 5점입니다.',
        value => ( value < 0.5 ) || '최저 점수는 0.5점입니다.',
      ],
      editedRating: {
        id: this.rating.id,
        score: this.rating.score,
        comment: this.rating.comment,
        movie: this.id,
        user: this.rating.user,
      },
    }
  },
  methods: {
    closeMe() {
      this.$emit("close");
    },
    async submit(editedRating) {
      console.log(editedRating)
      await this.$emit("editRating", editedRating);

    },    
  },
}
</script>
<style src="./RatingForm.css" scoped></style>
<template>
   <v-rating
      class="score"
      :value=score
      background-color="orange lighten-3"
      color="amber"
      dense
      half-increments
      readonly
      size="14"></v-rating>
</template>

<script>
export default {
  name: 'Score',
  props: ["score"],

}
</script>

<style src="./Ratings.css" scoped></style>
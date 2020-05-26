<template>
   <v-rating
      :value=rating
      background-color="orange lighten-3"
      color="amber"
      dense
      half-increments
      readonly
      size="14"></v-rating>
</template>

<script>
export default {
  name: 'Rating',
  props: ["rating"],

}
</script>


<template>
  <div class="container">
    <iframe 
      v-if="details.trailer"
      class="iframe"
      type="text/html" 
      allow="autoplay"
      frameborder=0
      allowfullscreen
      :src="details.trailer"
      ></iframe>
    <v-img
      v-else-if="details.poster"
      class="media"
      :src="details.poster" />
    <v-img 
      v-else
      class="media"
      src="./defaultImg.jpg" />
  </div>
</template>

<script>

export default {
  name: "MovieTrailer",
  props: ["details"],

}
</script>

<style src="./MovieTrailer.css" scoped></style>
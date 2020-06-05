<template>
  <div v-if="details.trailer" class="trailer-container">
    <iframe 
      class="iframe"
      type="text/html" 
      allow="autoplay"
      frameborder=0
      allowfullscreen
      :src="details.trailer"
      ></iframe>
  </div>
  
  <div v-else class="image-container">
    <v-img
      v-if="details.poster"
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